import gradio as gr

from app.gradio_pages.ocr import OCR
from app.gradio_pages.tts import TTS

gradio_page_list = [
    OCR(),
    TTS(),
]

tab_interface_list = []
tab_name_list = []
for gradio_page in gradio_page_list:
    tab_interface_list.append(gradio_page.render())
    tab_name_list.append(gradio_page.get_page_name())

tabbed_demo = gr.TabbedInterface(
    interface_list=tab_interface_list, tab_names=tab_name_list, title="gradio AI 学习"
)

if __name__ == "__main__":
    tabbed_demo.launch()
