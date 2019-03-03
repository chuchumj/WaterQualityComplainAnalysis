# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 06:14:45 2019

@author: Jane
"""

import csv
import matplotlib.pyplot as plt

# opening file path and reading the data into an array
data = open( r"C:\Users\Jane\Desktop\Courses\FinalsProject\DataForProject\Water\Water_Quality_complaints.csv", encoding = "utf8")
data_rows = [i for i in csv.reader(data)][1:] 
complains = [ data_rows[i][6] for i in range(len(data_rows))]

# the complain classes are extracted and counted 
#A dictionary is used to hold the complain classes together with their counts
complain_class_value = {}
count = 1
for i in range(len(complains)):
    for j in range(len(complains[i])):
        if complains[i][j] == "Q" :
            k = len(complains[i])-1
            if complains[i][j:k] not in complain_class_value:                
                complain_class_value[complains[i][j:k]] = count
            else:
                complain_class_value[complains[i][j:k]] += 1
                
print(complain_class_value)              

# putting the classes and the counts in an array to be used for pie chart for visualization of the data distribution     
complain_class = []
complain_value = []
for i,j in complain_class_value.items():
    complain_class.append(i)
    complain_value.append(j)


#ploting a pie chat to visualize our classes and thier distribution
plt.title("complain type with counts")
plt.axis([0,len(complain_class), 0,2000])
plt.xlabel("classes of complains")
plt.ylabel("class counts")
plt.plot(complain_class,complain_value)


#writing the results to csv file
with open(r"C:\Users\Jane\Desktop\Courses\FinalsProject\DataForProject\Water\water_Complain_Classes_Values.csv", "w", newline = "") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(complain_class)
    writer.writerow(complain_value)


 
     
 
    
    









