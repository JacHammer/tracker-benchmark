
import pandas as pd 

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

iv = open('attributes/iv.txt','r')
iv_list = iv.readline().rstrip().split(',')
iv.close()

results = [Path('result_batch_1').glob('*/'), 
           Path('result_batch_2').glob('*/'), 
           Path('result_batch_3').glob('*/'), 
           Path('result_batch_4').glob('*/'),
           Path('result_batch_5').glob('*/')]
batch_results = []
for pathlist in results:
    batch_result = []
    for path in pathlist:
        path_in_str = str(path)
        df = pd.read_csv(path_in_str, sep=' |:|<|>|\\\\|', engine='python', usecols=[1,6,7,8], header=None)
        tracker_name =  df[df.columns[0]][0]
        dataset_name = df[df.columns[1]]
        tracker_fps = df[df.columns[2]]
        tracker_iou = df[df.columns[3]]
        avg_tracker_time = 1/ tracker_fps.sum() 

        avg_tracker_iou = tracker_iou.sum() / 95
        batch_result.append(list([tracker_name , str(avg_tracker_time) , str(avg_tracker_iou)]))
    batch_results.append(batch_result)
