#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Eli
# datetime:2020-09-12 13:05
# software: PyCharm
import re

string = "123abc"
patt = "^[0-9]+abc$"
patten = re.compile(patt)
matchObj = patten.match(string)
print(matchObj)

