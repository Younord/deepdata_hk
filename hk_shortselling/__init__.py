#coding: utf8

import shortselling
import time, os

today = time.strftime('%Y%m%d')
path = __path__[0] + '/' + today
if not os.path.exists(path):
    os.mkdir(path)

jsfile = None
jstimeout = 30
output = None
params = {}
pymodname = 'shortselling'
description = u'港股市场沽空'
finalinvoke = ['start', '/wait', 'hkexe/DeepSecurityMaster.exe', '-d', os.path.join(os.path.dirname(__file__), today), '-t', '0x04']
finaltimeout = 60
