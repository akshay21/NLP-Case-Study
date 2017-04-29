import json
import nltk
from nltk.tokenize import wordpunct_tokenize, word_tokenize, sent_tokenize
import string

with open('semantics.json') as semantics_file:
    semantics=json.load(semantics_file)

with open('reviews1.json') as data_file:
    data =json.load(data_file)
info=data['HotelInfo']
hotel_name=info['Name']
print  "Hotel Name: ",hotel_name
reviews=data['Reviews']

for review in reviews:
    not_letters_or_numbers = u'!,.?()'
    table = dict((ord(char), u' ') for char in not_letters_or_numbers)
    content=review['Content'].translate(table)
    tokens=sent_tokenize(content)
    tokens=[w.lower() for w in tokens]
    print "tokens: ", tokens