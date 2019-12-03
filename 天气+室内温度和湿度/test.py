# -*- coding:utf-8 -*-
import re
import requests
import time


def get_weather():
    while True:
        try:
            path = 'http://www.weather.com.cn/weather/101100101.shtml'
            headers = {'Referer': 'http://www.weather.com.cn/weather1d/101100101.shtml',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/78.0.3904.97 Safari/537.36'
                       }
            r = requests.get(path, headers=headers, timeout=1)
            r.encoding = r.apparent_encoding
            text = r.text
            need_all = re.findall(u'<ul class="t clea[\s\S]*?</ul>', text)
            need = need_all[0]
            data = []
            days = re.findall(u'<h1>(.*?)</h1>', need)
            max_tem = re.findall(u'an>(-?[\d]*℃?)</span>', need)
            min_tem = re.findall(u'<i>(-?[\d]*℃?)</i>', need)
            if len(max_tem) < len(min_tem):
                max_tem.insert(0, min_tem[0])
                is_now = True
            else:
                is_now = False
            wea = re.findall(u'class="wea">(.*?)</p>', need)
            wind = re.findall(u'<i>(.*?级)</i>', need)
            for i in range(7):
                tmp = []
                tmp.append(days[i])
                tmp.append(u' 最高气温：')
                tmp.append(max_tem[i])
                tmp.append(u' 最低气温：')
                tmp.append(min_tem[i])
                tmp.append(u' 天气：')
                tmp.append(wea[i])
                tmp.append(u' 风速：')
                tmp.append(wind[i])
                data.append(tmp)
            if is_now:
                for i in range(3):
                    del data[0][1]
                data[0].insert(1, u' 当前温度：')
            tmp = []
            i = 0
            if len(data[i]) == 7:
                tmp.append(data[i][4])
                tmp.append(data[i][2])
                tmp.append(data[i][-1])
            elif len(data[i]) == 9:
                tmp.append(data[i][6])
                tmp.append(data[i][2])
                tmp.append(data[i][4])
                tmp.append(data[i][-1])
            return_text = "["
            for i in tmp:
                i = "'" + i + "',"
                return_text += i
            return_text += "]"
            return_text = return_text.encode('utf-8')
        except:
            return_text = '["--","--","--"]'
        with open("wea_data", 'w') as f:
            f.write(return_text)
        print return_text
        time.sleep(7200)


if __name__ == "__main__":
    get_weather()
