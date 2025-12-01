import gradio as gr
from transformers import pipeline

# Load a pre-trained image classification model
classifier = pipeline("image-classification")

def classify_image(img):
    results = classifier(img)
    # return only the top result
    top_result = results[0]
    label = top_result["label"]
    score = round(top_result["score"], 3)
    return f"Prediction: {label} (Confidence: {score})"

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Classification",
    description="Upload an image and the model will guess what's inside."
)

if __name__ == "__main__":
    demo.launch(share=True)
