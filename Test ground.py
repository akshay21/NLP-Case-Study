import json
import nltk
import string
from nltk.tokenize import word_tokenize,sent_tokenize,wordpunct_tokenize


not_letters_or_numbers=u'!,.?()'
table=dict((ord(char),u' ')for char in not_letters_or_numbers)

# def content_token(content):
#     #content_tokens=content.tokenized()
#     content_sent=content.translate(table)
#     print "content_tokens :",content_sent
#     tokens=word_tokenize(content_sent)
#     print "tokens: ",tokens

with open('semantics.json') as semantics_file:
    semantics=json.load(semantics_file)

print "len: ", len(semantics['positive'])
posWords= [semantics['positive'][1]['phrase']]
for pos in posWords:
    print pos

'''li=[['lunch','food','dinner'],['staff','personnel']]
for l in li:
    if 'lunch' in l :
        print l'''


'''for phrase in posWords:
    if 'good' in phrase['phrase']:
        print phrase['value']
        break
    else: print "no good word"'''
#print posWords

#with open('reviews1.json') as data_file:
#    data =json.load(data_file)

#data_file.close

#tokens=tokenize(data_file)

#print tokens


'''reviews=data['Reviews']

for review in reviews:
    not_letters_or_numbers = u'!,.?()'
    table = dict((ord(char), u' ') for char in not_letters_or_numbers)
    content=review['Content'].translate(table)
    tokens=wordpunct_tokenize(content)
    tokens=[w.lower() for w in tokens]
    print "tokens: ", tokens
    
    
    #print "content: ",content
    #content_token(content)'''
'''for review in reviews:
    print review['Content']'''




