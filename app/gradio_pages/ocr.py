from enum import Enum

import gradio as gr
import pytesseract

from .base import GradioPageBase


class OCR_Type(Enum):
    Tesseract = "tesseract"


class OCR(GradioPageBase):
    # OCR识别库
    ocr_type_list = [
        OCR_Type.Tesseract.value,
    ]
    ocr_default = OCR_Type.Tesseract.value

    def get_page_name(self) -> str:
        return "OCR识别"

    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        ocr_page = gr.Blocks()
        with ocr_page:
            ocr_type = gr.Dropdown(
                choices=self.ocr_type_list,
                value=self.ocr_default,
                label="选择ocr识别库",
            )
            with gr.Row():
                input_image = gr.Image(label="上传图片")
                output_text = gr.TextArea(label="识别结果")
            submit_button = gr.Button("提交")
            submit_button.click(
                fn=self._ocr,
                inputs=[ocr_type, input_image],
                outputs=output_text,
            )
        return ocr_page
        # return gr.Interface(self._ocr, "image", "textarea")

    def _ocr(self, ocr_type, image):
        match ocr_type:
            case OCR_Type.Tesseract.value:
                return self._tesseract_ocr(image)
            case _:
                gr.Error(f"ocr识别类型不支持: {ocr_type}")

    def _tesseract_ocr(self, image):
        """
        使用 tesseract 进行ocr识别

        sudo apt install tesseract-ocr
        sudo apt install libtesseract-dev

        安装中文库 chi_sim
        sudo apt-get install tesseract-ocr-chi-sim
        """
        return pytesseract.image_to_string(image, lang="chi_sim")
