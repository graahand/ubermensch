1. robots vanda bittikai, yesle garnu parne (must) kaam chai DDD(Dangerous, Dull, Dirty) tasks haru automate garnu paryo ani robots haru le context sanga/surrounding sanga interact garerw kei hadh samma, fully automated navayepani decisions haru chai lina saknu paryo, like line following robot.

> [!NOTE] Charles Deguire, Kinova Inc
> But I realized how having anastronaut doing remote  manipulation with a
> space robot arm could be an aberration when people in wheelchairs could not even pour themselves a glass of water alone.

2. Leonardo da vinci le robotics ma pani contribution diyeko xan, jesma usle human anatomy and kinematics lai ramro sanga research garerw, tyo kura haru lai chai automation, robotics ma implement gareko painxa, josko example Leanardo's Fiat vanne automated(self-propelled) cart xa. yesko fully working replica 2006 ma Florence vanne thauma banaiyeko xah. [link](https://en.wikipedia.org/wiki/Leonardo%27s_self-propelled_cart)
3. Vaucanson's Digesting Automated Duck (replicates the actual duck)
4. simulation rw automation ko difference k ho vanda, simulation ma chai just yo kura chalxa kina chalxa thahaxaina, just chalxa. But automation ma chai aim k hunxa vanda robot chalxa vane kasari chalxa? mechanics pani explain garne aim hunxa. 




### 2 sep
flow good xah no gaps in the learning outcomes or the lessons, improvement in the cognitive learning outcomes reviewed, bloom's taxonomy. 

#### 5e ko description: 
> **"Engage is not an interactive activity—someone else (e.g., the teacher) presents something (like a video), and students just observe. Engage sparks _curiosity and connects to prior knowledge_."**  
> **"Explore means a hands-on activity where students interact with materials (e.g., a Robotics Mini-Museum), test ideas, and ask _'how/why did this happen?'_ through guided discovery."**  
> **"Explain means the teacher _and students_ collaboratively clarify concepts (e.g., answering _'How are robots built?'_), moving from exploration to formal understanding."**  
> **"Elaborate means deepening understanding _by applying concepts to new scenarios_ (e.g., building robots with kits or role-playing a robotics team to solve real-world problems)."**  
> **"Evaluate means assessing _how much knowledge transfer occurred_ (e.g., through presentations where students justify solutions, showing they can use concepts beyond the lesson)."**

##### class 8 lesson plan based on project
project: self balancing robot
1. yo robot banauna ko lagi main chaine components haru vaneko euta MPU6050 gyro-accelerometer chainxa, josle chai self balance garna contribute garxa, esp32 board chai as microcontroller use hune vayo, euta motor driver (L298N) and two dc geared motor chainxa. 
2. PID ko concept esma use hunxa kinavane yei concept le self balance garna ko lagi help garxa. 
> 
#### lessons and framework
NOW CRAFT THE CONTENT ACCORDING TO THE LESSON THAT WE HAVE PLANNED TILL NOW, I WILL PROVIDE YOU THE LESSON INFORMATION WITH ADDED TOPICS INSIDE THE LESSON, YOU CREATES THE LEARNING OUTCOMES IN 4 ASPECTS, COGNITIVE, TECHNICAL, PROBLEM SOLVING SKILLS AND SOFT SKILLS. 

SAMPLE OF HOW TO WRITE THE LEARNING OUTCOMES IS GIVEN IN THE ATTACHED IMAGE AND BELOW SAMPLE AS WELL: 
USE BLOOM VERBS FOR COGNITIVE PART. 
TECHNICAL PART SHOULD BE ALIGNED WITH PSYCHOMOTOR SKILL TAXONOMY
PROBLEM SOLVING SKILLS PART SHOULD BE ALIGNED WITH 3C Problem-Solving Framework. 
AND SOFT SKILLS PART SHOULD BE ALIGNED WITH CASEL SOCIAL EMOTIONAL FRAMEWORK. 

****
SAMPLE LEARNING OUTCOMES THAT IS MADE FOR CLASS 9: IMAGE AND VISION  


## project criteria

Criteria
1. Project should not use linux-based development boards like Raspberry Pi and Jetson Products.
2. Projects should integrate python devleopment boards for AI integration.
3. Programming language are strictly Python and Arduino programming.
4. 


Project list
1. Object Detection Based Treasure Hunt with AI Cam.
2. Smart Dustbin (Move around and classify different types of waste)
3. Face detection security robot (Detects faces and tracks them with camera movement)
4. Color following robot (Follows objects of specific colors using HSV color detection)
5. QR Code Scanner Robot (Scans QR codes and performs programmed actions, like dancing with servo)
6. Plant Recognizing Robot (Identify different plants along with remote control bluetooth)
7. Traffic Sign DetectionVehicle ( remote control car that recognizes and responds to traffic signs)

[link to the kit](https://www.alibaba.com/product-detail/High-Quality-ESP32-Education-Robot-Kit_1601163322570.html?spm=a2700.prosearch.normal_offer.d_title.6feb67afKFgcZU&priceId=d8594692e0d844409a6b8d5b2fcd9597)
[link to another kit](https://www.alibaba.com/product-detail/ACEBOTT-China-Made-AI-Visual-Robot_1601567963876.html?spm=a2700.prosearch.normal_offer.d_title.7f1a67af57OkmN&priceId=b84880d0f50e41f3b1731ef8bfb06a3b)


4:motor/battery/switch (mechanical) (parents, stakeholders, studentss point of view, who you are trying to teach, why you are teaching, no murga,  professionals (difference thin line between  the course taken and not taken students))
5: 


apil.ghimire@ingskill.edu.np
1234Bishal1234

[Kendryte k21](https://maixduino.sipeed.com/en/hardware/k210.html) AI vision and hearing development board.



5Es: Engage, explore, explain, elaborate, evaluate
### teaching plan for class 9 robotics

1. students already have the background of Python programming, but the basic Python won't be sufficient for the kind of project planned for class 9. 
2. Computer Vision should be teached from ground up along with a basic implementation.
3. What is image, composition of the image, color channels in image (black and white, RGB) dealing with images with Python(OpenCV).
4. Object recognition, how the AI learns the patterns and able to recognize objects and faces, how? (learning kit allow training the recognition model in real time by capturing the samples with the embedded ESP32 camera itself)
5. How color detection works and how its different from using IR sensors? with OpenCV.
6. Students also required to learn and apply the qrcode/barcode specific python library like *pyzbar*. 
7. Not only qrcode and barcode, fiducial markers like AprilTags are very essential for robotics applications (apriltag/fiducial markers are like a qrcode for robots that contains specific instructions according to which the robots perform task as simple as led blinking to moving different actuators)
8. synergy between Python/AI and robotics, merely arduino programming and robots aren't sufficient for dealing with the real world problems and scenarios due to which Python integration is must, 
9. Our learning kit uses the development board slightly different from esp32 which  is Kendryte k210 which have builtin support for AI vision tasks from object recognition, face recognition, apriltag detection and color detection, such vision features are implemented via Python programming specifically known as MaixPy along with IDE support for this micropython implementation.

#### lessons
1. image and its composition (fundamentals)
2. dealing with the images (image processing, image operations (cropping, grayscale, rotating, resolution))
3. human vision and computer vision
4. why AI vision required, synergy (robotics and AI)
5. real world applications (robotics and AI)
6. Python and its derivatives (Micropython, MaixPy)
7. vision and sensors (when to use which or difference between them)
8. recognizing objects (is it memorizing or finding patterns)
9. teachable machines
10. apriltags (qr code with instructions sets for robots)
11. sensor fusion (sensors and AI vision)

## lessons 
1. image
2. image composed of (pixels, channels, color values)
3. color spaces in images (RGB, HSV, BINARY)
4. human vision and robot's vision (humans see continuously with **perception** (eye); robots see **discretely** via sensors/cameras and algorithms.)
5. working with the images (image processing, filtering, resizing, detecting edges, extracting features.)
6. ***python programming (syntax, data types, loops, functions )*** 
7. running python code via shell(REPL)
8. code editor for python (IDEs/editors like VS Code, MU editor)
9. running python script
10. development boards supporting python
11. variants of python (micropython and maix py)
12. MicroPython and Maix Py 
13. getting started with MicroPython (flash firmware, connect via serial)
14. Electronics basics
15. ESP32 and Kendryte K21 ()
16. Sensors, motors and actuators
17. ***arduino programming and hardware components (blinking led, buzzer and ultrasonic threshold for obstacle)***
18. GPIO (read sensors data and triggering outputs)
19. PWM (controlling motor speed, servo angles, movement of the robot)
20. working with sensors data using micropython (learn how to read, filter, and use input from distance, camera, or IMU sensors)
21. controlling actuators and motors using micropython (practice using GPIO + PWM to drive DC motors, servos, and relays)
22. fsm and micropython (design clear robot behaviors (Idle–Drive–Avoid, etc.) using state transitions coded in MicroPython.)
23. communication protocols (i2c, serial, spi)
24. serial communication 
25. i2c communication
26. camera modules and image capture
27. computer vision algorithms (edge detection, contour detection)
28. running cv algorithms in ESP/Kendryte
29. introduction to machine learning
30. learnable machines (machine learning for computer vision, recognizing new face)
31. running ml models in microcontrollers and challenges 
32. testing and debugging
33. object detection/qrcode detection/apriltag detection/face recognition robot 
34. documentation


knowledge competency and skill

**Class 9: Pro**


Knowledge: python programming (micropython), image processing, learnable machines (patterns), qrcodes/barcode/apriltags, synergy of robotics and artificial intelligence

Skills: write python program, working with images (cropping, rotation, color channels), training recognition models, detecting and extracting information from qr codes, applying python logics for actuation (actuators haru move garna or robot ko working mechanism change garna)

Competency: Design and build robots that can perform specified behaviours/variations (person identifying robot, obstacle(object) detection robot, waste classifying robot, color identifying robot, qrcode/barcode decoding robot, robot with robotic arm (performs specific task based on detected april tag))

Tools and Kits:


