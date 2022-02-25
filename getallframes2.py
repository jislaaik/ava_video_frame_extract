import cv2
import pandas as pd
import os 

df1 = pd.read_csv ('/home/cordesm/Desktop/ava_activespeaker_train_augmented.csv')
movies = os.listdir('/home/cordesm/Desktop/videos')
speaker_dir = "/home/cordesm/Desktop/frames_train/"
vid_dir = "/home/cordesm/Desktop/videos/"
#x = df.loc[df['a'] == 'a5mEmM6w_ks'].b.tolist()
#x = df.loc[df['a'] == 'l.split('.')[0]'].b.tolist()
#x = df.loc[df['a'] == l.split('.')[0]].b.tolist()

df = (df1.video_id.unique())
movies2 = [x for x in movies if any(b in x for b in df)]

for l in movies2:
    if not os.path.exists(os.path.join(speaker_dir, l.split('.')[0])):
        os.makedirs((os.path.join(speaker_dir, l.split('.')[0])))
    speaker_dir2 = os.path.join(speaker_dir, l.split('.')[0])
    frames = df1.loc[df1['video_id'] == l.split('.')[0]].frame_timestamp.tolist()
    vidcap = cv2.VideoCapture(os.path.join(vid_dir + l))

    for j in frames:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, j*1000)
        success,image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(speaker_dir2, str(j)+'.jpg'), image)