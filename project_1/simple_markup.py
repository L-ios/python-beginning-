import sys, re
from util import *
print '<html><head><title>...</title><body>'

title = True
# sys.stdin 作为标准化输入，也就是在bash中的输入重定向
for block in blocks(sys.stdin):
    # r'\*(.+?)\*' 是一个正则表达式，而且是一个非贪婪的正则表达式
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'
