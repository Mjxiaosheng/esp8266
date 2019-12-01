    #ssd1306_lib
    #重新封装了显示汉语和任意大小像素图像的方法，使ssd1306更易用。
    #简单用法：
    
    from machine import Pin, I2C
    from ssd1306_lib import SSD1306_I2C
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    OLED = SSD1306_I2C(128, 64, i2c)
    OLED.draw_all(id, x_size, y_size, x_axis, y_axis)   #显示任意图像
    OLED.draw_chinese(chinese_str,x_axis,y_axis)        #显示汉语
    OLED.show()
    
    #id:要显示的：图像在font.byte2的id
    #x_size：显示图像的横向像素大小
    #y_size：显示图像纵向像素大小
    #x_axis：显示图像的横向偏移像素，在draw_chinese中为偏移半个汉字宽度的像素
    #y_axis：显示图像的纵向偏移像素，在draw_chinese中为偏移一个汉字高度的像素
    #chinese_str：要显示的中文字符串


    #font.py
    #byte存储draw_chinese的字模，byte2储存draw_all的字模



    #format_str.py
    #mk_cn_en_str(text)封装了128*64的oled屏格式化显示中英文字符的函数
    #简单用法:
     
    from format_str import mk_cn_en_str
    mk_cn_en_str(text)
    
    #text为要显示的字符串
    #注意：esp8266无论是webREPL还是MicroPython File Uploader等都不能输入中文所以交互式使用时会出错，不过可以调用。
    #从屏幕左上角开始显示汉字为16*16像素，英文为8*16像素（中英文都要在font.byte中储存字模）
    #文件中是sda接Pin4，scl接Pin5可以根据需要修改
