import pandas as pd 
from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

def returnSubsetList(attributes):
    available_dataset = ['Basketball', 'Biker', 'Bird1', 'Bird2', 'BlurBody', 'BlurCar1', 
                         'BlurCar2', 'BlurCar3', 'BlurCar4', 'BlurFace', 'BlurOwl', 'Board', 
                         'Bolt', 'Bolt2', 'Box', 'Boy', 'Car1', 'Car2', 'Car24', 'Car4', 
                         'CarDark', 'CarScale', 'ClifBar', 'Coke', 'Couple', 'Coupon', 
                         'Crossing', 'Crowds', 'Dancer', 'Dancer2', 'David2', 'David3', 
                         'Deer', 'Diving', 'Dog', 'Dog1', 'Doll', 'DragonBaby', 'Dudek', 
                         'FaceOcc1', 'FaceOcc2', 'Fish', 'FleetFace', 'Football', 'Freeman1', 
                         'Girl', 'Girl2', 'Gym', 'Human2', 'Human3', 'Human4', 'Human5', 
                         'Human6', 'Human7', 'Human8', 'Human9', 'Ironman', 'Jogging', 'Jogging2', 
                         'Jump', 'Jumping', 'KiteSurf', 'Lemming', 'Liquor', 'Man', 'Matrix', 
                         'Mhyang', 'MotorRolling', 'MountainBike', 'Panda', 'RedTeam', 'Rubik', 
                         'Shaking', 'Singer1', 'Singer2', 'Skater', 'Skater2', 'Skating1', 'Skating2', 
                         'Skiing', 'Soccer', 'Subway', 'Surfer', 'Suv', 'Sylvester', 'Tiger1', 'Tiger2', 
                         'Toy', 'Trans', 'Trellis', 'Twinnings', 'Vase', 'Walking', 'Walking2', 'Woman']    
    l = []

    if attributes == 'bc':
        file = open('attributes/bc.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'def':
        file = open('attributes/def.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'fm':
        file = open('attributes/fm.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'ipr':
        file = open('attributes/ipr.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'iv':
        file = open('attributes/iv.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'lr':
        file = open('attributes/lr.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'mb':
        file = open('attributes/mb.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'occ':
        file = open('attributes/occ.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l    
    elif attributes == 'opr':
        file = open('attributes/opr.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l     
    elif attributes == 'ov':
        file = open('attributes/ov.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l       
    elif attributes == 'sv':
        file = open('attributes/sv.txt','r')
        subset_list = file.readline().strip().replace(" ", "").split(',')
        file.close()
        for i in subset_list:
            if i in available_dataset:
                l.append(i)
        return l         
    else:
        return []
    
def getSubCategoryStatistics(batch_results_df, tracker, attributes):
    sub_results_df = batch_results_df.loc[batch_results_df[0] == tracker]
    sub_results_in_attr_df = sub_results_df.loc[sub_results_df[1].isin(returnSubsetList(attributes))]
    f_sec_mean = sub_results_in_attr_df[[2,4,6,8,10]].stack().mean()
    f_sec_std = sub_results_in_attr_df[[2,4,6,8,10]].stack().std()
    iou_mean = sub_results_in_attr_df[[3,5,7,9,11]].stack().mean()
    iou_std = sub_results_in_attr_df[[3,5,7,9,11]].stack().std()
    return [f_sec_mean, f_sec_std, iou_mean,iou_std]

    
attr_list = ['bc','def','fm','ipr','iv', 'lr', 'mb', 
             'occ', 'opr', 'ov', 'sv']    
tracker_list = ['TrackerBoosting', 'TrackerCSRT', 'TrackerKCF', 'TrackerMedianFlow', 'TrackerMIL', 'TrackerMOSSE', 'TrackerTLD']
results = [Path('result_batch_1').glob('*/'), 
           Path('result_batch_2').glob('*/'), 
           Path('result_batch_3').glob('*/'), 
           Path('result_batch_4').glob('*/'),
           Path('result_batch_5').glob('*/')]

batch_results = []
batch_results_df = pd.DataFrame()
for pathlist in results:
    batch_result = []
    batch_result_df = pd.DataFrame()
    for path in pathlist:
        path_in_str = str(path)
        if batch_result_df.empty == True:
            
            batch_result_df = pd.read_csv(path_in_str, sep=' |:|<|>|\\\\|', engine='python', usecols=[1,6,7,8], header=None)
        else:
            batch_result_df = pd.concat([batch_result_df, pd.read_csv(path_in_str, sep=' |:|<|>|\\\\|', engine='python', usecols=[1,6,7,8], header=None)],ignore_index=True)
    if batch_results_df.empty == True:
        batch_results_df = batch_result_df
    else:
        batch_results_df = pd.concat([batch_results_df, batch_result_df[batch_result_df.columns[2:4]]], axis=1, ignore_index=True)
       
       
fps_column = [2,4,6,8,10]
batch_results_df[fps_column] = 1 / batch_results_df[fps_column] 
#batch_results_df.to_csv('all_batch.csv',index=False)

for tracker in tracker_list:
    f_sec_mean_list = []
    f_sec_std_list = []
    iou_mean_list = []
    iou_std_list = []
    for attribute in attr_list:
        f_sec_mean, f_sec_std, iou_mean,iou_std = getSubCategoryStatistics(batch_results_df, tracker, attribute)
        f_sec_mean_list.append(f_sec_mean)
        f_sec_std_list.append(f_sec_std)
        iou_mean_list.append(iou_mean)
        iou_std_list.append(iou_std)


    IOU_x_pos = np.arange(len(attr_list))
    IOU = list(iou_mean_list)
    IOU_error = list(iou_std_list)
    fig, ax = plt.subplots(figsize=(10,10))
    
    ax.bar(IOU_x_pos, IOU, yerr=IOU_error, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Intersection of Union')
    ax.set_xticks(IOU_x_pos)
    ax.set_xticklabels(attr_list)
    ax.set_title(str('Intersection of Union For ' + tracker) + ' By Categories')
    ax.yaxis.grid(True)
    
    # Save the figure and show
    plt.tight_layout()
    plt.show()        
        
        
