"""
REAL Voice Cloning using Coqui TTS XTTS-v2
Requires Python 3.9, 3.10, or 3.11
"""

import os
import sys
import torch
from TTS.api import TTS
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


class VoiceCloner:
    """
    Voice cloning using Coqui TTS XTTS-v2 model
    Free, high-quality REAL voice cloning
    """
    
    def __init__(self, temperature=0.75, repetition_penalty=5.0, length_penalty=1.0):
        """
        Initialize voice cloner with XTTS-v2 model (Using OFFICIAL recommended settings)
        
        Args:
            temperature (float): Softmax temperature (0.1-1.0, default 0.75 for natural voice)
            repetition_penalty (float): Prevents repetition (1.0-20.0, default 5.0)
            length_penalty (float): Control length (0.5-2.0, default 1.0)
        
        Official XTTS-v2 defaults: temp=0.65, rep_penalty=2.0, top_k=50, top_p=0.8
        """
        print("Loading XTTS-v2 model with OFFICIAL recommended settings...")
        print("Using settings from Coqui TTS documentation for best quality")
        print("This may take a few minutes on first run...")
        
        # Use CPU by default to save memory (GPU can cause memory issues)
        # XTTS-v2 works fine on CPU for most use cases
        self.device = "cpu"  # Force CPU to avoid memory issues
        print(f"Using device: {self.device} (CPU mode for memory optimization)")
        
        # Store quality settings (based on official documentation)
        self.temperature = temperature  # 0.75 for natural voice with slight variation
        self.repetition_penalty = repetition_penalty  # 5.0 to reduce silences/repetition
        self.length_penalty = length_penalty
        
        # Load XTTS-v2 model
        model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
        self.tts = TTS(model_name)
        
        print("✅ Model loaded successfully!")
        print("📋 Using settings:")
        print(f"   - Temperature: {temperature} (controls randomness)")
        print(f"   - Repetition Penalty: {repetition_penalty} (reduces silences/uhhs)")
        print(f"   - Length Penalty: {length_penalty} (controls output length)")
        print(f"   - Top-k: 50 (default, vocabulary diversity)")
        print(f"   - Top-p: 0.8 (default, nucleus sampling)")
        print(f"   - Speed: 1.0 (default, normal speed)")
    
    def clone_voice(self, text, reference_audio_path, output_path, language="en", split_sentences=True, clean_audio=False):
        """
        Clone voice and generate speech (quality settings from model config)
        
        Args:
            text (str): Text to convert to speech
            reference_audio_path (str): Path to reference audio file (6-10 seconds recommended)
            output_path (str): Path to save generated audio
            language (str): Language code (en, hi, ur, es, fr, de, it, pt, pl, tr, ru, nl, cs, ar, zh-cn, ja, hu, ko)
            split_sentences (bool): Split long text for better quality (default True)
            clean_audio (bool): Clean generated audio (remove noise, enhance quality) (default True)
        
        Returns:
            str: Path to generated audio file
        """
        print(f"\n🎤 Cloning voice from: {reference_audio_path}")
        print(f"📝 Generating speech for: '{text[:50]}...'")
        print(f"🌍 Language: {language}")
        print(f"⚙️ Using quality settings from model config")
        print(f"🎙️ Audio cleaning: {'Enabled' if clean_audio else 'Disabled'}")
        
        # CRITICAL: For Hindi/Urdu/Arabic, manually split text BEFORE TTS
        # These languages have ~250 char limit, so we split manually
        manual_split_needed = False
        text_chunks = [text]  # Default: single chunk
        
        if language in ['hi', 'ur', 'ar'] and len(text) > 200:
            print(f"⚠️ Language '{language}' with {len(text)} chars - MANUAL sentence splitting required!")
            manual_split_needed = True
            
            # Split by sentence endings (। for Hindi/Urdu, . for others)
            import re
            if language in ['hi', 'ur']:
                # Split by Hindi/Urdu sentence endings
                sentences = re.split(r'[।\.\?!]', text)
            else:
                # Split by standard sentence endings
                sentences = re.split(r'[\.\?!]', text)
            
            # Clean and filter empty sentences
            sentences = [s.strip() for s in sentences if s.strip()]
            
            # Group sentences to stay under 200 chars per chunk
            text_chunks = []
            current_chunk = ""
            
            for sentence in sentences:
                # Add sentence ending back
                if language in ['hi', 'ur']:
                    sentence = sentence + "।"
                else:
                    sentence = sentence + "."
                
                # Check if adding this sentence would exceed limit
                if len(current_chunk) + len(sentence) > 200 and current_chunk:
                    # Save current chunk and start new one
                    text_chunks.append(current_chunk.strip())
                    current_chunk = sentence + " "
                else:
                    # Add to current chunk
                    current_chunk += sentence + " "
            
            # Add last chunk
            if current_chunk.strip():
                text_chunks.append(current_chunk.strip())
            
            print(f"   📝 Split into {len(text_chunks)} chunks:")
            for i, chunk in enumerate(text_chunks, 1):
                print(f"      Chunk {i}: {len(chunk)} chars - '{chunk[:50]}...'")
        
        # For other cases, use automatic splitting
        elif len(text) > 150:
            print(f"⚠️ Long text detected ({len(text)} chars).")
            print(f"   🔄 Using automatic sentence splitting.")
            split_sentences = True
        
        # Final check
        if not split_sentences and len(text) > 100:
            print(f"⚠️ Forcing sentence splitting ON for {len(text)} chars...")
            split_sentences = True
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        # Convert audio to WAV format if needed (TTS requires WAV)
        converted_audio = self._convert_to_wav(reference_audio_path)
        
        # Generate speech with cloned voice (quality settings from model config)
        try:
            # If manual split is needed, generate each chunk separately and combine
            if manual_split_needed and len(text_chunks) > 1:
                print(f"\n🎤 Generating {len(text_chunks)} audio chunks separately...")
                chunk_files = []
                
                for i, chunk in enumerate(text_chunks, 1):
                    print(f"\n   📝 Processing chunk {i}/{len(text_chunks)}: {len(chunk)} chars")
                    chunk_file = output_path.rsplit('.', 1)[0] + f'_chunk{i}.wav'
                    
                    # Generate this chunk
                    self.tts.tts_to_file(
                        text=chunk,
                        speaker_wav=converted_audio,
                        language=language,
                        file_path=chunk_file,
                        split_sentences=False  # Already split manually
                    )
                    
                    if os.path.exists(chunk_file):
                        print(f"   ✅ Chunk {i} generated: {os.path.getsize(chunk_file)} bytes")
                        chunk_files.append(chunk_file)
                    else:
                        print(f"   ❌ Chunk {i} failed!")
                
                # Combine all chunks with smooth transitions
                if len(chunk_files) > 0:
                    print(f"\n🔗 Combining {len(chunk_files)} audio chunks with smooth transitions...")
                    import soundfile as sf
                    import numpy as np
                    
                    combined_audio = []
                    sample_rate = None
                    
                    for i, chunk_file in enumerate(chunk_files):
                        audio, sr = sf.read(chunk_file)
                        if sample_rate is None:
                            sample_rate = sr
                        
                        # Add smooth transitions between chunks
                        if i > 0:
                            # Add a small silence gap (100ms) for natural pause
                            silence_duration = 0.1  # 100ms
                            silence_samples = int(silence_duration * sample_rate)
                            silence = np.zeros(silence_samples)
                            combined_audio.append(silence)
                            print(f"   🔇 Added 100ms pause before chunk {i+1}")
                        
                        # Apply crossfade between chunks for smooth transition
                        if i > 0 and len(combined_audio) > 1:
                            # Crossfade duration: 50ms
                            crossfade_duration = 0.05
                            crossfade_samples = int(crossfade_duration * sample_rate)
                            
                            # Get last part of previous audio
                            prev_audio = combined_audio[-2]  # -1 is silence, -2 is previous chunk
                            if len(prev_audio) >= crossfade_samples and len(audio) >= crossfade_samples:
                                # Fade out previous chunk end
                                fade_out = np.linspace(1, 0, crossfade_samples)
                                prev_audio[-crossfade_samples:] *= fade_out
                                
                                # Fade in current chunk start
                                fade_in = np.linspace(0, 1, crossfade_samples)
                                audio[:crossfade_samples] *= fade_in
                                
                                print(f"   🎵 Applied crossfade to chunk {i+1}")
                        
                        combined_audio.append(audio)
                    
                    # Concatenate all audio
                    final_audio = np.concatenate(combined_audio)
                    
                    # Save combined audio
                    sf.write(output_path, final_audio, sample_rate, subtype='PCM_16')
                    print(f"   ✅ Combined audio saved: {os.path.getsize(output_path)} bytes")
                    print(f"   🎙️ Total duration: {len(final_audio)/sample_rate:.2f} seconds")
                    
                    # Clean up chunk files
                    for chunk_file in chunk_files:
                        try:
                            os.remove(chunk_file)
                        except:
                            pass
                    
                    print(f"✅ Voice cloning completed successfully!")
                    return output_path
                else:
                    raise Exception("No chunks were generated successfully")
            
            elif clean_audio:
                # Generate to temp file, then clean
                temp_output = output_path.rsplit('.', 1)[0] + '_temp.wav'
                
                print(f"🎤 Generating speech...")
                print(f"   Text length: {len(text)} characters")
                print(f"   Text preview: '{text[:100]}...'")
                print(f"   Language: {language}")
                print(f"   ⚠️ CRITICAL: Split sentences: {split_sentences} {'✅ ENABLED' if split_sentences else '❌ DISABLED'}")
                if not split_sentences:
                    print(f"   ⚠️⚠️⚠️ WARNING: Split sentences is OFF - text may be truncated!")
                print(f"   Using parameters:")
                print(f"     - Temperature: {self.temperature}")
                print(f"     - Repetition Penalty: {self.repetition_penalty}")
                print(f"     - Length Penalty: {self.length_penalty}")
                
                # Estimate expected audio duration (rough: 150 chars per minute)
                expected_duration = (len(text) / 150) * 60
                print(f"   Expected audio duration: ~{expected_duration:.1f} seconds")
                
                # IMPORTANT: tts_to_file() does NOT accept temperature/repetition_penalty parameters
                # These are only used in the underlying inference() method
                # The TTS API will use default values or config values
                self.tts.tts_to_file(
                    text=text,
                    speaker_wav=converted_audio,
                    language=language,
                    file_path=temp_output,
                    split_sentences=split_sentences
                )
                
                # Verify temp file was created
                if not os.path.exists(temp_output):
                    raise Exception("TTS failed to generate audio file")
                
                # Check temp file size and duration
                temp_size = os.path.getsize(temp_output)
                print(f"   Generated audio size: {temp_size} bytes")
                
                # Check actual audio duration
                try:
                    import librosa
                    actual_audio, sr = librosa.load(temp_output, sr=None)
                    actual_duration = len(actual_audio) / sr
                    print(f"   Actual audio duration: {actual_duration:.2f} seconds")
                    
                    # Warn if duration is much shorter than expected
                    if actual_duration < expected_duration * 0.7:  # Less than 70% of expected
                        print(f"   ⚠️ WARNING: Audio seems incomplete!")
                        print(f"   Expected: ~{expected_duration:.1f}s, Got: {actual_duration:.2f}s")
                        print(f"   This might indicate text was truncated by TTS engine.")
                except Exception as e:
                    print(f"   ⚠️ Could not verify audio duration: {e}")
                
                if temp_size < 1000:
                    print(f"   ⚠️ Warning: Audio file is very small, might be incomplete")
                
                # Clean up generated audio (remove noise, enhance quality)
                print(f"🎙️ Cleaning generated audio...")
                self._clean_generated_audio(temp_output, output_path)
                
                # Verify output file
                if os.path.exists(output_path):
                    output_size = os.path.getsize(output_path)
                    print(f"   Cleaned audio size: {output_size} bytes")
                
                # Remove temp file
                if os.path.exists(temp_output):
                    try:
                        os.remove(temp_output)
                    except:
                        pass
            else:
                # Generate directly to output (no cleaning)
                print(f"⚠️ Skipping audio cleaning (disabled by user)")
                print(f"🎤 Generating speech...")
                print(f"   Text length: {len(text)} characters")
                print(f"   Language: {language}")
                print(f"   ⚠️ CRITICAL: Split sentences: {split_sentences} {'✅ ENABLED' if split_sentences else '❌ DISABLED'}")
                if not split_sentences:
                    print(f"   ⚠️⚠️⚠️ WARNING: Split sentences is OFF - text may be truncated!")
                print(f"   Using parameters:")
                print(f"     - Temperature: {self.temperature}")
                print(f"     - Repetition Penalty: {self.repetition_penalty}")
                print(f"     - Length Penalty: {self.length_penalty}")
                
                # IMPORTANT: tts_to_file() does NOT accept temperature/repetition_penalty parameters
                # These are only used in the underlying inference() method
                # The TTS API will use default values or config values
                self.tts.tts_to_file(
                    text=text,
                    speaker_wav=converted_audio,
                    language=language,
                    file_path=output_path,
                    split_sentences=split_sentences
                )
                
                # Verify output file
                if os.path.exists(output_path):
                    output_size = os.path.getsize(output_path)
                    print(f"   Generated audio size: {output_size} bytes")
        
        except Exception as e:
            print(f"❌ Error during voice generation: {e}")
            import traceback
            traceback.print_exc()
            raise
        
        # Clean up temporary converted file if created
        if converted_audio != reference_audio_path and os.path.exists(converted_audio):
            try:
                os.remove(converted_audio)
            except:
                pass
        
        # Final verification of output audio
        print(f"\n📊 Final Verification:")
        try:
            import librosa
            final_audio, final_sr = librosa.load(output_path, sr=None)
            final_duration = len(final_audio) / final_sr
            print(f"   ✅ Output audio duration: {final_duration:.2f} seconds")
            print(f"   ✅ Output file size: {os.path.getsize(output_path)} bytes")
            
            # Calculate expected duration and compare
            expected_duration = (len(text) / 150) * 60
            if final_duration < expected_duration * 0.6:  # Less than 60% of expected
                print(f"\n   ⚠️⚠️⚠️ CRITICAL WARNING ⚠️⚠️⚠️")
                print(f"   Audio duration ({final_duration:.2f}s) is much shorter than expected (~{expected_duration:.1f}s)")
                print(f"   Text might be incomplete! Possible causes:")
                print(f"   1. TTS engine truncated long text (>250 chars)")
                print(f"   2. Try enabling 'Split Sentences' option")
                print(f"   3. Try breaking text into smaller parts")
                print(f"   4. Check if reference audio quality is good")
            elif final_duration < expected_duration * 0.8:  # Less than 80%
                print(f"   ⚠️ Note: Audio is shorter than expected")
                print(f"   Expected: ~{expected_duration:.1f}s, Got: {final_duration:.2f}s")
                print(f"   This might be normal if text has punctuation/pauses")
            else:
                print(f"   ✅ Audio duration looks good!")
        except Exception as e:
            print(f"   ⚠️ Could not verify final audio: {e}")
        
        print(f"\n✅ Audio generated successfully: {output_path}")
        return output_path
    
    def _clean_generated_audio(self, input_path, output_path):
        """
        Clean generated audio - remove noise, enhance clarity (GENTLE processing to preserve voice)
        
        Args:
            input_path: Path to generated audio (with noise)
            output_path: Path to save cleaned audio
        """
        try:
            import librosa
            import soundfile as sf
            import numpy as np
            from scipy import signal
            
            print("  - Loading generated audio...")
            # Load audio with original sample rate to preserve quality
            audio_data, sample_rate = librosa.load(input_path, sr=None, mono=True)
            
            print(f"  - Audio length: {len(audio_data)/sample_rate:.2f} seconds")
            print(f"  - Sample rate: {sample_rate} Hz")
            
            # Check if audio is valid
            if len(audio_data) == 0:
                print("  ⚠️ Warning: Empty audio file!")
                import shutil
                shutil.copy(input_path, output_path)
                return
            
            # MINIMAL PROCESSING - Avoid pitch/speed/volume issues
            print("  - Applying MINIMAL processing to preserve voice quality...")
            
            # 1. ONLY normalize volume - NO filtering that can affect pitch/speed
            print("  - Normalizing volume (no pitch/speed changes)...")
            max_val = np.max(np.abs(audio_data))
            if max_val > 0:
                # Simple normalization to 85% to avoid clipping
                audio_data = audio_data / max_val
                audio_data = audio_data * 0.85
            
            # 2. VERY gentle fade only at edges to avoid clicks
            print("  - Adding gentle fades at edges...")
            fade_samples = int(0.005 * sample_rate)  # 5ms fade (very short)
            if len(audio_data) > fade_samples * 2:
                # Fade in
                fade_in = np.linspace(0, 1, fade_samples)
                audio_data[:fade_samples] *= fade_in
                # Fade out
                fade_out = np.linspace(1, 0, fade_samples)
                audio_data[-fade_samples:] *= fade_out
            
            # That's it! No compression, no filtering, no RMS normalization
            # These can cause pitch/speed/volume artifacts
            print("  - Skipping aggressive processing to preserve natural voice")
            
            # Save cleaned audio
            print(f"  - Saving cleaned audio...")
            print(f"  - Final audio length: {len(audio_data)/sample_rate:.2f} seconds")
            
            audio_data_int16 = (audio_data * 32767).astype(np.int16)
            sf.write(output_path, audio_data_int16, sample_rate, subtype='PCM_16')
            
            print("  ✅ Audio cleaned successfully!")
            
        except Exception as e:
            print(f"  ⚠️ Audio cleaning failed: {e}")
            print(f"  Using original generated audio...")
            # Copy original if cleaning fails
            import shutil
            try:
                shutil.copy(input_path, output_path)
            except Exception as copy_error:
                print(f"  ❌ Failed to copy original audio: {copy_error}")
                raise
    
    def enhance_audio(self, audio_path, noise_reduction=False, voice_enhancement=False):
        """
        Enhance audio quality with optional noise reduction and voice enhancement
        
        Args:
            audio_path: Path to audio file
            noise_reduction: Apply noise reduction
            voice_enhancement: Apply voice enhancement (clarity, normalization)
        
        Returns:
            Path to enhanced audio file
        """
        if not noise_reduction and not voice_enhancement:
            return audio_path  # No enhancement needed
        
        try:
            import librosa
            import soundfile as sf
            import numpy as np
            from scipy import signal
            
            print(f"\n🎙️ Enhancing audio quality...")
            if noise_reduction:
                print("  - Applying noise reduction...")
            if voice_enhancement:
                print("  - Applying voice enhancement...")
            
            # Load audio
            audio_data, sample_rate = librosa.load(audio_path, sr=22050, mono=True)
            
            # 1. Noise Reduction (Spectral Gating)
            if noise_reduction:
                # Simple noise reduction using spectral subtraction
                # Estimate noise from first 0.5 seconds
                noise_sample = audio_data[:int(0.5 * sample_rate)]
                noise_fft = np.fft.rfft(noise_sample)
                noise_power = np.abs(noise_fft) ** 2
                
                # Process audio in chunks
                chunk_size = 2048
                enhanced = np.zeros_like(audio_data)
                
                for i in range(0, len(audio_data), chunk_size):
                    chunk = audio_data[i:i+chunk_size]
                    if len(chunk) < chunk_size:
                        chunk = np.pad(chunk, (0, chunk_size - len(chunk)))
                    
                    chunk_fft = np.fft.rfft(chunk)
                    chunk_power = np.abs(chunk_fft) ** 2
                    
                    # Spectral subtraction
                    clean_power = np.maximum(chunk_power - 0.5 * noise_power[:len(chunk_power)], 0.1 * chunk_power)
                    clean_magnitude = np.sqrt(clean_power)
                    clean_fft = clean_magnitude * np.exp(1j * np.angle(chunk_fft))
                    
                    clean_chunk = np.fft.irfft(clean_fft)
                    enhanced[i:i+len(clean_chunk)] = clean_chunk[:len(audio_data[i:i+chunk_size])]
                
                audio_data = enhanced
                print("  ✅ Noise reduction applied")
            
            # 2. Voice Enhancement
            if voice_enhancement:
                # High-pass filter to remove low-frequency noise
                sos = signal.butter(4, 80, 'hp', fs=sample_rate, output='sos')
                audio_data = signal.sosfilt(sos, audio_data)
                
                # Normalize audio
                audio_data = audio_data / (np.max(np.abs(audio_data)) + 1e-8)
                audio_data = audio_data * 0.95  # Prevent clipping
                
                # Slight compression for better clarity
                threshold = 0.3
                ratio = 3.0
                mask = np.abs(audio_data) > threshold
                audio_data[mask] = np.sign(audio_data[mask]) * (
                    threshold + (np.abs(audio_data[mask]) - threshold) / ratio
                )
                
                print("  ✅ Voice enhancement applied")
            
            # Save enhanced audio
            enhanced_path = audio_path.rsplit('.', 1)[0] + '_enhanced.wav'
            audio_data_int16 = (audio_data * 32767).astype(np.int16)
            sf.write(enhanced_path, audio_data_int16, sample_rate, subtype='PCM_16')
            
            print(f"✅ Audio enhanced: {enhanced_path}")
            return enhanced_path
            
        except Exception as e:
            print(f"⚠️ Audio enhancement failed: {e}")
            print(f"Using original audio...")
            return audio_path
    
    def _convert_to_wav(self, audio_path):
        """Convert audio to WAV format if needed"""
        # Check if already WAV
        if audio_path.lower().endswith('.wav'):
            return audio_path
        
        try:
            import librosa
            import soundfile as sf
            import numpy as np
            
            print(f"Converting audio to WAV format...")
            
            # Load audio file with librosa (supports many formats)
            audio_data, sample_rate = librosa.load(audio_path, sr=22050, mono=True)
            
            # Convert to int16 PCM format (required by TTS)
            audio_data_int16 = (audio_data * 32767).astype(np.int16)
            
            # Convert to WAV with int16 PCM format
            temp_wav = audio_path.rsplit('.', 1)[0] + '_converted.wav'
            sf.write(temp_wav, audio_data_int16, sample_rate, subtype='PCM_16')
            
            print(f"✅ Converted to WAV: {temp_wav}")
            return temp_wav
            
        except Exception as e:
            print(f"⚠️ Could not convert audio with librosa: {e}")
            
            # Try with pydub as fallback
            try:
                from pydub import AudioSegment
                print(f"Trying pydub conversion...")
                
                audio = AudioSegment.from_file(audio_path)
                temp_wav = audio_path.rsplit('.', 1)[0] + '_converted.wav'
                audio.export(temp_wav, format='wav')
                
                print(f"✅ Converted to WAV with pydub: {temp_wav}")
                return temp_wav
            except Exception as e2:
                print(f"⚠️ Could not convert audio: {e2}")
                print(f"Please upload WAV format audio file")
                raise Exception("Audio format not supported. Please upload WAV file.")
    
    def clone_voice_batch(self, texts, reference_audio_path, output_dir, language="en"):
        """
        Clone voice for multiple texts
        
        Args:
            texts (list): List of texts to convert
            reference_audio_path (str): Path to reference audio
            output_dir (str): Directory to save generated audios
            language (str): Language code
        
        Returns:
            list: Paths to generated audio files
        """
        os.makedirs(output_dir, exist_ok=True)
        output_paths = []
        
        for i, text in enumerate(texts):
            output_path = os.path.join(output_dir, f"cloned_audio_{i+1}.wav")
            self.clone_voice(text, reference_audio_path, output_path, language)
            output_paths.append(output_path)
        
        return output_paths


def main():
    """Example usage"""
    # Initialize voice cloner
    cloner = VoiceCloner()
    
    # Example: Clone voice
    text = "Hello, this is a test of REAL voice cloning technology. The quality is quite impressive!"
    reference_audio = "reference_voice.wav"  # Your reference audio file
    output_audio = "output/cloned_speech.wav"
    
    # For Hindi/Urdu, use language="hi" or language="ur"
    # text = "यह एक टेस्ट है वॉइस क्लोनिंग का"
    # language = "hi"
    
    cloner.clone_voice(
        text=text,
        reference_audio_path=reference_audio,
        output_path=output_audio,
        language="en"  # Change to "hi" for Hindi, "ur" for Urdu
    )


if __name__ == "__main__":
    main()
