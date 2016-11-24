# -*- coding:utf-8 -*-
# 2016-10-13 16:36
# auther:wjp
# HTML 解析

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib

class MyHTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.key = {'time':None, 'event-title':None, 'event-location':None}

	def handle_starttag(self, tag, attrs):
		if tag == 'time':
			self.key['time'] = True
		elif tag == 'span' and attrs.__contains__(('class', 'event-location')):
			self.key['event-location'] = True
		elif tag == 'h3' and attrs.__contains__(('class', 'event-title')):
			self.key['event-title'] = True

	# def handle_endtag(self, tag):
		# print('endtag<%s>' % tag)

	# def handle_startendtag(self, tag, attrs):
		# print('startendtag<%s>' % tag)

	def handle_data(self, data):
		if self.key['time']:
			print 'Time:%s |' % data,
			self.key['time'] = None
		elif self.key['event-title']:
			print 'Title:%s |' % data,
			self.key['event-title'] = None
		elif self.key['event-location']:
			print 'Location:%s\n' % data,
			self.key['event-location'] = None

	# def handle_comment(self, data):
	# 	print('<!-- --> - %s' % data)

	# def handle_entityref(self, name):
	# 	print('&%s' % name)

	# def handle_charref(self, name):
	# 	print('$#%s' %name)

parser = MyHTMLParser()
html = urllib.urlopen('http://www.python.org/events/python-events/').read()
parser.feed(html)