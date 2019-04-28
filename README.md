# tracker-benchmark

OpenCV built-in tracker:

Boosting  
CSRT  
~~GOTURN (requres pre-trained model)~~ not been benchmarked due to memory leak  
KCF  
MedianFlow  
MIL  
MOSSE  
TLD  

The benchmarking dataset is from TB-100: http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html  
Only these video sequences are used:
`'Basketball', 'Biker', 'Bird1', 'Bird2', 'BlurBody', 'BlurCar1', 'BlurCar2', 'BlurCar3', 'BlurCar4', 'BlurFace', 'BlurOwl', 'Board', 'Bolt', 'Bolt2', 'Box', 'Boy', 'Car1', 'Car2', 'Car24', 'Car4', 'CarDark', 'CarScale', 'ClifBar', 'Coke', 'Couple', 'Coupon', 'Crossing', 'Crowds', 'Dancer', 'Dancer2', 'David2', 'David3', 'Deer', 'Diving', 'Dog', 'Dog1', 'Doll', 'DragonBaby', 'Dudek', 'FaceOcc1', 'FaceOcc2', 'Fish', 'FleetFace', 'Football', 'Freeman1', 'Girl', 'Girl2', 'Gym', 'Human2', 'Human3', 'Human4', 'Human5', 'Human6', 'Human7', 'Human8', 'Human9', 'Ironman', 'Jogging', 'Jogging2', 'Jump', 'Jumping', 'KiteSurf', 'Lemming', 'Liquor', 'Man', 'Matrix', 'Mhyang', 'MotorRolling', 'MountainBike', 'Panda', 'RedTeam', 'Rubik', 'Shaking', 'Singer1', 'Singer2', 'Skater', 'Skater2', 'Skating1', 'Skating2', 'Skiing', 'Soccer', 'Subway', 'Surfer', 'Suv', 'Sylvester', 'Tiger1', 'Tiger2', 'Toy', 'Trans', 'Trellis', 'Twinnings', 'Vase', 'Walking', 'Walking2', 'Woman'`.

To run the benchmark, run `python3 benchmark.py` in command line.
To generate plots, run `python3 plotter.py`, `attr_sub_plotter.py`, and `tracker_sub_plotter.py`.
