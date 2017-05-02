import json
from nltk.tokenize import sent_tokenize

class parser:
    Topic = ''
    sentences = []
    file_name = ""
    hotel_name = ""
    hotel_id = 0


    with open('semantics.json') as semantics_file:
        semantics = json.load(semantics_file)
    semantics_file.close

    posWords = [semantics['positive'][i]['phrase'] for i in range(len(semantics['positive']))]
    posVals = [semantics['positive'][i]['value'] for i in range(len(semantics['positive']))]

    intensifiers = [semantics['intensifier'][i]['phrase'] for i in range(len(semantics['intensifier']))]
    intensifierVals = [semantics['intensifier'][i]['multiplier'] for i in range(len(semantics['intensifier']))]

    negWords = [semantics['negative'][i]['phrase'] for i in range(len(semantics['negative']))]
    negVals = [semantics['negative'][i]['value'] for i in range(len(semantics['negative']))]

    topic_list = [['lunch', 'food', 'dinner', 'breakfast','restaurant','eat', 'bar'],\
                  ['staff', 'personnel', 'work froce', 'workers','concierge']]


    def __init__(self, file_name, topic):
        parser.file_name = file_name
        parser.Topic = topic
        parser.sentences = []

    def analysis(self, sentences, total_count):
        posCnt = 0
        negCnt = 0
        for sentence in sentences:
            score = 0
            words = sentence.strip().split()
            multiplier = 1
            for word in words:
                if word in parser.intensifiers:
                    multi = parser.intensifiers.index(word)
                    multiplier = parser.intensifierVals[multi]
                    # print "multiplier: ",word," value: ", multiplier
                elif word in parser.posWords:
                    i = parser.posWords.index(word)
                    val = parser.posVals[i]
                    score += val * multiplier
                    multiplier = 1
                elif word in parser.negWords:
                    i = parser.negWords.index(word)
                    val = parser.negVals[i]
                    score -= val * multiplier
                    multiplier = 1
                else:
                    multiplier = 1
            if score > 0:
                posCnt = posCnt + 1
            else:
                negCnt = negCnt + 1
        # return score
        #print "pos count: ", posCnt
        #print "neg count: ", negCnt
        return posCnt, negCnt

    def topic_finder(self):
        for l in self.topic_list:
            if self.Topic in l:
                return l

    def sent_token(self, tokens):
        topics = self.topic_finder()
        for sentence in tokens:
            not_letters_or_numbers = u"!,.?()-'$"
            table = dict((ord(char), u' ') for char in not_letters_or_numbers)
            token = sentence.translate(table)
            for key_word in topics:
                if key_word in token:
                    self.sentences.append(token)
                    break



    def getReviews(self):
        with open('D:/MS/NLP Case Study/Data/'+self.file_name, "r") as data_file:
            data = json.load(data_file)
        info = data['HotelInfo']
        self.hotel_id = info['HotelID']
        print "Hotel ID: ", self.hotel_id
        reviews = data['Reviews']
        data_file.close
        for review in reviews:
            content = review['Content']
            tokens = sent_tokenize(content)
            tokens = [t.lower() for t in tokens]
            self.sent_token(tokens)

