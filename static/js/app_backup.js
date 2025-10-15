// Voice Cloning Web App JavaScript

let mediaRecorder;
let audioChunks = [];
let recordingStartTime;
let recordingInterval;
let audioBlob = null;
let uploadedReferenceAudio = null;
let uploadedVideo = null;

// DOM Elements
const recordBtn = document.getElementById('recordBtn');
const stopBtn = document.getElementById('stopBtn');
const reRecordBtn = document.getElementById('reRecordBtn');
const recordingTimer = document.getElementById('recordingTimer');
const audioPlayer = document.getElementById('audioPlayer');
const audioPreview = document.getElementById('audioPreview');
const visualizerCanvas = document.getElementById('visualizerCanvas');
const audioVisualizer = document.getElementById('audioVisualizer');

const referenceAudioFile = document.getElementById('referenceAudioFile');
const audioFileName = document.getElementById('audioFileName');

const textInput = document.getElementById('textInput');
const charCount = document.getElementById('charCount');
const language = document.getElementById('language');

const videoFile = document.getElementById('videoFile');
const videoFileName = document.getElementById('videoFileName');
const videoPreview = document.getElementById('videoPreview');
const videoPlayer = document.getElementById('videoPlayer');
const videoInfo = document.getElementById('videoInfo');

const replaceAudio = document.getElementById('replaceAudio');
const audioStartTime = document.getElementById('audioStartTime');

const processBtn = document.getElementById('processBtn');
const progressCard = document.getElementById('progressCard');
const progressFill = document.getElementById('progressFill');
const progressMessage = document.getElementById('progressMessage');
const progressPercentage = document.getElementById('progressPercentage');

const resultCard = document.getElementById('resultCard');
const downloadBtn = document.getElementById('downloadBtn');
const newProcessBtn = document.getElementById('newProcessBtn');

let currentJobId = null;
let downloadUrl = null;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    checkProcessButton();
});

function setupEventListeners() {
    // Recording
    recordBtn.addEventListener('click', startRecording);
    stopBtn.addEventListener('click', stopRecording);
    reRecordBtn.addEventListener('click', resetRecording);
    
    // File uploads
    referenceAudioFile.addEventListener('change', handleReferenceAudioUpload);
    videoFile.addEventListener('change', handleVideoUpload);
    
    // Text input
    textInput.addEventListener('input', () => {
        charCount.textContent = textInput.value.length;
        checkProcessButton();
    });
    
    // Process
    processBtn.addEventListener('click', startProcessing);
    
    // Download
    downloadBtn.addEventListener('click', downloadVideo);
    newProcessBtn.addEventListener('click', resetAll);
}

// Voice Recording
async function startRecording() {
    try {
        // Check if browser supports getUserMedia
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            alert('Your browser does not support microphone access.\n\nPlease use:\n- Chrome\n- Edge\n- Firefox\n\nOr upload an audio file instead.');
            return;
        }
        
        // Request microphone permission
        const stream = await navigator.mediaDevices.getUserMedia({ 
            audio: {
                echoCancellation: true,
                noiseSuppression: true,
                autoGainControl: true
            } 
        });
        
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        
        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };
        
        mediaRecorder.onstop = async () => {
            audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const audioUrl = URL.createObjectURL(audioBlob);
            audioPreview.src = audioUrl;
            audioPlayer.style.display = 'flex';
            audioVisualizer.style.display = 'none';
            
            // Upload to server
            await uploadRecordedAudio();
            
            updateStepStatus('step1', 'completed');
            checkProcessButton();
        };
        
        mediaRecorder.start();
        
        // UI updates
        recordBtn.disabled = true;
        stopBtn.disabled = false;
        recordingTimer.classList.add('recording');
        audioVisualizer.style.display = 'block';
        
        // Start timer
        recordingStartTime = Date.now();
        recordingInterval = setInterval(updateTimer, 100);
        
        // Visualizer
        setupVisualizer(stream);
        
    } catch (error) {
        console.error('Error accessing microphone:', error);
        
        let errorMessage = 'Could not access microphone.\n\n';
        
        if (error.name === 'NotAllowedError' || error.name === 'PermissionDeniedError') {
            errorMessage += '❌ Permission Denied\n\n';
            errorMessage += 'How to fix:\n';
            errorMessage += '1. Click the 🔒 lock icon in address bar\n';
            errorMessage += '2. Find "Microphone" setting\n';
            errorMessage += '3. Change to "Allow"\n';
            errorMessage += '4. Refresh the page\n\n';
            errorMessage += 'OR\n\n';
            errorMessage += '✅ Upload an audio file instead (click "Upload Audio File" button below)';
        } else if (error.name === 'NotFoundError') {
            errorMessage += '❌ No microphone found\n\n';
            errorMessage += 'Please:\n';
            errorMessage += '1. Connect a microphone\n';
            errorMessage += '2. Or upload an audio file instead';
        } else {
            errorMessage += '❌ Error: ' + error.message + '\n\n';
            errorMessage += 'Try:\n';
            errorMessage += '1. Refresh the page\n';
            errorMessage += '2. Use Chrome or Edge browser\n';
            errorMessage += '3. Or upload an audio file instead';
        }
        
        alert(errorMessage);
        
        // Highlight the upload button as alternative
        referenceAudioFile.parentElement.style.animation = 'pulse 1s ease-in-out 3';
    }
}

function stopRecording() {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
        mediaRecorder.stream.getTracks().forEach(track => track.stop());
        
        recordBtn.disabled = false;
        stopBtn.disabled = true;
        recordingTimer.classList.remove('recording');
        clearInterval(recordingInterval);
    }
}

function resetRecording() {
    audioPlayer.style.display = 'none';
    audioVisualizer.style.display = 'block';
    recordingTimer.textContent = '00:00';
    audioBlob = null;
    uploadedReferenceAudio = null;
    updateStepStatus('step1', '');
    checkProcessButton();
}

function updateTimer() {
    const elapsed = Date.now() - recordingStartTime;
    const seconds = Math.floor(elapsed / 1000);
    const milliseconds = Math.floor((elapsed % 1000) / 100);
    recordingTimer.textContent = `${String(seconds).padStart(2, '0')}:${milliseconds}`;
}

function setupVisualizer(stream) {
    const audioContext = new AudioContext();
    const analyser = audioContext.createAnalyser();
    const source = audioContext.createMediaStreamSource(stream);
    
    source.connect(analyser);
    analyser.fftSize = 256;
    
    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);
    
    const canvas = visualizerCanvas;
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    
    function draw() {
        if (mediaRecorder && mediaRecorder.state === 'recording') {
            requestAnimationFrame(draw);
        }
        
        analyser.getByteFrequencyData(dataArray);
        
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        const barWidth = (canvas.width / bufferLength) * 2.5;
        let x = 0;
        
        for (let i = 0; i < bufferLength; i++) {
            const barHeight = (dataArray[i] / 255) * canvas.height;
            
            const gradient = ctx.createLinearGradient(0, canvas.height - barHeight, 0, canvas.height);
            gradient.addColorStop(0, '#6366f1');
            gradient.addColorStop(1, '#8b5cf6');
            
            ctx.fillStyle = gradient;
            ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
            
            x += barWidth + 1;
        }
    }
    
    draw();
}

async function uploadRecordedAudio() {
    const formData = new FormData();
    formData.append('audio', audioBlob, 'recorded_audio.wav');
    
    try {
        const response = await fetch('/api/upload-reference-audio', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            uploadedReferenceAudio = data.filename;
            console.log('Audio uploaded:', uploadedReferenceAudio);
        } else {
            alert('Error uploading audio: ' + data.error);
        }
    } catch (error) {
        console.error('Upload error:', error);
        alert('Error uploading audio');
    }
}

// File Upload Handlers
async function handleReferenceAudioUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    audioFileName.textContent = file.name;
    
    const formData = new FormData();
    formData.append('audio', file);
    
    try {
        const response = await fetch('/api/upload-reference-audio', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            uploadedReferenceAudio = data.filename;
            updateStepStatus('step1', 'completed');
            checkProcessButton();
        } else {
            alert('Error uploading audio: ' + data.error);
        }
    } catch (error) {
        console.error('Upload error:', error);
        alert('Error uploading audio');
    }
}

async function handleVideoUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    videoFileName.textContent = file.name;
    
    const formData = new FormData();
    formData.append('video', file);
    
    try {
        const response = await fetch('/api/upload-video', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            uploadedVideo = data.filename;
            
            // Show preview
            const videoUrl = URL.createObjectURL(file);
            videoPlayer.src = videoUrl;
            videoPreview.style.display = 'block';
            
            // Show info
            videoInfo.innerHTML = `
                <strong>Duration:</strong> ${data.duration.toFixed(2)}s | 
                <strong>FPS:</strong> ${data.fps} | 
                <strong>Size:</strong> ${data.size[0]}x${data.size[1]}
            `;
            
            updateStepStatus('step3', 'completed');
            checkProcessButton();
        } else {
            alert('Error uploading video: ' + data.error);
        }
    } catch (error) {
        console.error('Upload error:', error);
        alert('Error uploading video');
    }
}

// Step Status
function updateStepStatus(stepId, status) {
    const statusElement = document.getElementById(`${stepId}-status`);
    if (status === 'completed') {
        statusElement.textContent = '✓ Completed';
        statusElement.style.background = 'rgba(16, 185, 129, 0.3)';
    } else {
        statusElement.textContent = '';
        statusElement.style.background = 'rgba(255, 255, 255, 0.2)';
    }
}

// Check if ready to process
function checkProcessButton() {
    const hasReferenceAudio = uploadedReferenceAudio !== null;
    const hasText = textInput.value.trim().length > 0;
    const hasVideo = uploadedVideo !== null;
    
    processBtn.disabled = !(hasReferenceAudio && hasText && hasVideo);
    
    if (hasText) {
        updateStepStatus('step2', 'completed');
    } else {
        updateStepStatus('step2', '');
    }
}

// Processing
async function startProcessing() {
    const data = {
        text: textInput.value.trim(),
        referenceAudio: uploadedReferenceAudio,
        video: uploadedVideo,
        language: language.value,
        replaceAudio: replaceAudio.checked,
        audioStartTime: parseFloat(audioStartTime.value)
    };
    
    try {
        const response = await fetch('/api/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (result.success) {
            currentJobId = result.jobId;
            progressCard.style.display = 'block';
            processBtn.disabled = true;
            
            // Poll for status
            pollStatus();
        } else {
            alert('Error starting process: ' + result.error);
        }
    } catch (error) {
        console.error('Process error:', error);
        alert('Error starting process');
    }
}

async function pollStatus() {
    if (!currentJobId) return;
    
    try {
        const response = await fetch(`/api/status/${currentJobId}`);
        const status = await response.json();
        
        // Update progress
        progressFill.style.width = `${status.progress}%`;
        progressPercentage.textContent = `${status.progress}%`;
        progressMessage.textContent = status.message;
        
        if (status.status === 'completed') {
            // Show result
            progressCard.style.display = 'none';
            resultCard.style.display = 'block';
            downloadUrl = status.downloadUrl;
        } else if (status.status === 'error') {
            alert('Error: ' + status.message);
            progressCard.style.display = 'none';
            processBtn.disabled = false;
        } else {
            // Continue polling
            setTimeout(pollStatus, 1000);
        }
    } catch (error) {
        console.error('Status poll error:', error);
        setTimeout(pollStatus, 2000);
    }
}

// Download
function downloadVideo() {
    if (downloadUrl) {
        window.location.href = downloadUrl;
    }
}

// Reset
function resetAll() {
    location.reload();
}
