from .colors import Foreground
from .style import *


def test_style():
    black1.print("black1")
    red1.print("red1")
    green1.print("green1")
    yellow1.print("yellow1")
    blue1.print("blue1")
    magenta1.print("magenta1")
    cyan1.print("cyan1")
    white1.print("white1")

    black2.print("black2")
    red2.print("red2")
    green2.print("green2")
    yellow2.print("yellow2")
    blue2.print("blue2")
    magenta2.print("magenta2")
    cyan2.print("cyan2")
    white2.print("white2")

    iblack1.print("iblack1")
    ired1.print("ired1")
    igreen1.print("igreen1")
    iyellow1.print("iyellow1")
    iblue1.print("iblue1")
    imagenta1.print("imagenta1")
    icyan1.print("icyan1")
    iwhite1.print("iwhite1")

    iblack2.print("iblack2")
    ired2.print("ired2")
    igreen2.print("igreen2")
    iyellow2.print("iyellow2")
    iblue2.print("iblue2")
    imagenta2.print("imagenta2")
    icyan2.print("icyan2")
    iwhite2.print("iwhite2")

    ublack1.print("ublack1")
    ured1.print("ured1")
    ugreen1.print("ugreen1")
    uyellow1.print("uyellow1")
    ublue1.print("ublue1")
    umagenta1.print("umagenta1")
    ucyan1.print("ucyan1")
    uwhite1.print("uwhite1")

    ublack2.print("ublack2")
    ured2.print("ured2")
    ugreen2.print("ugreen2")
    uyellow2.print("uyellow2")
    ublue2.print("ublue2")
    umagenta2.print("umagenta2")
    ucyan2.print("ucyan2")
    uwhite2.print("uwhite2")

    tblack1.print("tblack1")
    tred1.print("tred1")
    tgreen1.print("tgreen1")
    tyellow1.print("tyellow1")
    tblue1.print("tblue1")
    tmagenta1.print("tmagenta1")
    tcyan1.print("tcyan1")
    twhite1.print("twhite1")

    tblack2.print("tblack2")
    tred2.print("tred2")
    tgreen2.print("tgreen2")
    tyellow2.print("tyellow2")
    tblue2.print("tblue2")
    tmagenta2.print("tmagenta2")
    tcyan2.print("tcyan2")
    twhite2.print("twhite2")

    fblack1.print("fblack1")
    fred1.print("fred1")
    fgreen1.print("fgreen1")
    fyellow1.print("fyellow1")
    fblue1.print("fblue1")
    fmagenta1.print("fmagenta1")
    fcyan1.print("fcyan1")
    fwhite1.print("fwhite1")

    fblack2.print("fblack2")
    fred2.print("fred2")
    fgreen2.print("fgreen2")
    fyellow2.print("fyellow2")
    fblue2.print("fblue2")
    fmagenta2.print("fmagenta2")
    fcyan2.print("fcyan2")
    fwhite2.print("fwhite2")

    bblack.print("bblack")
    bred.print("bred")
    bgreen.print("bgreen")
    byellow.print("byellow")
    bblue.print("bblue")
    bmagenta.print("bmagenta")
    bcyan.print("bcyan")
    bwhite.print("bwhite")


def test_color():
    char = "█" * 10
    color_dict = {key: value for key, value in Foreground.__dict__.items() if
                  isinstance(value, int) and key != 'default'}
    for key, value in color_dict.items():
        Color(key).print(char, key.title())
