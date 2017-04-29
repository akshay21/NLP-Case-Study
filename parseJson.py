import json
import string
import nltk
from nltk.tokenize import sent_tokenize
from pprint import pprint

with open('semantics.json') as semantics_file:
    semantics=json.load(semantics_file)

with open('reviews1.json') as data_file:
    data =json.load(data_file)

review= data["Reviews"][1]["Content"]
not_letters_or_numbers=u'!,.?()'
table=dict((ord(char),u' ')for char in not_letters_or_numbers)




#print table
#table=string.maketrans('.',' ')
'''print review
#review.strip().split()
rv1=review.translate(table)
print rv1.strip().split()

rv1=[w.lower() for w in rv1]

print "rv1:",rv1
tokens= nltk.wordpunct_tokenize(review)
print "tokens:",tokens

for token in tokens:
    if token in semantics['positive']:
        print semantics['positive']['value']'''


