import json
from nltk.tokenize import sent_tokenize
from google.cloud import language


#Creating semantics
with open('semantics.json') as semantics_file:
    semantics = json.load(semantics_file)

posWords = [semantics['positive'][i]['phrase'] for i in range(len(semantics['positive']))]
posVals = [semantics['positive'][i]['value'] for i in range(len(semantics['positive']))]

intensifiers = [semantics['intensifier'][i]['phrase'] for i in range(len(semantics['intensifier']))]
intensifierVals = [semantics['intensifier'][i]['multiplier'] for i in range(len(semantics['intensifier']))]

lang_client = language.Client()

with open('reviews1.json') as data_file:
    data = json.load(data_file)
info = data['HotelInfo']
hotel_name = info['Name']
print "Hotel Name: ",hotel_name
reviews = data['Reviews']

topic = 'breakfast'
pos_count = 0
pos_val = 0.0
neg_count = 0
neg_val = 0.0
total_count = 0

def topic_finder():
    topic_list = [['lunch','food','dinner','breakfast'],['staff','personnel']]
    for l in topic_list:
        if topic in l :
            return l

sentences=[]

def sent_token(tokens):
    topics = topic_finder()
    for sentence in tokens:
        not_letters_or_numbers = u"!,.?()-'$"
        table = dict((ord(char), u' ') for char in not_letters_or_numbers)
        token = sentence.translate(table)
        for key_word in topics:
            if key_word in token:
                sentences.append(token)
                break

for review in reviews:
    content = review['Content']
    tokens = sent_tokenize(content)
    tokens = [t.lower() for t in tokens]
    sent_token(tokens)

for sentence in sentences:
    print sentence
    words = sentence.strip().split()
    posCnt = 0
    multiplier = 1
    for word in words:
        if word in intensifiers:
            multi = intensifiers.index(word)
            multiplier = intensifierVals[multi]
            print "multiplier: ",word," value: ", multiplier
        elif word in posWords:
            i = posWords.index(word)
            val = posVals[i]
            pos_val = val*multiplier
            print "positive word: ",word," value: ", pos_val
            pos_count = pos_count + 1
            #print "positive count: ", pos_count
            total_count= total_count + 1
            #print "Total count: ", total_count

