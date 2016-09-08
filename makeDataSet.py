import csv
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D

datasheet = open("Recordings_8_AndroidWatch_BioHarness_0907.csv", "rb")
csvReader = csv.reader(datasheet)
dataset = []

for row in csvReader:
    for i in range(0, len(row)):
        row[i] = float(row[i])
    dataset.append(row[2:])

temp = []
counter = 0
clusterdataset = []
for i in range(0, len(dataset)):
    temp.append(dataset[i][1:])
    counter = counter + 1

    if counter == 10:
        clusterdataset.append(temp)
        counter = 0
        temp = []

'''
for i in range(0,len(clusterdataset)):
    print i, " : ", clusterdataset[i], "\n"
'''

centroid = []
for instance in clusterdataset:
    x = 0
    y = 0
    z = 0
    for i in range(0, len(instance)):
        x += instance[i][0]
        y += instance[i][1]
        z += instance[i][2]
    centroid.append([x/len(instance),y/len(instance),z/len(instance)])

for i in range(0,len(centroid)):
    print i, " : " , centroid[i] # ~ 34 still, 36~ walk

dest = open("centroid.csv", "wb")
writer = csv.writer(dest, delimiter=',')
writer.writerow(['Acc_x','Acc_y', 'Acc_z', 'y'])
counter = 0
for row in centroid :
    if 0 <= counter <= 35:
        y = "still"
    else:
        y = "walk"
    row.append(y)
    writer.writerow(row)
    counter= counter+1