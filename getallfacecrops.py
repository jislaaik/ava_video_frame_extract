import cv2
import numpy as np
import pandas as pd
import os
import csv


df1 = pd.read_csv ('/home/cordesm/Desktop/gt.csv') #only used to get the 27 missing videos
movies = os.listdir('/home/cordesm/Desktop/videos') #all movies to iterate through
frames_path = "/home/cordesm/Desktop/frames_train" #directory of my frames folders
ava_csv = '/home/cordesm/Desktop/ava_activespeaker_train_augmented.csv'
save_dir = "/home/cordesm/Desktop/faces"

#df = (df1.a.unique())
#movies2 = [xl for xl in movies if any(b in xl for b in df)] #list of all 27 movies with ending e.g. mp4
#print(movies2)

noi = [] #list of all 27 movies
for l in movies:
    lel = l.split('.')[0]
    noi.append(lel)
#print(noi)

def csv_to_list(csv_path):
    as_list = None
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        as_list = list(reader)
    return as_list


csv_data = csv_to_list(ava_csv)


csv_data.pop(0)
for row in csv_data:
    if row[0] in noi:
        x1 = float(row[2])
        y1 = float(row[3])
        x2 = float(row[4])
        y2 = float(row[5])
        ent_id = row[7]

        video = row[0]
        timestamp = row[1]
        if '.' not in timestamp:
            timestamp = timestamp+'.0'

        frame = os.path.join(frames_path, video, timestamp+'.jpg')

        if not os.path.exists((os.path.join(save_dir, ent_id))):
                os.makedirs((os.path.join(save_dir, ent_id)))

        im = cv2.imread(frame)

        h_im = np.size(im, 0)
        w_im = np.size(im, 1)

        crop_x1 = int(x1 * w_im)
        crop_y1 = int(y1 * h_im)
        crop_x2 = int(x2 * w_im)
        crop_y2 = int(y2 * h_im)

        img1 = im[crop_y1:crop_y2, crop_x1:crop_x2, :]

        cv2.imwrite(os.path.join(save_dir, ent_id, timestamp+'.jpg'), img1)


