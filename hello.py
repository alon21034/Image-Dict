import os
import urllib, urllib2
from flask import *
from flask_bootstrap import Bootstrap
from Dict import Dict
from Translate import Trans

app = Flask(__name__, static_folder='static')
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
	msg = None
	ret = None
	trans = []
	if request.method == 'POST':
		msg = request.form['query']
		ret = search(msg)
		trans.append(dictcc(msg))
		trans.append(googletrans(msg))
	return render_template('template.html', urls = ret, tran = trans)

def search(str):
	print str
	result = urllib.urlopen(("http://www.bing.com/images/search?q=%s&FORM=HDRSC2#a" % str))
	content = result.read()
	urls = []
	for i in range(1, min(30, len(content)-2)):
		s = content.split("<img class=\"img_hid\" src2=\"")[i].split("&amp")[0];
		urls.append(s)
	return urls

def dictcc(str):
	d = Dict()
	d.getResponse(str)
	d.parseResponse()
	print d.printResults()
	return d.printResults()

def googletrans(str):
	d = Trans()
	d.getResponse(str)
	d.parseResponse()
	print d.printResults()
	return d.printResults()

if __name__ == '__main__':
	app.run(port = 5000, debug=True)