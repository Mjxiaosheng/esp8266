from ssd1306_lib import SSD1306_I2C
from machine import Pin, I2C


def mk_cn_en_str(text):
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    oled = SSD1306_I2C(128, 64, i2c)
    row = 0
    col = 0
    for i in text:
        is_cn = i.encode('utf-8')
        if col == 16:
            col = 0
            row += 1
            if row == 4:
                break
        else:
            if len(is_cn) >= 2:
                if col == 15:
                    row +=1
                    col =0
                    oled.draw_chinese(i, col, row)
                    col += 2
                else:
                    oled.draw_chinese(i, col, row)
                    col += 2
            else:
                oled.draw_chinese(i, col, row)
                col += 1
    oled.show()
