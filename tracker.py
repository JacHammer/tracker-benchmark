from imutils.video import VideoStream
from imutils.video import FPS
from compute_iou import ComputeIOU
import argparse
import imutils
import time
import cv2
import glob

# TODO: implement a stream to feed images to trackers

# It should take argument like:
# tracker, a batch of images compiled by openCV, and groundtruth

# It should return things like: 
# IOU accuracy, fps, tracker type


# benchmark a tracker
# arguments:
#  -tracker: an OpenCV tracker or your own tracker class, for OpenCV, the 
#       tracker should be created by "cv2.TrackerGNAME_create()"
#       for other tracker, TODO
#  -img_folder__path: the path to a contineous set of images for benchmarking;
#  -groundtruth_path: the path to groundtruth;
#  -dataset_type: so far the benchmarking only supports VTB, more dataset may
#       be added.
def BenchmarkingTracker(tracker, image_path, groundtruth_path, dataset_type):
    images = [cv2.imread(file) for file in glob.glob(image_path)]
    

    n_image = len(images)
    sum_iou = 0.
    sum_fps = 0.

    init_image = images[0]
    with open(groundtruth_path, 'r') as f:
        init_coord = f.readline().rstrip()
        if ',' in init_coord:
            init_coord = init_coord.split(",")
        else:
            init_coord = init_coord.split()
            
        init_coord = tuple(init_coord)
        init_coord = tuple([int(v_ref) for v_ref in init_coord])       
        

    images_coordinates = open(groundtruth_path, "r")

    tracker.init(init_image, init_coord)
    for image in images:
        
        # get width and height of images
        (H, W) = image.shape[:2]
        # read bbox shape and convert it to tuple
        coord = images_coordinates.readline().rstrip()
        if coord.isspace() == True:
            break
        
        if ',' in coord:
            coord = coord.split(",")
        else:
            coord = coord.split()
            
        coord = tuple(coord)
        coord = tuple([int(v_ref) for v_ref in coord])

        fps = FPS().start()  # initialize fps counter
          # initialize the tracker
        (success, box) = tracker.update(image)  # update tracker with new image

        if success:
            (x, y, w, h) = [int(v) for v in box]
            (ref_x, ref_y, ref_w, ref_h) = [int(v_ref) for v_ref in coord]
            cv2.rectangle(image, (x, y), (x + w, y + h),(0, 255, 0), 2)
            cv2.rectangle(image, (ref_x, ref_y), (ref_x + ref_w, ref_y + ref_h),(0, 0, 0), 2)
            iou = ComputeIOU((x, y, x+w, y+h), (ref_x, ref_y, ref_x + ref_w, ref_y + ref_h))
            sum_iou = sum_iou + iou
        else:
            print("tracking failed: code: " + str(success))
            iou = 0.
            sum_iou = sum_iou + iou

        # update FPS    
        fps.update()
        fps.stop()
        sum_fps = sum_fps + fps.fps()

        info = [
            ("IOU", "{:.2f}".format(iou)),
            ("Tracker", str(tracker)),
            ("Success", "Yes" if success else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
        ]	

        # draw info on image
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(image, text, (10, H - ((i * 20) + 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)	

        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        
        
        
        
    # TODO:
    # calculate average IOU
    # calculate average FPS
    # write stats to file
    # f_to_write.write()
    cv2.destroyAllWindows()
    return [sum_fps/n_image, sum_iou/n_image]

'''
TODO for benchmarking procedures:
for tracker in list_of_trackers:
    for dataset in list_of_datasets:
        result = BenchmarkingTracker(tracker, dataset_img, dataset_coord, "idk")
	write results

'''

