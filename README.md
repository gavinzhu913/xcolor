## xcolor

支持UNIX及类UNIX操作系统
支持Python版本为Python3.0+

## 颜色值:



每种颜色有两种相近的颜色,以1和2区分.
"Black1","Red1","Green1","Yellow1","Blue1","Magenta1","Cyan1","White1"
"Black2","Red2","Green2","Yellow2","Blue2","Magenta2","Cyan2","White2"




## 字体风格:



"Bold":高亮加粗  
"Italic":斜体  
"Underline":下划线  
"Flash":闪烁  
"Throughline":删除线  



## 内置对象:

字体风格需要终端支持  

常规颜色风格  
black1,red1,green1,yellow1,blue1,magenta1,cyan1,white1  
black2,red2,green2,yellow2,blue2,magenta2,cyan2,white2  
斜体风格  
iblack1,ired1,igreen1,iyellow1,iblue1,imagenta1,icyan1,iwhite1  
iblack2,ired2,igreen2,iyellow2,iblue2,imagenta2,icyan2,iwhite2  
下划线风格   
ublack1,ured1,ugreen1,uyellow1,ublue1,umagenta1,ucyan1,uwhite1  
ublack2,ured2,ugreen2,uyellow2,ublue2,umagenta2,ucyan2,uwhite2  
删除线风格   
tblack1,tred1,tgreen1,tyellow1,tblue1,tmagenta1,tcyan1,twhite1  
tblack2,tred2,tgreen2,tyellow2,tblue2,tmagenta2,tcyan2,twhite2  
闪烁风格    
fblack1,fred1,fgreen1,fyellow1,fblue1,fmagenta1,fcyan1,fwhite1  
fblack2,fred2,fgreen2,fyellow2,fblue2,fmagenta2,fcyan2,fwhite2  
粗体风格  
bblack,bred,bgreen,byellow,bblue,bmagenta1,bcyan,bwhite  


## eg.

    import logging
    from xcolor import *
    
    # 测试颜色
    test_color()
    # 测试内置颜色对象
    test_style()
    
    
    # 用Color对象作为装饰器,改变被装饰函数内的标准输出
    @yellow1
    def test():
        print("*" * 20)
    
    
    test()
    
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    # setenv与clear成对使用,区间的标准输出风格被改变
    # 以绿色打印warning,红色打印error
    green1.setenv()
    logger.warning("warning")
    Color.clear()
    red2.setenv()
    logger.error("error")
    Color.clear()
    
    logger.error = ured2(logger.error)
    logger.warning = uyellow1(logger.warning)
    logger.info = yellow2(logger.info)
    logger.error("ERROR")
    logger.warning("WARNNING")
    logger.info("INFO")
    
