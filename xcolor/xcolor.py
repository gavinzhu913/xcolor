import sys
import functools
from .colors import *


class Color:

    def __init__(self, foreground="default", background="default", style="default"):
        self.foreground = foreground
        self.background = background
        self.style = style

    def print(self, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
        print('\033[%s;%s;%sm' % (
            Style.__dict__[self.style.lower()], Foreground.__dict__[self.foreground.lower()], \
            Background.__dict__[self.background.lower()]), end='', flush=True)
        print(*objects, sep=sep, end='', file=file, flush=flush)
        print('\033[0m', end=end, flush=True)

    def setenv(self):
        print('\033[%s;%s;%sm' % (
            Style.__dict__[self.style.lower()], Foreground.__dict__[self.foreground.lower()], \
            Background.__dict__[self.background.lower()]), end='', flush=True)

    def clear(self):
        print('\033[0m', end='', flush=True)

    def __getattr__(self, item):
        if isinstance(item, str):
            return item.title()

    def __repr__(self):
        return "<Color('%s','%s','%s')>" % (self.foreground.title(), self.background.title(), self.style.title())


def color(color_obj):
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            print('\033[%s;%s;%sm' % (
                Style.__dict__[color_obj.style.lower()],
                Foreground.__dict__[color_obj.foreground.lower()], \
                Background.__dict__[color_obj.background.lower()]), end='', flush=True)
            value = func(*args, **kwargs)
            print('\033[0m', end='', flush=True)
            return value
        return wrap
    return decorator


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
