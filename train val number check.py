import pandas as pd
import os

df = pd.read_csv ('/home/cordesm/Documents/asc/ava_activespeaker_val_augmented.csv')
lost = pd.read_csv ('/home/cordesm/Desktop/export_dataframe.csv')

list = lost.a.unique().tolist()

for i in list:
    times = df.loc[df['video_id'] == i].frame_timestamp
    times2 = lost.loc[lost['a'] == i].b.tolist()
    #print(len(times.unique()))
    #print(len(times2))
    print(os.path.join("In " + str(i) + " there are " + str(len(times.unique())) + " unique and total: " + str(len(times))))