import urllib, urllib2

class Trans:
	def __init__(self):
		self.inputlang = 'de'
		self.outputlang = 'en'

	def getResponse(self, str):
		req = urllib2.Request('https://translate.google.com.tw/translate_a/single?client=t&sl=%s&tl=%s&hl=zh-TW&dt=bd&dt=ex&dt=ld&dt=md&dt=qc&dt=rw&dt=rm&dt=ss&dt=t&dt=at&dt=sw&ie=UTF-8&oe=UTF-8&oc=1&otf=1&ssel=0&tsel=0&q=%s' % (inputlang, outputlang, str), None,
                {'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'}
            )
		f = urllib2.urlopen(req)
		self.Response = f.read()
	def parseResponse(self):
		self.Result = 'apple'
		self.InputWord = 'Apfel'		

	def printResults(self):
		return [self.Result, self.InputWord]