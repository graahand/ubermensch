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
| pangolin build successfull                                                                                                                                                                                           |      |
| building orb_slam3 as well, let's see what's happens, it successfully built i think, let's test it.                                                                                                                  |      |
|                                                                                                                                                                                                                      |      |

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

| libglew-dev      | opengl extension wrangler library for pangolin 3d visualization |
| ---------------- | --------------------------------------------------------------- |
| cmake            | configure, generate and manage builds                           |
| libeigen3-dev    | high performance C++ maths library for linear algebra           |
| ffmpeg           | multimedia framework for video/audio/decoding/encoding          |
| libdc1394-22-dev | library for IEEE 1394 digital cameras                           |
|                  |                                                                 |


1. **building from source basically means creating executable binaries from the human written source code**
2. cmake isn't compiler rather build system generator which creates the instructions for actual compiler like gcc. 
3. make and ninja are build tools that bulds the project based on Makefile, the Makefile is generated by cmake, a build system generator. 
su

git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
./scripts/install_prerequisites.sh recommended
mkdir build && cd build
cmake ..
cmake --build .
sudo make install
sudo ldconfig


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
* then build with 
* but before below instructions, for jazzy we need to Fix `.h` → `.hpp` includes in `cv_bridge` automatically before build, as this cause a headache
```
		#!/bin/bash
set -e  # stop if any command fails

# 1️⃣ Source ROS 2 Jazzy environment
echo "[INFO] Sourcing ROS 2 Jazzy..."
source /opt/ros/jazzy/setup.bash

# 2️⃣ Set ORB_SLAM3 root directory
export ORB_SLAM3_ROOT_DIR="/home/museum/ORB_SLAM3"

# 3️⃣ Go to your workspace
cd ~/colcon_ws_museum

# 4️⃣ Optional: fix cv_bridge header includes (.h -> .hpp)
echo "[INFO] Fixing cv_bridge headers..."
find src/orbslam3_ros2 -type f -name "*.cpp" -o -name "*.hpp" -o -name "*.h" \
    | xargs sed -i 's|<cv_bridge/cv_bridge.h>|<cv_bridge/cv_bridge.hpp>|g'

# 5️⃣ Build the orbslam3 package
echo "[INFO] Building orbslam3..."
colcon build --symlink-install --packages-select orbslam3

# 6️⃣ Source the workspace so ROS can find the package
echo "[INFO] Sourcing local workspace..."
source install/setup.bash

echo "[SUCCESS] orbslam3 build finished!"

```
* add this line to the CMakeLists.txt file: find_package(OpenCV REQUIRED)
* builld the sophus as well: 
* cd ~/ORB_SLAM3/Thirdparty/Sophus
	cmake -DBUILD_TESTS=OFF .
	make
	sudo make install
	(**Skip building tests**)
	* ls /usr/local/include/sophus/se3.hpp
* $ cd ~/colcon_ws, colcon build --symlink-install --packages-select orbslam3

### how to use?
 * source ~/colcon_ws/install/local_setup.bash
 * then run the orbslam mode, among (mono, stereo, rgbd, stereo-inertial)
 * vocabulary and config file can be found here: `orbslam3_ros2/vocabulary/ORBvoc.txt`, `orbslam3_ros2/config/monocular/TUM1.yaml` (vocabulary file is a .txt file that have pre-trained vocabulary for visual features), (.yaml file is a config file that contains camera calibration parameters)
* for mono mode run ( ros2 run orbslam3 mono PATH_TO_VOCABULARY PATH_TO_YAML_CONFIG_FILE)
```
		museum@museum:~/colcon_ws_museum$ ros2 run orbslam3 mono /home/museum/colcon_ws_museum/src/orbslam3_ros2/vocabulary/ORBvoc.txt /home/museum/colcon_ws_museum/src/orbslam3_ros2/config/monocular/TUM1.yaml
```
* for stereo mode (ros2 run orbslam3 stereo PATH_TO_VOCABULARY PATH_TO_YAML_CONFIG_FILE BOOL_RECTIFY)
* for rgbd model (ros2 run orbslam3 rgbd PATH_TO_VOCABULARY PATH_TO_YAML_CONFIG_FILE)

#### now that the robslam mode is ran, we need to integrate the cameras as well for real time slam. 
how to? 
first install ros-foxy-usb-cam package for usb web camera, 
*sudo apt install ros-jazzy-usb-cam*
or instead of usb_cam, v4l2-camera can be installed as well . 

then test the camera node, with *ros2 run usb_cam usb_cam_node_exe* or ros2 run v4l2_camera v4l2_camera_node,

by default it will publish on /image_raw or /camera/image_raw topic. 
list out the topics with: ros2 topic list. 


what is rosbag? 
rosbag is a blackbox flight recorder, in ROS topics are **streams of data**, rosbag is a file that records these streams so they can be replayed them later as if they are coming from the real sensors. 
When you feed a rosbag to ORB-SLAM3, it thinks the data is coming from live cameras

#### what is stereo-inertial mode means?
it means using two cameras (stereo) to get depth information and "IMU" (inertial measurement unit) to measure acceleration and rotation. **fusion of visual and inertial slam** 



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
