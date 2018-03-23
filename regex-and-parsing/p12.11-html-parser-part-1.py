# Problem: https://www.hackerrank.com/domains/python/py-regex/2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for i in attrs:
            print('-> {} > {}'.format(i[0], i[1]))
    def handle_endtag(self, tag):
        print("End   : {}".format(tag))
    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for i in attrs:
            print('-> {} > {}'.format(i[0], i[1]))

T = int(input())
html = ''
for _  in range(T):
    html += input()
parser = MyHTMLParser()
parser.feed(html)
