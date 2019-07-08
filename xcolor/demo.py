import logging
from xcolor import *

if __name__ == "__main__":
    # 测试颜色
    test_color()
    # 测试内置颜色对象
    test_style()
    # 蓝色字体
    # print方法与内建print方法参数相同
    BLUE.print("hello world!")
    # 创建一个黄色字体,黑色背景色,带下划线的颜色对象
    color_obj = Color("Yellow", "Black", "Underline")
    color_obj.print("hello", " world!")
    # 重设风格为粗体,字体色紫色,背景颜色为当前终端默认颜色
    color_obj.foreground = "Purple"
    color_obj.background = "default"
    color_obj.style = "Bold"
    color_obj.print("Hi")


    # 用Color对象作为装饰器,改变被装饰函数内的标准输出
    @YELLOW
    def test():
        print("*"*20)

    test()

    logger = logging.getLogger("test")
    # setenv与clear成对使用,区间的标准输出风格被改变
    # 以绿色打印warning,红色打印error
    GREEN.setenv()
    logger.warning("warning")
    GREEN.clear()
    RED.setenv()
    logger.error("error")
    RED.clear()

