from ssd1306_lib import SSD1306_I2C
from machine import Pin, I2C
import urequests as requests
from format_str_pro import ssd1306_i2c_lump_print_str
import utime
import dht

utime.sleep(7)
i2c = I2C(scl=Pin(2), sda=Pin(0))
oled = SSD1306_I2C(128, 64, i2c)
d = dht.DHT22(Pin(5))
while True:
    try:
        d.measure()
        temp = "室内温度:" + str(d.temperature()) + "℃"
        humidity = "室内湿度:" + str(d.humidity()) + "%"
        reply_text = temp + humidity
        try:
            r = requests.post("http://----------------------/weather", data=reply_text)
            r.encoding = 'utf-8'
            data = eval(r.text)
        except:
            data = ['晴', '--', '--℃', '--']
        if len(data) == 4:
            data[1] = data[1] + '/' + data[2]
            del data[2]
        oled.fill(0)
        if '雪' in data[0]:
            oled.draw_all("snow", 32, 32, 0, 0)
        elif '雨' in data[0]:
            oled.draw_all("rain", 32, 32, 0, 0)
        elif '多云' in data[0]:
            oled.draw_all("cloudy", 32, 32, 0, 0)
        elif '阴' in data[0]:
            oled.draw_all("overcast", 32, 32, 0, 0)
        elif '晴' in data[0]:
            oled.draw_all("sun", 32, 32, 0, 0)
        else:
            ssd1306_i2c_lump_print_str(oled, "-/-/-/-/", 32, 32, 0, 0)
        ssd1306_i2c_lump_print_str(oled, temp, 128, 16, 0, 32)
        ssd1306_i2c_lump_print_str(oled, humidity, 128, 16, 0, 48)
        ssd1306_i2c_lump_print_str(oled, data[1], 96, 16, 32, 0)
        ssd1306_i2c_lump_print_str(oled, data[2], 96, 16, 32, 16)
        oled.show()
        utime.sleep(5)
    except KeyboardInterrupt:
        break
    except:
        oled.fill(0)
        oled.draw_all("bug", 127, 63, 0, 0)
        oled.show()
        utime.sleep(5)
        continue
