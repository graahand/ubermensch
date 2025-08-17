#smarc 
#rnd 

| tested the segmentation by tweaking the value of core parameters and sdc successfully navigated through the track                                                                                                    | 8/13 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| issue regarding the cameras, when display is connected only one of the camera is opened (lane detection or object detection).                                                                                        | 8/13 |
| slam familiraty                                                                                                                                                                                                      | q11  |
| go there once: https://chatgpt.com/c/689c7670-aae8-8326-8841-fea39d2c7153                                                                                                                                            | 8/13 |
| ros2 installation in pc                                                                                                                                                                                              |      |
| installed software-properties-common (success)                                                                                                                                                                       |      |
| added universe repository to the apt(package manager) (success)                                                                                                                                                      |      |
| installed ros2-apt-source package which provides keys and apt source configuration for various ROS repositories                                                                                                      |      |
| install development tools ()                                                                                                                                                                                         |      |
| install ros-jazzy-desktop                                                                                                                                                                                            |      |
| ros2 middleware interface (a abstraction layer that defines how ros2 nodes communicate with each other over the network )                                                                                            |      |
| tested the ros2 talker and listener (it worked properly)                                                                                                                                                             |      |
| now installed ros-jazzy-image-tools for working with camera feed and images                                                                                                                                          |      |
| installed ros-jazzy-rtabmap-ros package for slam based on stereo or monocular camera.                                                                                                                                |      |
| installing rtabmap_ros from source, updating and install rosdep(ros dependency i think)                                                                                                                              |      |
| empy python package required for building, also the anaconda environment needs to be deactivated because ros2 uses its own python environment when building.                                                         |      |
| anaconda is interrrupting the installation and  build process to set the anaconda environment off (conda config --set auto_activate_base false) then source the ROS and then only start the build process. (success) |      |
| the rtabmap_ros is inside ros2_ws directory and needs to source the ros2_ws/intall/setup.bash before running anything related to rtab_ros                                                                            |      |
| installed the camera driver for the usb camera (sudo apt install ros-jazzy0v4l2-camera) then run its camera node.                                                                                                    |      |

## orb_slam3_ros2_wrapper

[slam3](https://github.com/zang09/ORB_SLAM3_ROS2/tree/main)

### requirements are
ubuntu above 20.04
ros2 above foxy
opencv above 4.2.0

### build the pangolin first as it is also another dependency for orb-slam3


sudo apt install libglew-dev cmake libpython3-dev python3-dev \
libeigen3-dev ffmpeg libavcodec-dev libavutil-dev libavformat-dev \
libswscale-dev libdc1394-22-dev libjpeg-dev libpng-dev libtiff-dev libopenexr-dev


git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build && cd build
cmake ..
cmake --build .


sudo make install

then 
### instructions 
build orb_slam3, how to?
* git clone https://github.com/zang09/ORB-SLAM3-STEREO-FIXED.git ORB_SLAM3  (name of the folder where the repo will be cloned)
* then cd ORB_SLAM3
* chmod +x build.sh then run the bash file. 

install related ros2 package
* sudo apt install ros-$ROS_DISTRO-vision-opencv && sudo apt install ros-$ROS_DISTRO-message-filters (allows to synchronize multiple ROS topics)

### building the wrapper 
* mkdir -p colcon_ws/src
* cd ~/colcon_ws/src (src is a source folder where the ros2 packages are placed before building)
* git clone https://github.com/zang09/ORB_SLAM3_ROS2.git orbslam3_ros2 (this wrapper is the "glue" between ROS2 topics and ORB-SLAM3 functions.)
* 
* Change this [line](https://github.com/zang09/ORB_SLAM3_ROS2/blob/ee82428ed627922058b93fea1d647725c813584e/CMakeLists.txt#L5) to your own `python site-packages` path
* Change this [line](https://github.com/zang09/ORB_SLAM3_ROS2/blob/ee82428ed627922058b93fea1d647725c813584e/CMakeModules/FindORB_SLAM3.cmake#L8) to your own `ORB_SLAM3` path (Without this, the wrapper won’t find the ORB-SLAM3 library.)
* then build with ($ cd ~/colcon_ws, colcon build --symlink-install --packages-select orbslam3)

### how to use?
 * source ~/colcon_ws/install/local_setup.bash
 * then run the orbslam mode, among (mono, stereo, rgbd, stereo-inertial)
 * vocabulary and config file can be found here: `orbslam3_ros2/vocabulary/ORBvoc.txt`, `orbslam3_ros2/config/monocular/TUM1.yaml` (vocabulary file is a .txt file that have pre-trained vocabulary for visual features), (.yaml file is a config file that contains camera calibration parameters)
* for mono mode run ( ros2 run orbslam3 mono PATH_TO_VOCABULARY PATH_TO_YAML_CONFIG_FILE)
* for stereo mode (ros2 run orbslam3 stereo PATH_TO_VOCABULARY PATH_TO_YAML_CONFIG_FILE BOOL_RECTIFY)
* for rgbd model (ros2 run orbslam3 rgbd PATH_TO_VOCABULARY PATH_TO_YAML_CONFIG_FILE)

what is rosbag? 
rosbag is a blackbox flight recorder, in ROS topics are **streams of data**, rosbag is a file that records these streams so they can be replayed them later as if they are coming from the real sensors. 
When you feed a rosbag to ORB-SLAM3, it thinks the data is coming from live cameras

#### what is stereo-inertial mode means?
it means using two cameras (stereo) to get depth information and "IMU" (inertial measurement unit) to measure acceleration and rotation. **fusion of visual and inertial slam** 


## stella_vslam_ros with docker  image


| cloned stella-vslam-ros repository                                                                                                                       | t   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| tried to build the docker file (humble-ros based)                                                                                                        |     |
| build failed due to stack trace library (backward-cpp), which was later solved by editing the docker file and adding the build commands for backward-cpp |     |

# slam

simultaneous localization and mapping 
(robot figures out where it is and builds a map of its surrounding at the same time without knowing whereabouts.) SLAM is used for the indoor places or to the places where GPS/BDS doesn't works or too imprecise. 

data capture using Lidar (x), depth camera (x), stereo camera (two cameras capturing same scene, with disparity calculates depth with triangulation) and IMU (gyroscope and accelerometer).

then the landmarks, corners, furnitures are detected via depth.
pose estimated (position) via odometry(collecting data from sensor and estimating the movement) (In visual odometry (VO), camera images track how features move between frames to estimate translation and rotation)

updating the map and loop closure(corrects the drift)

SLAM have different co-ordinate system which starts with arbitary origin (0, 0, 0), then the position of the robot is  estimated relative to that starting origin. 
It’s like saying, “I’m 2 meters to the right of where I started, and 1 meter forward,” not “I’m at 27.6812° N, 85.3240° E.”


## visual slam

monocular slam (single camera)
stereo slam (dual camera side wise side)

https://chatgpt.com/c/689c7670-aae8-8326-8841-fea39d2c7153


## tools and github implementations for visual slam


## Robotics (Navigation, Planning and Control)

perception(slam)-planning(djisktra, a*)-control

slam builds 2d occupancy grids (free space vs obstacles), A* plans the path through the free space. 

slam is not like training a mode on dataset rather updating the map starting from zero, in real time as new sensor data arrives. 

obstacles and free space in stereo slam is estimated using stereo disparity(meaning?)
if a ray from camera hits a surface at certain depth that's obstacle if the ray continues without hitting then its free space. 

stereo disparity means how much the same object appears shifted between the left and right camera images
Using disparity + camera baseline + focal length, we can calculate **depth** using triangulation

ll
Depth=f×Bdisparity\text{Depth} = \frac{f \times B}{\text{disparity}}
- Install ROS2 + SLAM package (e.g., RTAB-Map ROS, ORB-SLAM2 ROS wrapper).
    
- Connect your camera (stereo or RGB-D).
    
- Teleop the car through your defined route → SLAM builds the map.
    
- Save the map (ROS maps can be saved as `.pgm` + `.yaml`).
    
- Reload the map for autonomous runs.

kalman filters for sensor fusion (estimate robot pose from noisy sensors)
