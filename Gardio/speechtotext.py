import gradio as gr
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import soundfile as sf

# Load model
model_name = "facebook/wav2vec2-base-960h"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

def speech_to_text(audio_file):
    if audio_file is None:
        return "No audio provided."

    # Read audio
    speech, sr = sf.read(audio_file)

    # Convert stereo to mono if needed
    if len(speech.shape) > 1:
        speech = speech.mean(axis=1)

    # Tokenize and predict
    inputs = processor(speech, sampling_rate=sr, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    return transcription

# Gradio Interface
iface = gr.Interface(
    fn=speech_to_text,
    inputs=gr.Audio(type="filepath"),  # no 'source' argument needed
    outputs="text",
    title="Speech-to-Text with Wav2Vec2",
    description="Upload a voice file or record directly in the browser."
)

iface.launch()
