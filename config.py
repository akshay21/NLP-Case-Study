# install these packages if not already present.
from Reviews import parser
import numpy as np
import matplotlib.pyplot as plt

#The files with reviews
file_list = ["reviews1.json","reviews2.json","reviews3.json","reviews4.json","reviews5.json"]

#The topic you want search like, breakfast or spa or location
topic=raw_input("Please enter the topic you want to search: ")

results =[]

#Collecting results.
def cal(hotelId, pos_count, neg_count, rating):
    tmp={'hotelID': hotelId, 'pos_count':pos_count, 'neg_count':neg_count, 'rating': rating}
    results.append(tmp)


for file in file_list:
    temp=parser(file,topic)
    temp.getReviews()
    pos,neg=temp.analysis(parser.sentences,0)
    rating = float(pos) / float(pos + neg)
    cal(temp.hotel_id, pos, neg, rating)

print "Results: ", results

""" Finding the best hotel for given topic"""
max_rating=0.0
best_hotel=0
for result in results:
    if result['rating'] > max_rating:
        best_hotel = result['hotelID']
        max_rating=rating
print best_hotel,"is the best hotel for the topic: ",topic, "with rating of", max_rating, "out of 1"


""" Ploting graph for better understanding of the results"""
hotel_list=([result['hotelID'] for result in results])
y_pos= np.arange(len(hotel_list))
ratings=[result['rating'] for result in results]

plt.bar(y_pos,ratings, align='center', alpha=0.5)
plt.xticks(y_pos,hotel_list)
plt.xlabel('Hotel IDs')
plt.ylabel('Hotel Rating')
plt.title(' Hotel ratings comparision')

plt.show()