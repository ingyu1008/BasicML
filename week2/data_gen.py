from random import random
from numpy import random as rd
from math import sin

train = open("train_data.txt", "w")
val = open("val_data.txt", "w")
train_multi = open("train_data_multi.txt", "w")
val_multi = open("val_data_multi.txt", "w")


# initial variables
train_data_size = 200
val_data_size = 200
feature_size = 1
coef = [rd.uniform(-50000,50000)] + [rd.normal(0, 50) for _ in range(feature_size)]
feature_size_multi = 5
coef_multi = [rd.uniform(-50000,50000)] + [rd.normal(0, 50)
                                      for _ in range(feature_size_multi)]


# return inner prod of coef and X with random uniformly distributed noise
def get_y(X, coef, noise_function):
    y = 0
    for i in range(len(X)):
        y += X[i] * coef[i]
    return y + noise_function(sum(X))*rd.normal(0, 60000)


# make data
train_data = []
for __ in range(train_data_size):
    data = [random()*10000 for _ in range(feature_size)]
    train_data.append(
        data + [get_y([1]+data, coef, lambda x: sin(x))])

val_data = []
for __ in range(val_data_size):
    data = [random()*10000 for _ in range(feature_size)]
    val_data.append(data + [get_y([1]+data, coef, lambda x: 0)])

train_data_multi = []
for __ in range(train_data_size):
    data = [random()*10000 for _ in range(feature_size_multi)]
    train_data_multi.append(
        data + [get_y([1]+data, coef_multi, lambda x: sin(x))])

val_data_multi = []
for __ in range(val_data_size):
    data = [random()*10000 for _ in range(feature_size_multi)]
    val_data_multi.append(data + [get_y([1]+data, coef_multi, lambda x: 0)])


# print data
for i in train_data:
    s = ""
    for j in i:
        s += str(j) + " "
    train.write(s.rstrip() + "\n")

for i in val_data:
    s = ""
    for j in i:
        s += str(j) + " "
    val.write(s.rstrip() + "\n")

for i in train_data_multi:
    s = ""
    for j in i:
        s += str(j) + " "
    train_multi.write(s.rstrip() + "\n")

for i in val_data_multi:
    s = ""
    for j in i:
        s += str(j) + " "
    val_multi.write(s.rstrip() + "\n")
