import numpy as np

from sklearn.cluster import KMeans


with open('places.txt', 'r') as f:
    places = f.readlines()
    
arr = []
for line in places:
    x1 = float(line.split(',')[0])
    x2 = float(line.split(',')[1])
    arr.append([x1, x2])

X = np.array(arr)
kmeans = KMeans(n_clusters=3, init='k-means++').fit_predict(X)

i = 0
for item in kmeans:   
    print i, item
    i += 1
