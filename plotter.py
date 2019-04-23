
import pandas as pd 

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

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

        df = pd.read_csv(path_in_str, sep=' |:|<|>|', engine='python', usecols=[1,4,5,6], header=None)
        # df = pd.read_csv(path_in_str, sep=' |:|<|>|\\\\|', engine='python', usecols=[1,6,7,8], header=None)
        tracker_name =  df[df.columns[0]][0]
        dataset_name = df[df.columns[1]]
        tracker_fps = df[df.columns[2]]
        tracker_iou = df[df.columns[3]]
        avg_tracker_time = 1/ tracker_fps.sum() 

        avg_tracker_iou = tracker_iou.sum() / 95
        batch_result.append(list([tracker_name , str(avg_tracker_time) , str(avg_tracker_iou)]))
    batch_results.append(batch_result)

batch_results_df = pd.DataFrame()
counter = 0
for batch_result in batch_results:
    if batch_results_df.empty == True:
        
        batch_results_df = pd.DataFrame(batch_result)
        batch_results_df.columns = [str('name'), str('f_sec_' + str(counter)), str('iou_' + str(counter))]
    else:

        batch_result_df = pd.DataFrame(batch_result)
        batch_result_df.columns = [str('name'), str('f_sec_' + str(counter)), str('iou_' + str(counter))]
        batch_results_df = pd.concat([batch_results_df, batch_result_df], axis=1, sort=False)
    counter = counter + 1

iou_df = batch_results_df[['iou_0','iou_1','iou_2','iou_3','iou_4']].copy().astype(float)
f_sec_df = batch_results_df[['f_sec_0','f_sec_1','f_sec_2','f_sec_3','f_sec_4']].copy().astype(float)


iou_mean = iou_df[['iou_0','iou_1','iou_2','iou_3','iou_4']].mean(axis=1)
f_sec_mean = f_sec_df[['f_sec_0','f_sec_1','f_sec_2','f_sec_3','f_sec_4']].mean(axis=1)

iou_std = iou_df[['iou_0','iou_1','iou_2','iou_3','iou_4']].std(axis=1)
f_sec_std = f_sec_df[['f_sec_0','f_sec_1','f_sec_2','f_sec_3','f_sec_4']].std(axis=1)

print(iou_mean)
print(f_sec_mean)
print(iou_std)
print(f_sec_std)

# plot error bars for IOU
trackers = ['Boosting', 'CSRT', 'KCF', 'MedianFlow', 'MIL', 'MOSSE', 'TLD']
IOU_x_pos = np.arange(len(trackers))
IOU = list(iou_mean)
IOU_error = list(iou_std)
fig, ax = plt.subplots(figsize=(10,10))

ax.bar(IOU_x_pos, IOU, yerr=IOU_error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Intersection of Union')
ax.set_xticks(IOU_x_pos)
ax.set_xticklabels(trackers)
ax.set_title('IOU performance for Trackers')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.show()

f_sec_x_pos = np.arange(len(trackers))
f_sec = list(f_sec_mean)
f_sec_error = list(f_sec_std)
fig, ax = plt.subplots(figsize=(10,10))

ax.bar(f_sec_x_pos, f_sec, yerr=f_sec_error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Frame Time (s)')
ax.set_xticks(f_sec_x_pos)
ax.set_xticklabels(trackers)
ax.set_title('Frame Time For Trackers')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.show()

