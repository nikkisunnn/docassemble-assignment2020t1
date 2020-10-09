import re 
from docassemble.base.util import *

def check_nric(nric):
    nricCheckDigits = 'JZIHGFEDCBA'
    weights = [2, 7, 6, 5, 4, 3, 2]
    if len(nric) != 9:
        return False

    firstChar = nric[0].upper()
    digits = nric[1:8]
    lastChar = nric[8].upper()
    
    if firstChar not in "ST" or not digits.isdigit():
        return False

    total = 0
    if firstChar in "T":
        total += 4
    for i in range(7):
        total += int(digits[i]) * weights[i]

    if firstChar in "ST"and nricCheckDigits[total % 11] == lastChar:
      return True
    else:
      return False
