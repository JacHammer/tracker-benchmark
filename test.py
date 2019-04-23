from pathlib import Path
from tracker import BenchmarkingTracker
import cv2
import glob

groundtruth_path = "dataset\VTB\Basketball\Basketball\groundtruth_rect.txt"
image_path = 'dataset\VTB\Basketball\Basketball\img\*jpg'

images = [cv2.imread(file) for file in glob.glob(image_path)]
images_coordinates = open(groundtruth_path, "r")


init_img = images[0]
init_coord = images_coordinates.readline().rstrip()


if ',' in init_coord:
    init_coord = init_coord.split(",")
else:
    init_coord = init_coord.split()
    
init_coord = tuple(init_coord)
init_coord = tuple([int(v_ref) for v_ref in init_coord])
