# xcolor
color values:Red,Green,Yellow,Blue,Purple,Cyan,Black,White

style values:Default,Highlight,Italic,Underline,Flashing,Reversed,Linethrough

create a color object and use print

eg.

yellow =  Xcolor("Yellow")

yellow.print("Hello World!")

blue = Xcolor(foreground="Blue",background="Whilte",style="Highlight")

blue.print("Blue")

blue.foreground="Green"

blue.print("Green color!")
