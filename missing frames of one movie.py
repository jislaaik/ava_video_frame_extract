import cv2
import pandas as pd
import os 

speaker_dir = "/home/cordesm/Documents/asc/missvid/a5mEmM6w_ks"
df = pd.read_csv ('/home/cordesm/Desktop/export_dataframe.csv')
#print (df.head())

x = df.loc[df['a'] == 'a5mEmM6w_ks'].b.tolist()

for i in x:
    vidcap = cv2.VideoCapture("/home/cordesm/Documents/asc/a5mEmM6w_ks.mp4")
    vidcap.set(cv2.CAP_PROP_POS_MSEC, i*1000)
    success,image = vidcap.read()
    if success:
        cv2.imwrite(os.path.join(speaker_dir, str(i)+'.jpg'), image)