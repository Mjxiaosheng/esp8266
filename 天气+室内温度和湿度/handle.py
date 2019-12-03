#filename:handle.py
# -*- coding:utf-8
import web


class Handle(object):
	def GET(self,name): 
		try:
			if name == 'weather':
				f = open("wea_data")
				c = f.read()
				f.close()
				return c
			else:
				return "read failure"
		except:
			return "read failure."
	def POST(self,name):
		try:
			if name == "weather":
				g = open("reply_data","w")
				g.write(web.data())
				g.close()
				f = open("wea_data")
				c = f.read()
				f.close()
				return c
			else:
				return "error"
		except:
			return "error"
