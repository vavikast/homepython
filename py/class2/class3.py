#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum,unique
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6


day1=Weekday.Mon
print(day1)
print("show weekday.mon")
print(Weekday.Thu)
print("show weekday.Thu")
print(Weekday['Thu'])
print("show weekday['Thu']")
print(Weekday.Tue.value)
print("show weekday.Tue.value")
print(Weekday(1))
print("show Weekday(1)")
