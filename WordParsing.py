## Jocelyn Huang
## 09/10/2013
## Three Letter Words
import string

s = "this, I am a fan of is it's a string with words that have the one to not exactly three letter rule."

#s = "that isn't good not bad not great not horrible really I need a small word cool aint great though"
#
#-----------------<Removes punctuation>---------------------------
removal = {ord(char): None for char in string.punctuation}
s = s.translate(removal)
words = [elt for elt in s.split(" ")]
wordsCopy = words[:]
#
#-----------------<Takes out negatives>---------------------------
negatives = ["not", "pet", "never", "dont", "wasnt", "isnt", "no", "aint"]
#
# Creates dictionary of {"negative": ["words", "that", "follow"], "other_negative": []}
#
set_aside = {negatives[i]: [words[index] for index in [j+1 for j, elt in enumerate(words) if elt == negatives[i]]] for i in range(len(negatives))}
#
# Removes negative pairings (e.g. "not good")
#
words = [words[i] if (words[i-1] not in negatives and words[i] not in negatives) else None for i in range(len(words))]
words = list(filter(None, words))
#
#-----------------<Filters short words>---------------------------
#
# Three letter words to be included. Creation of dictionaryRevised removes 1~3 letter words excluding these.
three_letter_words = ['top', 'add', 'who', 'hit', 'all', 'tad', 'why', 'fan', 'art', 'out', 'new', 'old', 'let', 'put', 'mad', 'odd',]
mergeTarget = {"this": 50, "target": 30, "good": 80, "rule": 90, "fan": 95} # Test merger
words = {(elt if len(elt)>3 or elt in three_letter_words else None): 1 for elt in words}
merge = {elt: words.get(elt, 0) + mergeTarget.get(elt, 50) for elt in words or mergeTarget}
#
print("Merged dictionary is: ", merge, "\n\n Set aside: ", set_aside)
