import asyncio

import edge_tts
import gradio as gr

from .base import GradioPageBase


class TTS(GradioPageBase):
    voice_list = [
        "zh-CN-XiaoxiaoNeural",
        "zh-CN-XiaoyiNeural",
        "zh-CN-YunjianNeural",
        "zh-CN-YunxiNeural",
        "zh-CN-YunxiaNeural",
        "zh-CN-YunyangNeural",
        "zh-CN-liaoning-XiaobeiNeural",
        "zh-CN-shaanxi-XiaoniNeural",
        "zh-HK-HiuGaaiNeural",
        "zh-HK-HiuMaanNeural",
        "zh-HK-WanLungNeural",
        "zh-TW-HsiaoChenNeural",
        "zh-TW-HsiaoYuNeural",
        "zh-TW-YunJheNeural",
    ]
    default_voice = "zh-CN-XiaoxiaoNeural"

    def get_page_name(self) -> str:
        return "TTS配音"

    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        ocr_page = gr.Blocks()
        with ocr_page:
            select_voice = gr.Dropdown(
                choices=self.voice_list,
                value=self.default_voice,
                label="选择声音",
            )
            with gr.Row():
                input_text = gr.TextArea(label="配音文本")
                output_audio = gr.Audio(label="配音结果")
            submit_button = gr.Button("提交")
            submit_button.click(
                fn=self._tts,
                inputs=[select_voice, input_text],
                outputs=output_audio,
            )
        return ocr_page

    def _tts(self, select_voice, input_text):
        return asyncio.run(self.__generate_tts(select_voice, input_text))

    async def __generate_tts(self, voice, text):
        communicate = edge_tts.Communicate(text, voice)
        tts_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                tts_data += chunk["data"]
        return tts_data
