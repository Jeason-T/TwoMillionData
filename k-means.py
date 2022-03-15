import math
import matplotlib.pyplot as plt
import random
import pandas as pd
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(12, 8), facecolor='cornsilk')#窗口大小
m = Basemap()

def getEuclidean(point1, point2):
    dimension = len(point1)
    dist = 0.0
    for i in range(dimension):
        dist += (point1[i] - point2[i]) ** 2
    return math.sqrt(dist)


def k_means(dataset, k, iteration):
    # 初始化簇心向量
    index = random.sample(list(range(len(dataset))), k)
    vectors = []
    for i in index:
        vectors.append(dataset[i])
    # 初始化标签
    labels = []
    for i in range(len(dataset)):
        labels.append(-1)
    # 根据迭代次数重复k-means聚类过程
    while (iteration > 0):
        # 初始化簇
        C = []
        for i in range(k):
            C.append([])
        for labelIndex, item in enumerate(dataset):
            classIndex = -1
            minDist = 1e6
            for i, point in enumerate(vectors):
                dist = getEuclidean(item, point)
                if (dist < minDist):
                    classIndex = i
                    minDist = dist
            C[classIndex].append(item)
            labels[labelIndex] = classIndex
        for i, cluster in enumerate(C):
            clusterHeart = []
            dimension = len(dataset[0])
            for j in range(dimension):
                clusterHeart.append(0)
            for item in cluster:
                for j, coordinate in enumerate(item):
                    clusterHeart[j] += coordinate / len(cluster)
            vectors[i] = clusterHeart
        iteration -= 1
    return C, labels


# 数据集：每三个是一组分别是西瓜的编号，密度，含糖量
data = pd.read_csv(r'D:\qq消息\1459991091\FileRecv\Citibike数据集.csv')
a = pd.DataFrame(data, columns=['start station latitude', 'start station longitude'])

# print(float(a['start station latitude'][0]))
# print(a)
dataset = [[float(a['start station latitude'][i]), float(a['start station longitude'][i])]for i in range(1, 10000)]
C, labels = k_means(dataset, 5, 20)

colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
for i in range(len(C)):
    coo_X = []  # x坐标列表
    coo_Y = []  # y坐标列表
    for j in range(len(C[i])):
        coo_X.append(C[i][j][0])
        coo_Y.append(C[i][j][1])
    # print(coo_X,coo_Y)
    plt.scatter(coo_X,coo_Y, marker='x', color=colValue[i%len(colValue)] ,label=i)
#你也可以根据经纬度标注点

plt.legend(loc='upper right')
plt.show()
print(labels)
