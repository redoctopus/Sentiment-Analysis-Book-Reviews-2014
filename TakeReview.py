## Jocelyn Huang
## 10/29/2013
## Take in Review and Give Rating Guess
import RemovePunctuation

def getRating(review, dictionary):
    review = RemovePunctuation.removePunctuation(review)
    print("Punct removed: ", review) # For testing
    
