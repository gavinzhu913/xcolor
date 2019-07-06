# xcolor

颜色值:

每种颜色有两种相近的颜色,以A和B区分.

没有以A或B结尾的颜色,如Red,则默认取其中的一种

"Black","Red","Green","Yellow","Blue","Purlple","Cyan","White"

"BlackA","RedA","GreenA","YellowA","BlueA","PurpleA","CyanA","WhiteA"

"BlackB","RedB","GreenB","YellowB","BlueB","PurpleB","CyanB","WhiteB"



当前终端前景色,背景色,默认风格均为"Default"



字体风格:

"Bold":高度加粗

"Italic":斜体

"Underline":下划线

"Flash":闪烁

"Throughline":删除线




内置对象:

常规颜色风格

BLACK,RED,GREEN,YELLOW,BLUE,PURPLE,CYAN,WHITE

斜体风格

IBLACK,IRED,IGREEN,IYELLOW,IBLUE,IPURPLE,ICYAN,IWHITE

下划线风格

UBLACK,URED,UGREEN,UYELLOW,UBLUE,UPURPLE,UCYAN,UWHITE

删除线风格

TBLACK,TRED,TGREEN,TYELLOW,TBLUE,TPURPLE,TCYAN,TWHITE




eg.

from xcolor import *

#查看所有颜色

test_color()

#查看内置对象风格

test_style()

#打印蓝色字体,print方法参数与内置print函数相同

BLUE.print("hello world!",[1,2,3])

#打印带下划线的黄色字体

UYELLOW.print("Hi")

#创建一个字体白色,背景色蓝色的Color对象,高亮显示

color = Color("White","Blue","Bold")

color.print(color)

#重设字体蓝色,背景色为当前终端背景色,默认风格显示

color.foreground = "Blue"

color.background = "Default"

color.style = "Default"

color.print("Hello")

