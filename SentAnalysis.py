import json
import nltk
from nltk.tokenize import wordpunct_tokenize, word_tokenize, sent_tokenize
from google.cloud import language


#Creating semantics
with open('semantics.json') as semantics_file:
    semantics=json.load(semantics_file)

posWords= [semantics['positive'][i]['phrase'] for i in range(len(semantics['positive']))]
posVals=[semantics['positive'][i]['value'] for i in range(len(semantics['positive']))]

intesifiers=[semantics['intensifier'][i]['phrase'] for i in range(len(semantics['intensifier']))]
intesifierVals=[semantics['intensifier'][i]['multiplier'] for i in range(len(semantics['intensifier']))]

lang_client = language.Client()

with open('reviews1.json') as data_file:
    data =json.load(data_file)
info=data['HotelInfo']
hotel_name=info['Name']
print  "Hotel Name: ",hotel_name
reviews=data['Reviews']

topic='breakfast'
pos_count=0
neg_count=0
total_count=0
def topic_finder():
    topic_list=[['lunch','food','dinner','breakfast'],['staff','personnel']]
    for l in topic_list:
        if topic in l :
            return l

sentences=[]

def sent_token(tokens):
    topics = topic_finder()
    #print "topics: ",topics
    for token in tokens:
        not_letters_or_numbers = u"!,.?()-'$"
        table = dict((ord(char), u' ') for char in not_letters_or_numbers)
        token=token.translate(table)
        for key_word in topics:
            if key_word in token:
                sentences.append(token)
                break

for review in reviews:
    content=review['Content']
    tokens=sent_tokenize(content)
    tokens=[token.lower() for token in tokens]
    sent_token(tokens)

for sent in sentences:
    doc = lang_client.document_from_text(sent)
    senti = doc.analyze_sentiment().sentiment
    print "senti.score: ",senti.score
    print "senti.mag: ", senti.magnitude

    '''words=sent.strip().split()
    posCnt=0
    for word in words:
        if word in posWords:
            i = posWords.index(word)
            val = posVals[i]
            print "word: ",word," Value: ", val
        if word in intesifiers:
            multi = intesifiers.index(word)
            multi'''

