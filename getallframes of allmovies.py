import cv2
import pandas as pd
import os 

df1 = pd.read_csv ('/home/cordesm/Desktop/gt.csv')
movies = os.listdir('/home/cordesm/Documents/movies')
speaker_dir = "/home/cordesm/Documents/asc/missvid/"
vid_dir = "/home/cordesm/Documents/movies/"
#x = df.loc[df['a'] == 'a5mEmM6w_ks'].b.tolist()
#x = df.loc[df['a'] == 'l.split('.')[0]'].b.tolist()
#x = df.loc[df['a'] == l.split('.')[0]].b.tolist()

df = (df1.a.unique())
movies2 = [x for x in movies if any(b in x for b in df)]

for l in movies2:
    if not os.path.exists(l.split('.')[0]):
        os.makedirs(l.split('.')[0])
    speaker_dir2 = os.path.join(speaker_dir, l.split('.')[0])
    frames = df1.loc[df1['a'] == l.split('.')[0]].b.tolist()
    vidcap = cv2.VideoCapture(os.path.join(vid_dir + l))

    for j in frames:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, j*1000)
        success,image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(speaker_dir2, str(j)+'.jpg'), image)
