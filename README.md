## xcolor

支持UNIX及类UNIX操作系统
支持Python版本为Python3.0+

## 颜色值:



每种颜色有两种相近的颜色,以A和B区分.
没有以A或B结尾的颜色,如Red,则默认取其中的一种
"Black","Red","Green","Yellow","Blue","Magenta","Cyan","White"
"BlackA","RedA","GreenA","YellowA","BlueA","MagentaA","CyanA","WhiteA"
"BlackB","RedB","GreenB","YellowB","BlueB","MagentaB","CyanB","WhiteB"

当前终端前景色,背景色,默认风格均为"Default"



## 字体风格:



"Bold":高亮加粗  
"Italic":斜体  
"Underline":下划线  
"Flash":闪烁  
"Throughline":删除线  



## 内置对象:

字体风格需要终端支持  

常规颜色风格  
BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE  
BLACKA,REDA,GREENA,YELLOWA,BLUEA,MAGENTAA,CYANA,WHITEA  
BLACKB,REDB,GREENB,YELLOWB,BLUEB,MAGENTAB,CYANB,WHITEB  
斜体风格  
IBLACK,IRED,IGREEN,IYELLOW,IBLUE,IMAGENTA,ICYAN,IWHITE  
IBLACKA,IREDA,IGREENA,IYELLOWA,IBLUEA,IMAGENTAA,ICYANA,IWHITEA  
IBLACKB,IREDB,IGREENB,IYELLOWB,IBLUEB,IMAGENTAB,ICYANB,IWHITEB  
下划线风格  
UBLACK,URED,UGREEN,UYELLOW,UBLUE,UMAGENTA,UCYAN,UWHITE  
UBLACKA,UREDA,UGREENA,UYELLOWA,UBLUEA,UMAGENTAA,UCYANA,UWHITEA  
UBLACKB,UREDB,UGREENB,UYELLOWB,UBLUEB,UMAGENTAB,UCYANB,UWHITEB  
删除线风格  
TBLACK,TRED,TGREEN,TYELLOW,TBLUE,TMAGENTA,TCYAN,TWHITE  
TBLACKA,TREDA,TGREENA,TYELLOWA,TBLUEA,TMAGENTAA,TCYANA,TWHITEA  
TBLACKB,TREDB,TGREENB,TYELLOWB,TBLUEB,TMAGENTAB,TCYANB,TWHITEB  
闪烁风格  
FBLACK,FRED,FGREEN,FYELLOW,FBLUE,FMAGENTA,FCYAN,FWHITE  
FBLACKA,FREDA,FGREENA,FYELLOWA,FBLUEA,FMAGENTAA,FCYANA,FWHITEA  
FBLACKB,FREDB,FGREENB,FYELLOWB,FBLUEB,FMAGENTAB,FCYANB,FWHITEB  
粗体风格  
BBLACK,BRED,BGREEN,BYELLOW,BBLUE,BMAGENTA,BCYAN,BWHITE  


## eg.

    import logging
    from xcolor import *
	# 测试颜色
    test_color()
    # 测试内置颜色对象
    test_style()
    # 蓝色字体
    # print方法与内建print方法参数相同
    BLUE.print("hello world!")
    # 创建一个黄色字体,带下划线的颜色对象
    color = Color("YellowB", "Underline")
    color.print("hello", " world!")
    # 重设风格为粗体,字体色红色
    color.foreground = "Red"
    color.style = "Bold"
    color.print("Hi")


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
