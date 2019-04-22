from pathlib import Path
from tracker import BenchmarkingTracker
import cv2



OPENCV_OBJECT_TRACKERS = {


    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create,
            }
source_path = Path("dataset/VTB")   

# TODO: prepare file to write stats
for i in OPENCV_OBJECT_TRACKERS:
    for abs_path in source_path.glob("*"):
        tracker = OPENCV_OBJECT_TRACKERS[i]()
        tracker_name = str(tracker).split()[0][1:]
        
        f_to_write = open(tracker_name, 'a')
        for a in abs_path.glob("*/*/"):
            if a.is_dir():
                img_dir = str(a) + "\*jpg"
                print(img_dir)
            if a.match('*.txt'):
                img_groundtruth_coords = str(a)
                print(img_groundtruth_coords)
        
        results = BenchmarkingTracker(tracker, img_dir, img_groundtruth_coords, "idk")
        print(results)    
        f_to_write.write(str( str(tracker) + ' ' + str(abs_path) + ' ' + str(results[0]) + ' ' + str(results[1]) + '\n'  ))
        f_to_write.close()    
    



    
