# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:58:40 2019

@author: Jane
"""
import csv
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt

data_set = open(r"C:\Users\Jane\Desktop\JobSearch\Data Science\DataScienceProject\Tweets.csv",encoding="utf8")
#read the data set excluding the colums
all_tweets_classes = [i for i in csv.reader(data_set)][0:]
all_tweets = all_tweets_classes[1:][:]

#seperate training and testing dataset
partition= int((70/100)*len(all_tweets))
all_training_tweets = all_tweets[0:partition]
training_tweets =[row[0] for row in all_training_tweets]
class_training_tweets = [row[1] for row in all_training_tweets]


all_testing_tweets = all_tweets[partition-1: ]
testing_tweets = [row[0] for row in all_testing_tweets]
class_testing_tweets = [row[1] for row in all_testing_tweets]

#creating a pipeline
pipeline_data = Pipeline(steps = [("vectorizer", TfidfVectorizer(ngram_range =(1,2))), ("classifier", LogisticRegression())])

#visualization of our class distribution
plt.axis([0, 5, 1,10000])
plt.xlabel("Sentiment classes")
plt.ylabel("Frequency")
plt.title("Frequency of sentiment classes")
data = open(r"C:\Users\Jane\Desktop\JobSearch\Data Science\DataScienceProject\Tweets.csv",encoding="utf8")


#since the first string is the column name, access this list by select column 1:end of the list

tweet_data = [i[1] for i in csv.reader(data)][1:]
print(tweet_data[0])
print(len(tweet_data))
tweet_data.sort()
negative =[i for i in tweet_data if i == "negative"]
print(len(negative))
positive =[i for i in tweet_data if i == "positive"]
print(len(positive))
neutral =[i for i in tweet_data if i == "neutral"]
print(len(neutral))
plt.bar(["negative","positive","neutral"],[len(positive),len(neutral),len(negative)])
plt.show()

#training and testing of our model
#as you train, you test.
accuracy_list = [] 
for batch in (20, 50, 100, 500, 1000, 2000, 3000, len(training_tweets)):
    pipeline_data.fit(training_tweets[:batch], class_training_tweets[:batch])
    print("tfidf",pipeline_data.score(testing_tweets,class_testing_tweets))
    accuracy_list.append(pipeline_data.score(testing_tweets,class_testing_tweets))

#Visualiztion of our accuracy of our model
plt.axis([0, len(all_tweets), 0, 1])
plt.xlabel("number of samples")
plt.ylabel("accuracy")
plt.title("Accuracy Graph")
plt.plot([20,50,100, 500, 1000, 2000, 3000, len(training_tweets)], accuracy_list)







