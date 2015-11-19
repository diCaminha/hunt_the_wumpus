#!/usr/bin/env python3

import http.cookies
import time
import cgi

form = cgi.FieldStorage()

option = form.getvalue('firstChoice')

print('Content-Type: text/html')
print()
print('<html><body>')
print('User entered option number ', option, '<br />')
print('Now storing the option in Cookie named \'FirstChoice\'...<br />')

cookie = http.cookies.SimpleCookie()
cookie['FirstChoice'] = option

print('Now retrieving the option the user entered by printing out the cookie we just created...<br />')
print(cookie, '<br />')

print('If both numbers match then we have success!<br /><br />')

print('<a href="../start.html"><h3>Click Here to Start Over</h3></a>')
print('</body></html>')
