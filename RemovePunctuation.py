## Jocelyn Huang
## 10/29/2013
## Remove Punctuation from String
import string

def removePunctuation(s):
    if not isinstance(s, str): return None
    s = s.replace("-", " ")
    s = s.replace(".", " ")
    s = s.replace("/", " ")
    #if('"' in s):    #--> delete the words in between?s
    #    print("hey")
    removal = {ord(char): None for char in string.punctuation}
    s = s.translate(removal).lower()
    return s