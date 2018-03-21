# -*- coding: utf-8 -*-
from enum import Enum
M = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for key, member in M.__members__.items():
    print( key, '=>', member, ',', member.value, ',', type(member) )
	
