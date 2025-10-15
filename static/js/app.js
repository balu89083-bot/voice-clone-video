// Voice Cloning Web App JavaScript - Updated with Quality Presets

let mediaRecorder;
let audioChunks = [];
let recordingStartTime;
let recordingInterval;
let audioBlob = null;
let uploadedReferenceAudio = null;
let uploadedVideo = null;
let persistedReferenceAudio = null; // Persist reference audio

// Quality Presets
const qualityPresets = {
    realistic: {
        name: 'Most Realistic',
        description: 'Balanced, natural sounding voice',
        temperature: 0.65,
        repetitionPenalty: 10.0,
        lengthPenalty: 1.0
    },
    professional: {
        name: 'Professional/News',
        description: 'Consistent, clear, professional tone',
        temperature: 0.4,
        repetitionPenalty: 15.0,
        lengthPenalty: 1.0
    },
    emotional: {
        name: 'Emotional/Expressive',
        description: 'Varied, expressive, emotional delivery',
        temperature: 0.8,
        repetitionPenalty: 7.0,
        lengthPenalty: 1.0
    },
    educational: {
        name: 'Educational/Clear',
        description: 'Clear, slower pace, easy to understand',
        temperature: 0.5,
        repetitionPenalty: 12.0,
        lengthPenalty: 1.0
    },
    storytelling: {
        name: 'Storytelling/Narrative',
        description: 'Engaging, narrative style with good pacing',
        temperature: 0.7,
        repetitionPenalty: 8.0,
        lengthPenalty: 1.0
    },
    conversational: {
        name: 'Conversational/Casual',
        description: 'Natural, casual conversation style',
        temperature: 0.75,
        repetitionPenalty: 6.0,
        lengthPenalty: 1.0
    },
    dramatic: {
        name: 'Dramatic/Theatrical',
        description: 'Dramatic, theatrical performance style',
        temperature: 0.85,
        repetitionPenalty: 5.0,
        lengthPenalty: 1.0
    },
    calm: {
        name: 'Calm/Soothing',
        description: 'Calm, soothing, relaxing tone',
        temperature: 0.45,
        repetitionPenalty: 10.0,
        lengthPenalty: 1.0
    }
};

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
const qualityPreset = document.getElementById('qualityPreset');
const presetDescription = document.getElementById('presetDescription');

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
const resultVideoPlayer = document.getElementById('resultVideoPlayer');
const playBtn = document.getElementById('playBtn');
const downloadBtn = document.getElementById('downloadBtn');
const newProcessBtn = document.getElementById('newProcessBtn');
const clearAllBtn = document.getElementById('clearAllBtn');

const enableNoiseReduction = document.getElementById('enableNoiseReduction');
const enableVoiceEnhancement = document.getElementById('enableVoiceEnhancement');
const enableAudioCleaning = document.getElementById('enableAudioCleaning');

const voiceToTextBtn = document.getElementById('voiceToTextBtn');
const stopVoiceToTextBtn = document.getElementById('stopVoiceToTextBtn');
const voiceToTextStatus = document.getElementById('voiceToTextStatus');
const clearTextBtn = document.getElementById('clearTextBtn');

let currentJobId = null;
let downloadUrl = null;
let recognition = null;
let isRecognizing = false;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    loadPersistedData();
    updateProcessButton();
});

function setupEventListeners() {
    // Recording
    recordBtn.addEventListener('click', startRecording);
    stopBtn.addEventListener('click', stopRecording);
    reRecordBtn.addEventListener('click', reRecord);
    
    // File uploads
    referenceAudioFile.addEventListener('change', handleReferenceAudioUpload);
    videoFile.addEventListener('change', handleVideoUpload);
    
    // Update character count
    textInput.addEventListener('input', () => {
        const length = textInput.value.length;
        charCount.textContent = length;
        
        // Show helpful hints based on text length
        const textLengthHint = document.getElementById('textLengthHint');
        if (length === 0) {
            textLengthHint.textContent = '';
            textLengthHint.style.color = '';
        } else if (length < 250) {
            textLengthHint.textContent = '✅ Good length';
            textLengthHint.style.color = '#10b981';
        } else if (length < 500) {
            textLengthHint.textContent = '⚠️ Long text - will use automatic sentence splitting';
            textLengthHint.style.color = '#f59e0b';
        } else {
            textLengthHint.textContent = '⚠️ Very long text - may take longer to process';
            textLengthHint.style.color = '#ef4444';
        }
        
        // Save to localStorage
        localStorage.setItem('savedText', textInput.value);
        
        updateProcessButton();
    });
    
    // Language selection
    language.addEventListener('change', () => {
        // Save language to localStorage
        localStorage.setItem('selectedLanguage', language.value);
    });
    
    // Quality preset
    qualityPreset.addEventListener('change', () => {
        updatePresetDescription();
        // Save preset to localStorage
        localStorage.setItem('qualityPreset', qualityPreset.value);
    });
    
    // Replace audio checkbox
    replaceAudio.addEventListener('change', () => {
        // Save to localStorage
        localStorage.setItem('replaceAudio', replaceAudio.checked);
    });
    
    // Audio start time
    audioStartTime.addEventListener('input', () => {
        // Save to localStorage
        localStorage.setItem('audioStartTime', audioStartTime.value);
    });
    
    // Enhancement options
    enableNoiseReduction.addEventListener('change', () => {
        localStorage.setItem('enableNoiseReduction', enableNoiseReduction.checked);
    });
    
    enableVoiceEnhancement.addEventListener('change', () => {
        localStorage.setItem('enableVoiceEnhancement', enableVoiceEnhancement.checked);
    });
    
    enableAudioCleaning.addEventListener('change', () => {
        localStorage.setItem('enableAudioCleaning', enableAudioCleaning.checked);
    });
    
    // Voice to Text
    voiceToTextBtn.addEventListener('click', startVoiceToText);
    stopVoiceToTextBtn.addEventListener('click', stopVoiceToText);
    clearTextBtn.addEventListener('click', clearText);
    
    // Process
    processBtn.addEventListener('click', processVideo);
    
    // Result actions
    playBtn.addEventListener('click', playResultVideo);
    downloadBtn.addEventListener('click', downloadVideo);
    newProcessBtn.addEventListener('click', resetForNewProcess);
    
    // Clear all button
    clearAllBtn.addEventListener('click', clearAllSettings);
}

function updatePresetDescription() {
    const preset = qualityPresets[qualityPreset.value];
    if (preset) {
        presetDescription.textContent = preset.description;
    }
}

// Load persisted data from localStorage
function loadPersistedData() {
    // Load persisted reference audio
    const savedAudio = localStorage.getItem('persistedReferenceAudio');
    if (savedAudio) {
        persistedReferenceAudio = savedAudio;
        uploadedReferenceAudio = savedAudio;
        
        // Show in UI
        audioFileName.textContent = 'Previously uploaded audio';
        audioPreview.src = `/uploads/${savedAudio}`;
        audioPlayer.style.display = 'flex';
        document.getElementById('step1-status').innerHTML = '<i class="fas fa-check-circle"></i>';
        
        console.log('✅ Loaded persisted reference audio:', savedAudio);
    }
    
    // Load quality preset
    const savedPreset = localStorage.getItem('qualityPreset');
    if (savedPreset && qualityPresets[savedPreset]) {
        qualityPreset.value = savedPreset;
        updatePresetDescription();
    }
    
    // Load language
    const savedLanguage = localStorage.getItem('selectedLanguage');
    if (savedLanguage) {
        language.value = savedLanguage;
        console.log('✅ Loaded language:', savedLanguage);
    }
    
    // Load text
    const savedText = localStorage.getItem('savedText');
    if (savedText) {
        textInput.value = savedText;
        charCount.textContent = savedText.length;
        document.getElementById('step2-status').innerHTML = '<i class="fas fa-check-circle"></i>';
        console.log('✅ Loaded text:', savedText.substring(0, 50) + '...');
    }
    
    // Load replace audio checkbox
    const savedReplaceAudio = localStorage.getItem('replaceAudio');
    if (savedReplaceAudio !== null) {
        replaceAudio.checked = savedReplaceAudio === 'true';
    }
    
    // Load audio start time
    const savedStartTime = localStorage.getItem('audioStartTime');
    if (savedStartTime !== null) {
        audioStartTime.value = savedStartTime;
    }
    
    // Load enhancement options
    const savedNoiseReduction = localStorage.getItem('enableNoiseReduction');
    if (savedNoiseReduction !== null) {
        enableNoiseReduction.checked = savedNoiseReduction === 'true';
    }
    
    const savedVoiceEnhancement = localStorage.getItem('enableVoiceEnhancement');
    if (savedVoiceEnhancement !== null) {
        enableVoiceEnhancement.checked = savedVoiceEnhancement === 'true';
    }
    
    // Load audio cleaning option (default: true)
    const savedAudioCleaning = localStorage.getItem('enableAudioCleaning');
    if (savedAudioCleaning !== null) {
        enableAudioCleaning.checked = savedAudioCleaning === 'true';
    } else {
        // Default to true (enabled)
        enableAudioCleaning.checked = true;
        localStorage.setItem('enableAudioCleaning', 'true');
    }
    
    console.log('✅ All settings loaded from localStorage');
}

// Save reference audio to localStorage
function saveReferenceAudio(filename) {
    localStorage.setItem('persistedReferenceAudio', filename);
    console.log('💾 Saved reference audio to localStorage:', filename);
}

// Clear persisted reference audio
function clearPersistedAudio() {
    localStorage.removeItem('persistedReferenceAudio');
    persistedReferenceAudio = null;
    uploadedReferenceAudio = null;
    console.log('🗑️ Cleared persisted reference audio');
}

// Auto Punctuation Function
function addAutoPunctuation(text) {
    if (!text || text.trim().length === 0) return text;
    
    // Trim whitespace
    text = text.trim();
    
    // Detect language (Hindi/Urdu vs English)
    const hindiPattern = /[\u0900-\u097F\u0600-\u06FF]/;
    const isHindiUrdu = hindiPattern.test(text);
    
    // Capitalize first letter (for English/Roman script)
    if (!isHindiUrdu) {
        text = text.charAt(0).toUpperCase() + text.slice(1);
    }
    
    // Add commas after common pause words/phrases
    const pauseWords = [
        // English
        'however', 'therefore', 'moreover', 'furthermore', 'meanwhile', 'nevertheless',
        'additionally', 'consequently', 'otherwise', 'instead', 'besides', 'indeed',
        'actually', 'basically', 'essentially', 'generally', 'naturally', 'obviously',
        'personally', 'frankly', 'honestly', 'literally', 'seriously', 'technically',
        'well', 'so', 'now', 'then', 'also', 'too', 'again', 'still', 'yet',
        'first', 'second', 'third', 'finally', 'lastly', 'next',
        'for example', 'for instance', 'in fact', 'in addition', 'in conclusion',
        'on the other hand', 'as a result', 'in other words',
        // Hindi/Urdu
        'लेकिन', 'परंतु', 'और', 'फिर', 'तब', 'जब', 'क्योंकि', 'इसलिए',
        'वैसे', 'मतलब', 'यानी', 'तो', 'अब', 'पहले', 'दूसरे', 'अंत में',
        'lekin', 'par', 'aur', 'phir', 'tab', 'jab', 'kyunki', 'isliye',
        'waise', 'matlab', 'yaani', 'toh', 'pehle', 'dusre', 'akhir mein'
    ];
    
    // Add comma after pause words if not already present
    pauseWords.forEach(word => {
        const regex = new RegExp(`\\b${word}\\b(?![,।])`, 'gi');
        text = text.replace(regex, match => match + ',');
    });
    
    // Add commas at natural break points (key phrases)
    const breakPhrases = [
        // Hindi phrases that need comma
        'के साथ', 'के बाद', 'के पहले', 'की तरह', 'के लिए',
        'इसी के साथ', 'इसके अलावा', 'इसके बावजूद',
        'ने कहा कि', 'बताया कि', 'कहा है कि'
    ];
    
    breakPhrases.forEach(phrase => {
        const regex = new RegExp(`(${phrase})(?![,।])`, 'gi');
        text = text.replace(regex, '$1,');
    });
    
    // Add comma before conjunctions if sentence is long (>15 words)
    const conjunctions = ['and', 'but', 'or', 'so', 'yet', 'aur', 'और', 'par', 'परंतु', 'ya', 'या', 'lekin', 'लेकिन'];
    if (text.split(' ').length > 15) {
        conjunctions.forEach(conj => {
            const regex = new RegExp(`\\s(${conj})\\s(?![,।])`, 'gi');
            text = text.replace(regex, (match, p1) => `, ${p1} `);
        });
    }
    
    // Split long sentences with Hindi full stop (।) or period
    // Detect sentence boundaries (after 20-30 words)
    const words = text.split(' ');
    if (words.length > 25) {
        // Find natural break points (after verbs like है, था, हैं, etc.)
        const sentenceEnders = ['है', 'हैं', 'था', 'थे', 'थी', 'हो', 'होगा', 'होगी', 'होंगे'];
        
        let processedText = '';
        let wordCount = 0;
        
        for (let i = 0; i < words.length; i++) {
            processedText += words[i];
            wordCount++;
            
            // Check if this word is a sentence ender and we've crossed 15 words
            const isEnder = sentenceEnders.some(ender => words[i].includes(ender));
            
            if (isEnder && wordCount > 15 && i < words.length - 3) {
                // Add Hindi full stop if Hindi/Urdu, otherwise period
                if (isHindiUrdu) {
                    processedText += '।';
                } else {
                    processedText += '.';
                }
                wordCount = 0;
            }
            
            // Add space if not last word
            if (i < words.length - 1) {
                processedText += ' ';
            }
        }
        
        text = processedText;
    }
    
    // Add ending punctuation if not present
    const lastChar = text.charAt(text.length - 1);
    if (!['.', '?', '!', ',', '।'].includes(lastChar)) {
        // Check if it's a question
        const questionWords = ['what', 'when', 'where', 'who', 'why', 'how', 'which', 'whose', 'whom',
                               'kya', 'kab', 'kahan', 'kaun', 'kaise', 'kyun', 'kis',
                               'क्या', 'कब', 'कहाँ', 'कौन', 'कैसे', 'क्यों'];
        const firstWord = text.split(' ')[0].toLowerCase();
        
        if (questionWords.includes(firstWord)) {
            text += '?';
        } else {
            // Use Hindi full stop for Hindi/Urdu, period for English
            text += isHindiUrdu ? '।' : '.';
        }
    }
    
    // Fix spacing around punctuation
    text = text.replace(/\s+([.,!?।])/g, '$1'); // Remove space before punctuation
    text = text.replace(/([.,!?।])([^\s])/g, '$1 $2'); // Add space after punctuation
    text = text.replace(/\s+/g, ' '); // Remove multiple spaces
    
    // Capitalize after sentence-ending punctuation (for English)
    if (!isHindiUrdu) {
        text = text.replace(/([.!?।])\s+([a-z])/g, (match, p1, p2) => p1 + ' ' + p2.toUpperCase());
    }
    
    return text;
}

// Voice to Text Functions
function startVoiceToText() {
    // Check browser support
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert('❌ Voice to Text not supported in your browser. Please use Chrome, Edge, or Safari.');
        return;
    }
    
    try {
        // Initialize speech recognition
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SpeechRecognition();
        
        // Configure recognition
        recognition.continuous = true;  // Keep listening
        recognition.interimResults = true;  // Show interim results
        recognition.lang = language.value || 'en-US';  // Use selected language
        
        // Map language codes to speech recognition codes
        const langMap = {
            'en': 'en-US',
            'hi': 'hi-IN',
            'ur': 'ur-PK',
            'es': 'es-ES',
            'fr': 'fr-FR',
            'de': 'de-DE',
            'it': 'it-IT',
            'pt': 'pt-PT',
            'pl': 'pl-PL',
            'tr': 'tr-TR',
            'ru': 'ru-RU',
            'nl': 'nl-NL',
            'cs': 'cs-CZ',
            'ar': 'ar-SA',
            'zh-cn': 'zh-CN',
            'ja': 'ja-JP',
            'hu': 'hu-HU',
            'ko': 'ko-KR'
        };
        
        recognition.lang = langMap[language.value] || 'en-US';
        
        let finalTranscript = textInput.value;  // Keep existing text
        
        recognition.onstart = () => {
            isRecognizing = true;
            voiceToTextBtn.style.display = 'none';
            stopVoiceToTextBtn.style.display = 'inline-flex';
            voiceToTextStatus.textContent = '🎤 Listening... Speak now!';
            voiceToTextStatus.style.color = '#ef4444';
            textInput.style.borderColor = '#ef4444';
        };
        
        recognition.onresult = (event) => {
            let interimTranscript = '';
            
            for (let i = event.resultIndex; i < event.results.length; i++) {
                const transcript = event.results[i][0].transcript;
                
                if (event.results[i].isFinal) {
                    // Add automatic punctuation to final transcript
                    const punctuatedText = addAutoPunctuation(transcript);
                    finalTranscript += (finalTranscript ? ' ' : '') + punctuatedText;
                } else {
                    interimTranscript += transcript;
                }
            }
            
            // Update textarea with final + interim
            textInput.value = finalTranscript + (interimTranscript ? ' ' + interimTranscript : '');
            charCount.textContent = textInput.value.length;
            
            // Save to localStorage
            localStorage.setItem('savedText', finalTranscript);
            
            updateProcessButton();
        };
        
        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            
            let errorMessage = 'Error: ';
            switch(event.error) {
                case 'no-speech':
                    errorMessage += 'No speech detected. Please try again.';
                    break;
                case 'audio-capture':
                    errorMessage += 'Microphone not found or not working.';
                    break;
                case 'not-allowed':
                    errorMessage += 'Microphone permission denied.';
                    break;
                case 'network':
                    errorMessage += 'Network error. Check internet connection.';
                    break;
                default:
                    errorMessage += event.error;
            }
            
            voiceToTextStatus.textContent = errorMessage;
            voiceToTextStatus.style.color = '#ef4444';
            
            stopVoiceToText();
        };
        
        recognition.onend = () => {
            if (isRecognizing) {
                // Restart if still supposed to be recognizing
                try {
                    recognition.start();
                } catch (e) {
                    stopVoiceToText();
                }
            }
        };
        
        // Start recognition
        recognition.start();
        
    } catch (error) {
        alert('Error starting voice recognition: ' + error.message);
        console.error('Voice recognition error:', error);
    }
}

function stopVoiceToText() {
    if (recognition) {
        isRecognizing = false;
        recognition.stop();
        recognition = null;
    }
    
    voiceToTextBtn.style.display = 'inline-flex';
    stopVoiceToTextBtn.style.display = 'none';
    voiceToTextStatus.textContent = '✅ Stopped listening';
    voiceToTextStatus.style.color = '#10b981';
    textInput.style.borderColor = '';
    
    // Clear status after 3 seconds
    setTimeout(() => {
        voiceToTextStatus.textContent = '';
    }, 3000);
}

function clearText() {
    if (textInput.value.trim().length > 0) {
        if (confirm('Are you sure you want to clear all text?')) {
            textInput.value = '';
            charCount.textContent = '0';
            
            // Clear from localStorage
            localStorage.removeItem('savedText');
            
            // Update status
            document.getElementById('step2-status').innerHTML = '';
            updateProcessButton();
            
            // Show feedback
            voiceToTextStatus.textContent = '✅ Text cleared';
            voiceToTextStatus.style.color = '#10b981';
            
            setTimeout(() => {
                voiceToTextStatus.textContent = '';
            }, 2000);
        }
    } else {
        // Already empty
        voiceToTextStatus.textContent = 'ℹ️ Text is already empty';
        voiceToTextStatus.style.color = '#6b7280';
        
        setTimeout(() => {
            voiceToTextStatus.textContent = '';
        }, 2000);
    }
}

// Clear all settings and data
function clearAllSettings() {
    if (confirm('Are you sure you want to clear all settings and data? This will reset everything including saved voice, text, and preferences.')) {
        // Clear localStorage
        localStorage.clear();
        
        // Reset all variables
        audioBlob = null;
        uploadedReferenceAudio = null;
        uploadedVideo = null;
        persistedReferenceAudio = null;
        currentJobId = null;
        downloadUrl = null;
        
        // Reset UI
        audioPlayer.style.display = 'none';
        audioFileName.textContent = '';
        audioPreview.src = '';
        
        textInput.value = '';
        charCount.textContent = '0';
        
        language.value = 'en';
        qualityPreset.value = 'realistic';
        updatePresetDescription();
        
        videoFileName.textContent = '';
        videoPreview.style.display = 'none';
        videoPlayer.src = '';
        
        replaceAudio.checked = true;
        audioStartTime.value = '0';
        
        resultCard.style.display = 'none';
        progressCard.style.display = 'none';
        
        document.getElementById('step1-status').innerHTML = '';
        document.getElementById('step2-status').innerHTML = '';
        document.getElementById('step3-status').innerHTML = '';
        
        updateProcessButton();
        
        alert('✅ All settings and data cleared successfully!');
        console.log('🗑️ All settings cleared');
    }
}

// Recording Functions
async function startRecording() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        
        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };
        
        mediaRecorder.onstop = () => {
            audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            const audioUrl = URL.createObjectURL(audioBlob);
            audioPreview.src = audioUrl;
            audioPlayer.style.display = 'flex';
            audioVisualizer.style.display = 'none';
            
            // Mark step as complete
            document.getElementById('step1-status').innerHTML = '<i class=\"fas fa-check-circle\"></i>';
            updateProcessButton();
        };
        
        mediaRecorder.start();
        recordingStartTime = Date.now();
        
        // Update UI
        recordBtn.disabled = true;
        stopBtn.disabled = false;
        audioVisualizer.style.display = 'block';
        
        // Start timer
        recordingInterval = setInterval(updateRecordingTimer, 100);
        
    } catch (error) {
        alert('Microphone access denied or not available. Please use "Upload Audio File" option.');
        console.error('Recording error:', error);
    }
}

function stopRecording() {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
        mediaRecorder.stream.getTracks().forEach(track => track.stop());
        
        clearInterval(recordingInterval);
        recordBtn.disabled = false;
        stopBtn.disabled = true;
    }
}

function reRecord() {
    audioPlayer.style.display = 'none';
    audioBlob = null;
    audioFileName.textContent = '';
    
    // Clear persisted audio
    clearPersistedAudio();
    
    document.getElementById('step1-status').innerHTML = '';
    updateProcessButton();
}

function updateRecordingTimer() {
    const elapsed = Date.now() - recordingStartTime;
    const seconds = Math.floor(elapsed / 1000);
    const milliseconds = Math.floor((elapsed % 1000) / 100);
    recordingTimer.textContent = `${String(seconds).padStart(2, '0')}:${milliseconds}`;
}

// File Upload Functions
async function handleReferenceAudioUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    audioFileName.textContent = file.name;
    
    // Upload immediately with enhancement options
    const formData = new FormData();
    formData.append('audio', file);
    formData.append('noiseReduction', enableNoiseReduction.checked);
    formData.append('voiceEnhancement', enableVoiceEnhancement.checked);
    
    try {
        const response = await fetch('/api/upload-reference-audio', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        if (result.success) {
            uploadedReferenceAudio = result.filename;
            persistedReferenceAudio = result.filename;
            
            // Save to localStorage for persistence
            saveReferenceAudio(result.filename);
            
            document.getElementById('step1-status').innerHTML = '<i class=\"fas fa-check-circle\"></i>';
            
            // Show preview
            audioPreview.src = `/uploads/${result.filename}`;
            audioPlayer.style.display = 'flex';
            
            updateProcessButton();
        } else {
            alert('Error uploading audio: ' + (result.error || 'Unknown error'));
        }
    } catch (error) {
        alert('Error uploading audio: ' + error.message);
        console.error('Upload error:', error);
    }
}

async function handleVideoUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    videoFileName.textContent = file.name;
    
    // Upload immediately
    const formData = new FormData();
    formData.append('video', file);
    
    try {
        const response = await fetch('/api/upload-video', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        if (result.success) {
            uploadedVideo = result.filename;
            document.getElementById('step3-status').innerHTML = '<i class=\"fas fa-check-circle\"></i>';
            
            // Show preview
            videoPlayer.src = `/uploads/${result.filename}`;
            videoPreview.style.display = 'block';
            videoInfo.textContent = `Video uploaded: ${file.name}`;
            
            updateProcessButton();
        } else {
            alert('Error uploading video: ' + (result.error || 'Unknown error'));
        }
    } catch (error) {
        alert('Error uploading video: ' + error.message);
        console.error('Upload error:', error);
    }
}

// Process Video
async function processVideo() {
    // Get reference audio (use persisted if available, otherwise current)
    let referenceAudio = persistedReferenceAudio || uploadedReferenceAudio;
    
    // If we have a new recording, upload it first
    if (audioBlob && !uploadedReferenceAudio) {
        const formData = new FormData();
        formData.append('audio', audioBlob, 'recording.webm');
        formData.append('noiseReduction', enableNoiseReduction.checked);
        formData.append('voiceEnhancement', enableVoiceEnhancement.checked);
        
        try {
            const response = await fetch('/api/upload-reference-audio', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            if (result.success) {
                referenceAudio = result.filename;
                persistedReferenceAudio = result.filename;
                
                // Save to localStorage for persistence
                saveReferenceAudio(result.filename);
            } else {
                alert('Error uploading recording: ' + (result.error || 'Unknown error'));
                return;
            }
        } catch (error) {
            alert('Error uploading recording: ' + error.message);
            return;
        }
    }
    
    // Get quality preset settings
    const preset = qualityPresets[qualityPreset.value];
    
    // Prepare request data
    const requestData = {
        text: textInput.value,
        referenceAudio: referenceAudio,
        video: uploadedVideo,
        language: language.value,
        replaceAudio: replaceAudio.checked,
        audioStartTime: parseFloat(audioStartTime.value) || 0,
        temperature: preset.temperature,
        repetitionPenalty: preset.repetitionPenalty,
        lengthPenalty: preset.lengthPenalty,
        enableTextSplitting: true,
        enableAudioCleaning: enableAudioCleaning.checked
    };
    
    try {
        // Start processing
        const response = await fetch('/api/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        });
        
        const result = await response.json();
        if (result.success) {
            currentJobId = result.jobId;
            
            // Show progress
            progressCard.style.display = 'block';
            processBtn.disabled = true;
            
            // Poll for status
            pollStatus();
        } else {
            alert('Error starting process: ' + (result.error || 'Unknown error'));
        }
    } catch (error) {
        alert('Error: ' + error.message);
        console.error('Process error:', error);
    }
}

// Poll Status
async function pollStatus() {
    if (!currentJobId) return;
    
    try {
        const response = await fetch(`/api/status/${currentJobId}`);
        const status = await response.json();
        
        // Update progress
        progressFill.style.width = status.progress + '%';
        progressPercentage.textContent = status.progress + '%';
        progressMessage.textContent = status.message;
        
        if (status.status === 'completed') {
            // Show result
            downloadUrl = status.downloadUrl;
            resultVideoPlayer.src = downloadUrl;
            resultCard.style.display = 'block';
            progressCard.style.display = 'none';
            processBtn.disabled = false;
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
        setTimeout(pollStatus, 1000);
    }
}

// Result Actions
function playResultVideo() {
    resultVideoPlayer.play();
}

function downloadVideo() {
    if (downloadUrl) {
        window.location.href = downloadUrl;
    }
}

function resetForNewProcess() {
    // Reset UI but keep ALL settings (audio, text, language, etc.)
    resultCard.style.display = 'none';
    progressCard.style.display = 'none';
    
    // Clear ONLY video (keep everything else)
    uploadedVideo = null;
    videoFileName.textContent = '';
    videoPreview.style.display = 'none';
    videoPlayer.src = '';
    document.getElementById('step3-status').innerHTML = '';
    
    // Keep reference audio, text, language, quality preset - ALL SETTINGS PERSIST!
    // User can reuse same settings for multiple videos
    
    currentJobId = null;
    downloadUrl = null;
    
    updateProcessButton();
}

// Update Process Button
function updateProcessButton() {
    const hasReferenceAudio = audioBlob || uploadedReferenceAudio || persistedReferenceAudio;
    const hasText = textInput.value.trim().length > 0;
    const hasVideo = uploadedVideo !== null;
    
    processBtn.disabled = !(hasReferenceAudio && hasText && hasVideo);
    
    // Update step 2 status
    if (hasText) {
        document.getElementById('step2-status').innerHTML = '<i class=\"fas fa-check-circle\"></i>';
    } else {
        document.getElementById('step2-status').innerHTML = '';
    }
}
