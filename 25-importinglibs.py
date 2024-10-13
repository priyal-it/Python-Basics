#lec 11: Different ways to import a library
'''
import calendar
print(calendar.month(2024,9))
print(calendar.calendar(2024))
'''

"""
from calendar import month,calendar
print(calendar(2024))
print(month(2024,9))
"""

'''
import calendar as c
print(c.month(2024,9))
'''

from calendar import month as m
print(m(2024,8))