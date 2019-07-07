## xcolor

支持UNIX及类UNIX操作系统
支持Python版本为Python3.0+

### 颜色值:

------------


每种颜色有两种相近的颜色,以A和B区分.
没有以A或B结尾的颜色,如Red,则默认取其中的一种
"Black","Red","Green","Yellow","Blue","Purlple","Cyan","White"
"BlackA","RedA","GreenA","YellowA","BlueA","PurpleA","CyanA","WhiteA"
"BlackB","RedB","GreenB","YellowB","BlueB","PurpleB","CyanB","WhiteB"

当前终端前景色,背景色,默认风格均为"Default"



### 字体风格:

------------


"Bold":高亮加粗
"Italic":斜体
"Underline":下划线
"Flash":闪烁
"Throughline":删除线


### 内置对象:
------------
常规颜色风格
BLACK,RED,GREEN,YELLOW,BLUE,PURPLE,CYAN,WHITE
斜体风格
IBLACK,IRED,IGREEN,IYELLOW,IBLUE,IPURPLE,ICYAN,IWHITE
下划线风格
UBLACK,URED,UGREEN,UYELLOW,UBLUE,UPURPLE,UCYAN,UWHITE
删除线风格
TBLACK,TRED,TGREEN,TYELLOW,TBLUE,TPURPLE,TCYAN,TWHITE

eg.
------------

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

	# color装饰器
	# 接受一个Color对象,改变被装饰函数内的标准输出
	@color(TBLUE)
	def test():
		print("test")
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
