# Problem: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('-> {} > {}'.format(i[0], i[1]))

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('-> {} > {}'.format(i[0], i[1]))

T = int(input())
html = ''
for _  in range(T):
    html += input()
parser = MyHTMLParser()
parser.feed(html)
