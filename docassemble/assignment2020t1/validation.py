import re 
from docassemble.base.util import *

def check_nric(string):
  if not re.match(r'[STst][0-9]{7}[A-z]', string) or len(string) > 9:
    validation_error('Invalid NRIC format.')
  return True