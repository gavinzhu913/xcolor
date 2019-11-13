import logging
import xcolor

if __name__ == "__main__":
    # 测试颜色
    xcolor.test_color()
    # 测试内置颜色对象
    xcolor.test_style()
    # 蓝色字体
    # print方法与内建print方法参数相同
    xcolor.blue1.print("hello world!")
    # 创建一个黄色字体,带下划线的颜色对象
    color = xcolor.Color("Yellow2", "Underline")
    color.print("hello", " world!")
    # 重设风格为粗体,字体色红色
    color.foreground = "Red"
    color.style = "Bold"
    color.print("Hi")


    # 用Color对象作为装饰器,改变被装饰函数内的标准输出
    @xcolor.yellow2
    def test():
        print("*"*20)

    test()

    logger = logging.getLogger("test")
    # setenv与clear成对使用,区间的标准输出风格被改变
    # 以绿色打印warning,红色打印error
    xcolor.green2.setenv()
    logger.warning("warning")
    xcolor.clear()
    xcolor.red1.setenv()
    logger.error("error")
    xcolor.clear()

