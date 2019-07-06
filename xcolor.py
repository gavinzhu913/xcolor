import sys


class Foreground:
    default = 38
    blacka = 30
    blackb = 90
    reda = 31
    redb = 91
    greena = 32
    greenb = 92
    yellowa = 33
    yellowb = 93
    bluea = 34
    blueb = 94
    purplea = 35
    purpleb = 95
    cyana = 36
    cyanb = 96
    whitea = 37
    whiteb = 97
    black = blackb
    red = reda
    green = greenb
    yellow = yellowa
    blue = blueb
    purple = purpleb
    cyan = cyana
    white = whiteb


class Background:
    default = 48
    blacka = 40
    blackb = 100
    reda = 41
    redb = 101
    greena = 42
    greenb = 102
    yellowa = 43
    yellowb = 103
    bluea = 44
    blueb = 104
    purplea = 45
    purpleb = 105
    cyana = 46
    cyanb = 106
    whitea = 47
    whiteb = 107
    black = blackb
    red = reda
    green = greenb
    yellow = yellowa
    blue = blueb
    purple = purpleb
    cyan = cyana
    white = whiteb


class Style:
    default = 0
    bold = 1
    italic = 3
    underline = 4
    flash = 5
    throughline = 9


class Color:

    def __init__(self, foreground="default", background="default", style="default"):
        self.foreground = foreground
        self.background = background
        self.style = style

    def print(self, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
        print('\033[%s;%s;%sm' % (Style.__dict__[self.style.lower()], Foreground.__dict__[self.foreground.lower()], \
                                  Background.__dict__[self.background.lower()]), end='')
        print(*objects, sep=sep, end='', file=file, flush=flush)
        print('\033[0m', end=end)

    def __getattr__(self, item):
        if isinstance(item, str):
            return item.title()

    def __repr__(self):
        return "<Color('%s','%s','%s')>" % (self.foreground.title(), self.background.title(), self.style.title())


BLACK = Color("Black")
RED = Color("Red")
GREEN = Color("Green")
YELLOW = Color("Yellow")
BLUE = Color("Blue")
PURPLE = Color("Purple")
CYAN = Color("Cyan")
WHITE = Color("White")

IBLACK = Color("Black", style="Italic")
IRED = Color("Red", style="Italic")
IGREEN = Color("Green", style="Italic")
IYELLOW = Color("Yellow", style="Italic")
IBLUE = Color("Blue", style="Italic")
IPURPLE = Color("Purple", style="Italic")
ICYAN = Color("Cyan", style="Italic")
IWHITE = Color("White", style="Italic")

UBLACK = Color("Black", style="Underline")
URED = Color("Red", style="Underline")
UGREEN = Color("Green", style="Underline")
UYELLOW = Color("Yellow", style="Underline")
UBLUE = Color("Blue", style="Underline")
UPURPLE = Color("Purple", style="Underline")
UCYAN = Color("Cyan", style="Underline")
UWHITE = Color("White", style="Underline")

TBLACK = Color("Black", style="Throughline")
TRED = Color("Red", style="Throughline")
TGREEN = Color("Green", style="Throughline")
TYELLOW = Color("Yellow", style="Throughline")
TBLUE = Color("Blue", style="Throughline")
TPURPLE = Color("Purple", style="Throughline")
TCYAN = Color("Cyan", style="Throughline")
TWHITE = Color("White", style="Throughline")


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
