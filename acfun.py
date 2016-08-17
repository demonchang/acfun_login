#!/usr/bin/env python

import urllib, urllib2, cookielib, re, time, requests

LOGIN_URL = 'http://passport.acfun.tv/login.aspx'
ACCOUNT = 'YOURCOUNT'
PWD = 'PASSWORD'

class Acfun(object):

	def __init__(self):
		self.account = ACCOUNT
		self.pwd = PWD
		self.login_url = LOGIN_URL
		self.cookiefile = 'cookie.txt'
		self.html = ''

	def login(self):
		data_json = {'password':self.pwd, 'username':self.account}
		data  = urllib.urlencode(data_json)
		cookie = cookielib.MozillaCookieJar(self.cookiefile)		
		handler = urllib2.HTTPCookieProcessor(cookie)		
		opener = urllib2.build_opener(handler)		
		response = opener.open(self.login_url, data)		
		cookie.save(ignore_discard=True, ignore_expires=True)
		#target_url = 'http://www.acfun.tv/member/#area=profile'
		#result = opener.open(target_url)
		#self.html = result.read()

	def getContent(self):
		pattern = re.compile(r'<div id="mainer-inner">.*?class="name">(.*?)</a>.*?', re.S)
		result = re.findall(pattern, self.html)
		print result[0]

	def signin(self):
		cookie = cookielib.MozillaCookieJar()
		cookie.load(self.cookiefile, ignore_discard=True, ignore_expires=True)
		times =  int(time.time()*1000)
		url = 'http://www.acfun.tv/webapi/record/actions/signin?channel=0&date='+str(times)
		#url = 'http://www.acfun.tv/member/checkin.aspx'
		headers = {
			"Host": "www.acfun.tv",
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
			"Accept": "*/*",
			"Accept-Language": "en-US,en;q=0.5",
			"Referer": "http://www.acfun.tv/member/",
		}
		data = ''
		data = urllib.urlencode(data)
		req = urllib2.Request(url, headers=headers)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
		#opener.addheaders = [('Referer', 'http://www.acfun.tv/member/')]
		response = opener.open(req, data)
		print response.read()	

		

if __name__ == "__main__":

	acfun = Acfun()
	acfun.login()
	#acfun.getContent()
	acfun.signin()

