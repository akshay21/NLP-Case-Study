from Reviews import parser
from nltk import sent_tokenize

file_list = ["reviews1.json","reviews2.json","reviews3.json","reviews4.json","reviews5.json"]

topic="breakfast"

print "list len: ",len(file_list)

results =[]

def cal(hotelId, pos_count, neg_count):
    rating=float(pos_count)/float(pos_count+neg_count)
    tmp={'hotelID': hotelId, 'pos_count':pos_count, 'neg_count':neg_count, 'rating': rating}
    results.append(tmp)


for file in file_list:
    temp=parser(file,topic)
    temp.getReviews()
    pos,neg=temp.analysis(parser.sentences,0)
    rating = float(pos) / float(pos + neg)
    cal(temp.hotel_id, pos, neg, rating)

print "Results: ", results

max_rating=0.0
best_hotel=0
for result in results:
    if result['rating'] > max_rating:
        best_hotel = result['hotelID']
        max_rating=rating
print best_hotel,"is the best hotel for the topic: ",topic, "with rating of", max_rating, "out of 1"



