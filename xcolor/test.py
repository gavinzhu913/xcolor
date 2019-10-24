from .colors import Foreground
from .style import *


def test_style():
    xcolor_black1.print("black1")
    xcolor_red1.print("red1")
    xcolor_green1.print("green1")
    xcolor_yellow1.print("yellow1")
    xcolor_blue1.print("blue1")
    xcolor_magenta1.print("magenta1")
    xcolor_cyan1.print("cyan1")
    xcolor_white1.print("white1")

    xcolor_black2.print("black2")
    xcolor_red2.print("red2")
    xcolor_green2.print("green2")
    xcolor_yellow2.print("yellow2")
    xcolor_blue2.print("blue2")
    xcolor_magenta2.print("magenta2")
    xcolor_cyan2.print("cyan2")
    xcolor_white2.print("white2")


    xcolor_iblack1.print("iblack1")
    xcolor_ired1.print("ired1")
    xcolor_igreen1.print("igreen1")
    xcolor_iyellow1.print("iyellow1")
    xcolor_iblue1.print("iblue1")
    xcolor_imagenta1.print("imagenta1")
    xcolor_icyan1.print("icyan1")
    xcolor_iwhite1.print("iwhite1")

    xcolor_iblack2.print("iblack2")
    xcolor_ired2.print("ired2")
    xcolor_igreen2.print("igreen2")
    xcolor_iyellow2.print("iyellow2")
    xcolor_iblue2.print("iblue2")
    xcolor_imagenta2.print("imagenta2")
    xcolor_icyan2.print("icyan2")
    xcolor_iwhite2.print("iwhite2")

    xcolor_ublack1.print("ublack1")
    xcolor_ured1.print("ured1")
    xcolor_ugreen1.print("ugreen1")
    xcolor_uyellow1.print("uyellow1")
    xcolor_ublue1.print("ublue1")
    xcolor_umagenta1.print("umagenta1")
    xcolor_ucyan1.print("ucyan1")
    xcolor_uwhite1.print("uwhite1")

    xcolor_ublack2.print("ublack2")
    xcolor_ured2.print("ured2")
    xcolor_ugreen2.print("ugreen2")
    xcolor_uyellow2.print("uyellow2")
    xcolor_ublue2.print("ublue2")
    xcolor_umagenta2.print("umagenta2")
    xcolor_ucyan2.print("ucyan2")
    xcolor_uwhite2.print("uwhite2")


    xcolor_tblack1.print("tblack1")
    xcolor_tred1.print("tred1")
    xcolor_tgreen1.print("tgreen1")
    xcolor_tyellow1.print("tyellow1")
    xcolor_tblue1.print("tblue1")
    xcolor_tmagenta1.print("tmagenta1")
    xcolor_tcyan1.print("tcyan1")
    xcolor_twhite1.print("twhite1")

    xcolor_tblack2.print("tblack2")
    xcolor_tred2.print("tred2")
    xcolor_tgreen2.print("tgreen2")
    xcolor_tyellow2.print("tyellow2")
    xcolor_tblue2.print("tblue2")
    xcolor_tmagenta2.print("tmagenta2")
    xcolor_tcyan2.print("tcyan2")
    xcolor_twhite2.print("twhite2")


    xcolor_fblack1.print("fblack1")
    xcolor_fred1.print("fred1")
    xcolor_fgreen1.print("fgreen1")
    xcolor_fyellow1.print("fyellow1")
    xcolor_fblue1.print("fblue1")
    xcolor_fmagenta1.print("fmagenta1")
    xcolor_fcyan1.print("fcyan1")
    xcolor_fwhite1.print("fwhite1")

    xcolor_fblack2.print("fblack2")
    xcolor_fred2.print("fred2")
    xcolor_fgreen2.print("fgreen2")
    xcolor_fyellow2.print("fyellow2")
    xcolor_fblue2.print("fblue2")
    xcolor_fmagenta2.print("fmagenta2")
    xcolor_fcyan2.print("fcyan2")
    xcolor_fwhite2.print("fwhite2")

    xcolor_bblack.print("bblack")
    xcolor_bred.print("bred")
    xcolor_bgreen.print("bgreen")
    xcolor_byellow.print("byellow")
    xcolor_bblue.print("bblue")
    xcolor_bmagenta.print("bmagenta")
    xcolor_bcyan.print("bcyan")
    xcolor_bwhite.print("bwhite")


def test_color():
    char = "█" * 10
    color_dict = {key: value for key, value in Foreground.__dict__.items() if
                  isinstance(value, int) and key != 'default'}
    for key, value in color_dict.items():
        Color(key).print(char, key.title())
