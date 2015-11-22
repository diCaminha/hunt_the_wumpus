#!/usr/bin/env python3

import http.cookies
import time
import cgi
import cgitb

# This enables errors to show. Will turn off once
# everything is finished and working properly
cgitb.enable()

form = cgi.FieldStorage()

option = form.getvalue('currentRoom')

print('Content-Type: text/html')
print()
print('<html><body>')
print('You are in room # ',option, '<br />')

cookie = http.cookies.SimpleCookie()
cookie['currentRoom'] = option

print('</body></html>')
