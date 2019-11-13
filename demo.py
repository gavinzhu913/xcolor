if __name__ == "__main__":
    import logging
    import xcolor

    # 测试颜色
    xcolor.test_color()
    # 测试内置颜色对象
    xcolor.test_style()
    # 蓝色字体
    # print方法与内建print方法参数相同
    xcolor.blue1.print("hello world!")


    # 用Color对象作为装饰器,改变被装饰函数内的标准输出
    @xcolor.yellow1
    def test():
        print("*" * 60)


    test()

    std_handler = logging.StreamHandler()
    std_handler.setLevel(logging.DEBUG)
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    logger.error = xcolor.red1(logger.error)
    logger.warning = xcolor.bred(logger.warning)
    logger.info = xcolor.green2(logger.info)
    logger.debug = xcolor.iblue2(logger.debug)
    logger.error("error")
    logger.warning("warn")
    logger.info("info")
    logger.debug("debug")
    # 设置终端颜色
    xcolor.byellow.setenv()
    print("abc")
    # 清除终端颜色
    xcolor.clear()
    print("efg")

