## Jocelyn Huang
## 10/29/2013
## Remove Punctuation from String
import string

def removePunctuation(s):
    if not isinstance(s, str): return None
    
    removal = {ord(char): None for char in string.punctuation}
    s = s.translate(removal).lower()
    return s