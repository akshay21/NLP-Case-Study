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

    # Creating a list of positive words from given semantics.
    posWords = [semantics['positive'][i]['phrase'] for i in range(len(semantics['positive']))]
    posVals = [semantics['positive'][i]['value'] for i in range(len(semantics['positive']))]

    # Creating a list of intensifiers from given semantics.
    intensifiers = [semantics['intensifier'][i]['phrase'] for i in range(len(semantics['intensifier']))]
    intensifierVals = [semantics['intensifier'][i]['multiplier'] for i in range(len(semantics['intensifier']))]

    # Creating a list of negative words from given semantics.
    negWords = [semantics['negative'][i]['phrase'] for i in range(len(semantics['negative']))]
    negVals = [semantics['negative'][i]['value'] for i in range(len(semantics['negative']))]

    '''This is the topics list with possible synonyms or words connected with topic in general.
       It is not exhaustive as if now but we can add words to to make our results more accurate.'''
    topic_list = [['lunch', 'food', 'dinner', 'breakfast','restaurant','eat', 'bar'],\
                  ['staff', 'personnel', 'work froce', 'workers','concierge']]

    #Constructor
    def __init__(self, file_name, topic):
        parser.file_name = file_name
        parser.Topic = topic
        parser.sentences = []

    #Method to analyze each sentence that contains a word from the topic list and determine its score.
    def analysis(self, sentences, total_count):
        posCnt = 0
        negCnt = 0
        for sentence in sentences:
            score = 0
            #Splitting the sentence into words.
            words = sentence.strip().split()
            multiplier = 1
            for word in words:
                #Checking if the word is an intensifier or a positive word or a negative word.
                if word in parser.intensifiers:
                    multi = parser.intensifiers.index(word)
                    multiplier = parser.intensifierVals[multi]
                    # print "multiplier: ",word," value: ", multiplier
                elif word in parser.posWords:
                    i = parser.posWords.index(word)
                    val = parser.posVals[i]
                    score += val * multiplier #Calculating score for each sentence.
                    multiplier = 1
                elif word in parser.negWords:
                    i = parser.negWords.index(word)
                    val = parser.negVals[i]
                    score -= val * multiplier
                    multiplier = 1
                else:
                    multiplier = 1
            #Determining the sentiment in the sentence by checking the score value.
            if score > 0:
                posCnt = posCnt + 1
            else:
                negCnt = negCnt + 1
        #We can also return accumilated score for each hotel
        #return score
        #print "pos count: ", posCnt
        #print "neg count: ", negCnt
        return posCnt, negCnt

    #A method to find the list of topics that closely matchhes with the given topic.
    def topic_finder(self):
        for l in self.topic_list:
            if self.Topic in l:
                return l

    #A method to tokenize each review into sentences.
    #It also collects all the sentences that have a word from the topic list in it.
    #By doing this we only process those sentences which talk about the given topic.
    def sent_token(self, tokens):
        topics = self.topic_finder()
        for sentence in tokens:
            #removing special characters from each sentence.
            not_letters_or_numbers = u"!,.?()-'$"
            table = dict((ord(char), u' ') for char in not_letters_or_numbers)
            token = sentence.translate(table)
            for key_word in topics:
                if key_word in token:
                    self.sentences.append(token)
                    break

    #A method which reads a json file and processes reviews for further processing.
    def getReviews(self):
        with open('D:/MS/NLP Case Study/Data/'+self.file_name, "r") as data_file:
            data = json.load(data_file)
        info = data['HotelInfo']
        self.hotel_id = info['HotelID']
        reviews = data['Reviews']
        data_file.close
        for review in reviews:
            content = review['Content']
            tokens = sent_tokenize(content)
            tokens = [t.lower() for t in tokens]
            self.sent_token(tokens)

