import gradio as gr
import requests
from fastapi import FastAPI

LOCAL_OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

# Updated function to accept both prompt and model_name
def generate_text(prompt: str, model_name: str):
    if not prompt:
        return "Please enter a prompt."

    try:
        data = {"model": model_name, "prompt": prompt, "stream": False}
        resp = requests.post(LOCAL_OLLAMA_ENDPOINT, json=data, timeout=30)
        resp.raise_for_status()
        return resp.json().get("response", "No response found from model.")
    except Exception as e:
        return f"Error: {str(e)}"

# Dropdown for model selection
model_dropdown = gr.Dropdown(
    choices=["qwen:0.5b"], 
    value="qwen:0.5b", 
    label="Select Model"
)

# Gradio interface
gui = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(lines=3, label="Your Prompt", placeholder="Write something..."), 
        model_dropdown
    ],
    outputs=gr.Textbox(label="Generated Text"),
    title="Local Ollama Assistant (qwen:0.5b)",
    description="This app talks to a local Ollama server (qwen:0.5b)."
)

# FastAPI app
app = FastAPI(title="Local Ollama Assistant")
app = gr.mount_gradio_app(app, gui, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)