import os, os.path
import csv

fold = (os.listdir('/home/cordesm/Desktop/faces'))
#print len([name for name in os.listdir('.') if os.path.isfile(name)])
#print(len(fold))

lis = []
for i in fold:
    lis.append(len(os.listdir(os.path.join('/home/cordesm/Desktop/faces', i))))

print(sum(lis))

file = open("/home/cordesm/Desktop/ava_activespeaker_train_augmented.csv")
reader = csv.reader(file)
lines= len(list(reader))

print(lines)