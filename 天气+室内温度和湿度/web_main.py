#filename:main.py
# -*- coding:utf-8
import web
from handle import Handle
web.config.debug = False


urls = ('/(.*)','Handle')

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
