import math
import numpy as np

period = 200
stepSize = 1/period
stepCounts = 5000

X = []
Y = []

for i in range(stepCounts):
    X.append(math.sin(2*math.pi*stepSize*i))
    Y.append(math.cos(math.pi*stepSize*i))

writeFileX = '/home/minh/PycharmProjects/DeepESN/data_backup/Lazy8X'
writeFileY = '/home/minh/PycharmProjects/DeepESN/data_backup/Lazy8Y'

with open(writeFileX,'w') as f:
    for i in range(len(X)-1):
        f.write(str(X[i]) + ',' + str(X[i+1]) + '\n')

with open(writeFileY,'w') as f:
    for i in range(len(Y)-1):
        f.write(str(Y[i]) + ',' + str(Y[i+1]) + '\n')