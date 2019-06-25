import sys


class Xcolor:
    """
    Xcolor(foreground=None,background=None,default_foreground=None,default_background=None,style=None)
    
    color:Red,Green,Yellow,Blue,Purple,Cyan,Black,White

    style:Default,Highlight,Italic,Underline,Flashing,Reversed,Linethrough
    """

    __style = {
        "default": 0,
        "highlight": 1,
        "italic": 3,
        "underline": 4,
        "flashing": 5,
        "reversed": 7,
        "linethrough": 9
    }

    __foreground_map = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "purple": 35,
        "cyan": 36,
        "white": 37,
    }

    __background_map = {
        "black": 40,
        "red": 41,
        "green": 42,
        "yellow": 43,
        "blue": 44,
        "purple": 45,
        "cyan": 46,
        "white": 47,
    }

    __default_foreground = "White"
    __default_background = "Black"

    def __init__(self, foreground=None, background=None, default_foreground=None, default_background=None, style=None):
        self.foreground = foreground
        self.background = background
        self.default_foreground = default_foreground
        self.default_background = default_background
        self.style = style

    def print(self, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
        self.__print(*objects, sep=sep, end=end, file=file, flush=flush)

    def __reset(self):
        default_foreground = self.__foreground_map[self.default_foreground.lower()] if self.default_foreground else \
            self.__foreground_map[self.__default_foreground.lower()]
        default_background = self.__background_map[self.default_background.lower()] if self.default_background else \
            self.__background_map[self.__default_background.lower()]
        print("\033[0;%s;%sm" % (default_foreground, default_background), end="", flush=True)

    def __print(self, *objects, sep, end, file, flush):
        style = self.__style[self.style.lower()] if self.style else None
        foreground = self.__foreground_map[self.foreground.lower()] if self.foreground else None
        background = self.__background_map[self.background.lower()] if self.background else None
        print("\033[", end="", flush=True)
        if style:
            print("%s" % (style), end="", flush=True)
        if foreground:
            print(";%s" % (foreground), end="", flush=True)
        if background:
            print(";%s" % (background), end="", flush=True)
        print("m", end="", flush=True)
        print(*objects, sep=sep, end='', file=file, flush=flush)
        self.__reset()
        print(end=end, flush=True)


RED = Xcolor("Red")
GREEN = Xcolor("Green")
BLUE = Xcolor("Blue")
CYAN = Xcolor("Cyan")
PURPLE = Xcolor("Purple")
YELLOW = Xcolor("Yellow")
WHITE = Xcolor("White")
BLACK = Xcolor("Black")

HRED = Xcolor("Red", style="Highlight")
HGREEN = Xcolor("Green", style="Highlight")
HBLUE = Xcolor("Blue", style="Highlight")
HCYAN = Xcolor("Cyan", style="Highlight")
HPURPLE = Xcolor("Purple", style="Highlight")
HYELLOW = Xcolor("Yellow", style="Highlight")
HWHITE = Xcolor("White", style="Highlight")
HBLACK = Xcolor("Black", style="Highlight")

IRED = Xcolor("Red", style="Italic")
IGREEN = Xcolor("Green", style="Italic")
IBLUE = Xcolor("Blue", style="Italic")
ICYAN = Xcolor("Cyan", style="Italic")
IPURPLE = Xcolor("Purple", style="Italic")
IYELLOW = Xcolor("Yellow", style="Italic")
IWHITE = Xcolor("White", style="Italic")
IBLACK = Xcolor("Black", style="Italic")

URED = Xcolor("Red", style="Underline")
UGREEN = Xcolor("Green", style="Underline")
UBLUE = Xcolor("Blue", style="Underline")
UCYAN = Xcolor("Cyan", style="Underline")
UPURPLE = Xcolor("Purple", style="Underline")
UYELLOW = Xcolor("Yellow", style="Underline")
UWHITE = Xcolor("White", style="Underline")
UBLACK = Xcolor("Black", style="Underline")

if __name__ == "__main__":
    RED.print("Hello World!")
    GREEN.print("Hello World!")
    BLUE.print("Hello World!")
    CYAN.print("Hello World!")
    PURPLE.print("Hello World!")
    YELLOW.print("Hello World!")
    WHITE.print("Hello World!")
    BLACK.print("Hello World!")

    HRED.print("Hello World!")
    HGREEN.print("Hello World!")
    HBLUE.print("Hello World!")
    HCYAN.print("Hello World!")
    HPURPLE.print("Hello World!")
    HYELLOW.print("Hello World!")
    HWHITE.print("Hello World!")
    HBLACK.print("Hello World!")

    IRED.print("Hello World!")
    IGREEN.print("Hello World!")
    IBLUE.print("Hello World!")
    ICYAN.print("Hello World!")
    IPURPLE.print("Hello World!")
    IYELLOW.print("Hello World!")
    IWHITE.print("Hello World!")
    IBLACK.print("Hello World!")

    URED.print("Hello World!")
    UGREEN.print("Hello World!")
    UBLUE.print("Hello World!")
    UCYAN.print("Hello World!")
    UPURPLE.print("Hello World!")
    UYELLOW.print("Hello World!")
    UWHITE.print("Hello World!")
    UBLACK.print("Hello World!")
