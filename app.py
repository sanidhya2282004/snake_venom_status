import gradio as gr
from model import predict_snake

iface = gr.Interface(
    fn=predict_snake,
    inputs=gr.Image(type="filepath", label="🖼️ Upload Snake Image"),
    outputs=gr.Text(label="☠️ Venomous Status"),
    title="Snake Venom Detector",
    description="Upload an image to determine if the snake is venomous or non-venomous."
)

iface.launch()
