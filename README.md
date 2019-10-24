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
xcolor_black1,xcolor_red1,xcolor_green1,xcolor_yellow1,xcolor_blue1,xcolor_magenta1,xcolor_cyan1,xcolor_white1  
xcolor_black2,xcolor_red2,xcolor_green2,xcolor_yellow2,xcolor_blue2,xcolor_magenta2,xcolor_cyan2,xcolor_white2  
斜体风格  
xcolor_iblack1,xcolor_ired1,xcolor_igreen1,xcolor_iyellow1,xcolor_iblue1,xcolor_imagenta1,xcolor_icyan1,xcolor_iwhite1  
xcolor_iblack2,xcolor_ired2,xcolor_igreen2,xcolor_iyellow2,xcolor_iblue2,xcolor_imagenta2,xcolor_icyan2,xcolor_iwhite2  
下划线风格   
xcolor_ublack1,xcolor_ured1,xcolor_ugreen1,xcolor_uyellow1,xcolor_ublue1,xcolor_umagenta1,xcolor_ucyan1,xcolor_uwhite1  
xcolor_ublack2,xcolor_ured2,xcolor_ugreen2,xcolor_uyellow2,xcolor_ublue2,xcolor_umagenta2,xcolor_ucyan2,xcolor_uwhite2  
删除线风格   
xcolor_tblack1,xcolor_tred1,xcolor_tgreen1,xcolor_tyellow1,xcolor_tblue1,xcolor_tmagenta1,xcolor_tcyan1,xcolor_twhite1  
xcolor_tblack2,xcolor_tred2,xcolor_tgreen2,xcolor_tyellow2,xcolor_tblue2,xcolor_tmagenta2,xcolor_tcyan2,xcolor_twhite2  
闪烁风格    
xcolor_fblack1,xcolor_fred1,xcolor_fgreen1,xcolor_fyellow1,xcolor_fblue1,xcolor_fmagenta1,xcolor_fcyan1,xcolor_fwhite1  
xcolor_fblack2,xcolor_fred2,xcolor_fgreen2,xcolor_fyellow2,xcolor_fblue2,xcolor_fmagenta2,xcolor_fcyan2,xcolor_fwhite2  
粗体风格  
xcolor_bblack,xcolor_bred,xcolor_bgreen,xcolor_byellow,xcolor_bblue,xcolor_bmagenta1,xcolor_bcyan,xcolor_bwhite  


## eg.

    import logging
    from xcolor import *
    
    # 测试颜色
    test_color()
    # 测试内置颜色对象
    test_style()
    
    
    # 用Color对象作为装饰器,改变被装饰函数内的标准输出
    @xcolor_yellow1
    def test():
        print("*" * 20)
    
    
    test()
    
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    # setenv与clear成对使用,区间的标准输出风格被改变
    # 以绿色打印warning,红色打印error
    xcolor_green1.setenv()
    logger.warning("warning")
    Color.clear()
    xcolor_red2.setenv()
    logger.error("error")
    Color.clear()
    
    logger.error = xcolor_ured2(logger.error)
    logger.warning = xcolor_uyellow1(logger.warning)
    logger.info = xcolor_yellow2(logger.info)
    logger.error("ERROR")
    logger.warning("WARNNING")
    logger.info("INFO")
    
