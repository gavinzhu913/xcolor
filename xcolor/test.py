from .colors import Foreground
from .style import *

def test_style():
    BLACK.print("BLACK")
    RED.print("RED")
    GREEN.print("GREEN")
    YELLOW.print("YELLOW")
    BLUE.print("BLUE")
    PURPLE.print("PURPLE")
    CYAN.print("CYAN")
    WHITE.print("WHITE")

    IBLACK.print("IBLACK")
    IRED.print("IRED")
    IGREEN.print("IGREEN")
    IYELLOW.print("IYELLOW")
    IBLUE.print("IBLUE")
    IPURPLE.print("IPURPLE")
    ICYAN.print("ICYAN")
    IWHITE.print("IWHITE")

    UBLACK.print("UBLACK")
    URED.print("URED")
    UGREEN.print("UGREEN")
    UYELLOW.print("UYELLOW")
    UBLUE.print("UBLUE")
    UPURPLE.print("UPURPLE")
    UCYAN.print("UCYAN")
    UWHITE.print("UWHITE")

    TBLACK.print("TBLACK")
    TRED.print("TRED")
    TGREEN.print("TGREEN")
    TYELLOW.print("TYELLOW")
    TBLUE.print("TBLUE")
    TPURPLE.print("TPURPLE")
    TCYAN.print("TCYAN")
    TWHITE.print("TWHITE")


def test_color():
    char = "█" * 10
    color_dict = {key: value for key, value in Foreground.__dict__.items() if
                  isinstance(value, int) and key != 'default'}
    for key, value in color_dict.items():
        Color(key).print(char, key.title())

