import inspect
import os
from abc import ABC, abstractmethod

import gradio as gr


class GradioPageBase(ABC):
    def get_page_name(self) -> str:
        """
        获取当前页面的名称, 默认使用文件名, 以驼峰命名法返回, 如: hello_world -> HelloWorld
        可以在子类中重写此方法, 自定义返回的名称
        :return:
        """
        # 获取文件的路径名 ps: __file__ 获取的不准, 返回的始终是父类的路径, 不会根据子类自动判断
        class_file_path = inspect.getfile(self.__class__)
        class_file_name_with_ext = os.path.basename(class_file_path)
        class_file_name, _ = os.path.splitext(class_file_name_with_ext)
        return " ".join([x.title() for x in class_file_name.split("_")])

    @abstractmethod
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        pass
