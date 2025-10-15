"""
Flask Web Application for Voice Cloning and Video Integration
Beautiful UI with voice recorder, text input, and video upload
"""

from flask import Flask, render_template, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
import os
import sys
import uuid
from pathlib import Path
from voice_cloner import VoiceCloner
from video_processor_ffmpeg import VideoProcessor
import threading
import json

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['TEMP_FOLDER'] = 'temp'

# Create necessary folders
for folder in [app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER'], app.config['TEMP_FOLDER']]:
    os.makedirs(folder, exist_ok=True)

# Allowed file extensions
ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm'}
ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3', 'ogg', 'webm', 'm4a'}

# Global variables
voice_cloner = None
video_processor = VideoProcessor()
processing_status = {}


def allowed_file(filename, allowed_extensions):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def get_voice_cloner(temperature=0.75, repetition_penalty=5.0, length_penalty=1.0):
    """Get or create voice cloner instance with quality settings (loads on demand to save memory)"""
    global voice_cloner
    if voice_cloner is None:
        print("📦 Loading TTS model (first time may take a while)...")
        voice_cloner = VoiceCloner(
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            length_penalty=length_penalty
        )
    return voice_cloner


def clear_memory():
    """Clear memory by releasing model and running garbage collection"""
    global voice_cloner
    import gc
    import torch
    
    print("🧹 Clearing memory...")
    
    # Clear voice cloner
    if voice_cloner is not None:
        del voice_cloner
        voice_cloner = None
    
    # Clear CUDA cache if available
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        print("   - CUDA cache cleared")
    
    # Run garbage collection
    gc.collect()
    print("   - Garbage collection done")
    print("✅ Memory cleared!")


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/languages', methods=['GET'])
def get_languages():
    """Get supported languages"""
    languages = [
        {'code': 'en', 'name': 'English'},
        {'code': 'hi', 'name': 'Hindi (हिंदी)'},
        {'code': 'ur', 'name': 'Urdu (اردو)'},
        {'code': 'es', 'name': 'Spanish'},
        {'code': 'fr', 'name': 'French'},
        {'code': 'de', 'name': 'German'},
        {'code': 'it', 'name': 'Italian'},
        {'code': 'pt', 'name': 'Portuguese'},
        {'code': 'pl', 'name': 'Polish'},
        {'code': 'tr', 'name': 'Turkish'},
        {'code': 'ru', 'name': 'Russian'},
        {'code': 'nl', 'name': 'Dutch'},
        {'code': 'cs', 'name': 'Czech'},
        {'code': 'ar', 'name': 'Arabic'},
        {'code': 'zh-cn', 'name': 'Chinese'},
        {'code': 'ja', 'name': 'Japanese'},
        {'code': 'hu', 'name': 'Hungarian'},
        {'code': 'ko', 'name': 'Korean'}
    ]
    return jsonify(languages)


@app.route('/api/upload-reference-audio', methods=['POST'])
def upload_reference_audio():
    """Upload reference audio for voice cloning"""
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        file = request.files['audio']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Get enhancement options
        noise_reduction = request.form.get('noiseReduction', 'false').lower() == 'true'
        voice_enhancement = request.form.get('voiceEnhancement', 'false').lower() == 'true'
        
        if file and allowed_file(file.filename, ALLOWED_AUDIO_EXTENSIONS):
            # Generate unique filename
            file_ext = file.filename.rsplit('.', 1)[1].lower()
            temp_filename = f"reference_{uuid.uuid4().hex}.{file_ext}"
            temp_filepath = os.path.join(app.config['UPLOAD_FOLDER'], temp_filename)
            
            file.save(temp_filepath)
            
            # Convert to WAV format immediately
            try:
                import librosa
                import soundfile as sf
                import numpy as np
                
                # Load and convert to WAV
                audio_data, sample_rate = librosa.load(temp_filepath, sr=22050, mono=True)
                
                # Convert to int16 PCM format (required by TTS)
                audio_data_int16 = (audio_data * 32767).astype(np.int16)
                
                # Save as WAV with int16 PCM format
                wav_filename = f"reference_{uuid.uuid4().hex}.wav"
                wav_filepath = os.path.join(app.config['UPLOAD_FOLDER'], wav_filename)
                sf.write(wav_filepath, audio_data_int16, sample_rate, subtype='PCM_16')
                
                # Apply enhancement if requested
                if noise_reduction or voice_enhancement:
                    cloner = get_voice_cloner()
                    enhanced_path = cloner.enhance_audio(wav_filepath, noise_reduction, voice_enhancement)
                    
                    # Use enhanced audio
                    if enhanced_path != wav_filepath:
                        # Delete original, use enhanced
                        try:
                            os.remove(wav_filepath)
                        except:
                            pass
                        wav_filepath = enhanced_path
                        wav_filename = os.path.basename(enhanced_path)
                
                # Delete temporary file if not WAV
                if file_ext != 'wav':
                    try:
                        os.remove(temp_filepath)
                    except:
                        pass
                
                return jsonify({
                    'success': True,
                    'filename': wav_filename,
                    'filepath': wav_filepath
                })
                
            except Exception as conv_error:
                # If conversion fails, return original file
                print(f"Conversion warning: {conv_error}")
                return jsonify({
                    'success': True,
                    'filename': temp_filename,
                    'filepath': temp_filepath
                })
        
        return jsonify({'error': 'Invalid file type'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/upload-video', methods=['POST'])
def upload_video():
    """Upload video file"""
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        file = request.files['video']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and allowed_file(file.filename, ALLOWED_VIDEO_EXTENSIONS):
            # Generate unique filename
            file_ext = file.filename.rsplit('.', 1)[1].lower()
            filename = f"video_{uuid.uuid4().hex}.{file_ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)
            
            # Get video info
            info = video_processor.get_video_info(filepath)
            
            return jsonify({
                'success': True,
                'filename': filename,
                'filepath': filepath,
                'duration': info['duration'],
                'fps': info['fps'],
                'size': info['size']
            })
        
        return jsonify({'error': 'Invalid file type'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/process', methods=['POST'])
def process_voice_cloning():
    """Process voice cloning and video integration"""
    try:
        data = request.json
        
        # Validate input
        required_fields = ['text', 'referenceAudio', 'video', 'language']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
        
        text = data['text']
        reference_audio = data['referenceAudio']
        video_file = data['video']
        language = data['language']
        replace_audio = data.get('replaceAudio', True)
        audio_start_time = data.get('audioStartTime', 0)
        
        # Quality settings
        speed = float(data.get('speed', 1.0))
        temperature = float(data.get('temperature', 0.65))
        repetition_penalty = float(data.get('repetitionPenalty', 7.0))
        length_penalty = float(data.get('lengthPenalty', 1.0))
        enable_text_splitting = data.get('enableTextSplitting', True)
        enable_audio_cleaning = data.get('enableAudioCleaning', True)
        
        # Generate unique job ID
        job_id = uuid.uuid4().hex
        
        # Initialize status
        processing_status[job_id] = {
            'status': 'processing',
            'progress': 0,
            'message': 'Starting voice cloning...'
        }
        
        # Process in background thread
        thread = threading.Thread(
            target=process_job,
            args=(job_id, text, reference_audio, video_file, language, replace_audio, audio_start_time,
                  speed, temperature, repetition_penalty, length_penalty, enable_text_splitting, enable_audio_cleaning)
        )
        thread.start()
        
        return jsonify({
            'success': True,
            'jobId': job_id
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def process_job(job_id, text, reference_audio, video_file, language, replace_audio, audio_start_time,
                speed=1.0, temperature=0.65, repetition_penalty=7.0, length_penalty=1.0, enable_text_splitting=True, enable_audio_cleaning=True):
    """Background job for processing"""
    try:
        # Update status
        processing_status[job_id]['message'] = 'Loading voice cloning model...'
        processing_status[job_id]['progress'] = 10
        
        # Get voice cloner with quality settings
        cloner = get_voice_cloner(
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            length_penalty=length_penalty
        )
        
        # Step 1: Clone voice
        processing_status[job_id]['message'] = 'Cloning voice with quality settings...'
        processing_status[job_id]['progress'] = 20
        
        reference_audio_path = os.path.join(app.config['UPLOAD_FOLDER'], reference_audio)
        temp_audio_path = os.path.join(app.config['TEMP_FOLDER'], f"cloned_{job_id}.wav")
        
        # Update progress during voice cloning
        processing_status[job_id]['progress'] = 30
        processing_status[job_id]['message'] = 'Analyzing reference voice with enhanced quality...'
        
        cloner.clone_voice(
            text=text,
            reference_audio_path=reference_audio_path,
            output_path=temp_audio_path,
            language=language,
            split_sentences=enable_text_splitting,
            clean_audio=enable_audio_cleaning
        )
        
        # Step 2: Add to video
        processing_status[job_id]['message'] = 'Voice cloned! Adding audio to video...'
        processing_status[job_id]['progress'] = 60
        
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file)
        output_filename = f"output_{job_id}.mp4"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        
        # Update progress during video processing
        processing_status[job_id]['progress'] = 70
        processing_status[job_id]['message'] = 'Processing video...'
        
        video_processor.add_audio_to_video(
            video_path=video_path,
            audio_path=temp_audio_path,
            output_path=output_path,
            replace_audio=replace_audio,
            audio_start_time=audio_start_time
        )
        
        # Complete
        processing_status[job_id]['status'] = 'completed'
        processing_status[job_id]['progress'] = 100
        processing_status[job_id]['message'] = 'Processing completed!'
        processing_status[job_id]['outputFile'] = output_filename
        processing_status[job_id]['downloadUrl'] = f'/api/download/{output_filename}'
        
    except Exception as e:
        # Fix encoding error in error messages
        error_msg = str(e).encode('utf-8', errors='replace').decode('utf-8')
        processing_status[job_id]['status'] = 'error'
        processing_status[job_id]['message'] = f'Error: {error_msg}'
        processing_status[job_id]['progress'] = 0


@app.route('/api/status/<job_id>', methods=['GET'])
def get_status(job_id):
    """Get processing status"""
    if job_id in processing_status:
        return jsonify(processing_status[job_id])
    return jsonify({'error': 'Job not found'}), 404


@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    """Download output file"""
    try:
        filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/clear-memory', methods=['POST'])
def api_clear_memory():
    """Clear memory - unload model and free resources"""
    try:
        clear_memory()
        return jsonify({'success': True, 'message': 'Memory cleared successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/cleanup', methods=['POST'])
def cleanup():
    """Cleanup old files"""
    try:
        data = request.json
        files_to_delete = data.get('files', [])
        
        for filename in files_to_delete:
            for folder in [app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER'], app.config['TEMP_FOLDER']]:
                filepath = os.path.join(folder, filename)
                if os.path.exists(filepath):
                    os.remove(filepath)
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Voice Cloning Web Application")
    print("="*60)
    print("\nStarting server...")
    
    # Get port from environment variable (for deployment) or use 5000 (for local)
    import os
    port = int(os.environ.get('PORT', 5000))
    
    print(f"Open your browser and go to: http://localhost:{port}")
    print("\nPress Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    # Use debug=False for production deployment
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
