from pathlib import Path
from tracker import BenchmarkingTracker
import cv2

img_groundtruth_coords = "dataset\VTB\David\David\groundtruth_rect.txt"
img_dir = 'dataset\VTB\David\David\img\*jpg'


tracker = cv2.TrackerCSRT_create()
results = BenchmarkingTracker(tracker, img_dir, img_groundtruth_coords, "idk")
print(results)    

if ',' in coord:
    coord = coord.split(",")
else:
    coord = coord.split()
coord = tuple(coord)
coord = tuple([int(v_ref) for v_ref in coord])


