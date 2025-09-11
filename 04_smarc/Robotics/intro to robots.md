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
##############################################################################

Robot Subsystems
Engage: **Recognize the parts**: demonstrate a simple line following robot. Introduce the term **subsystems** and pose a guiding question: “How do different parts of a robot work together?”
Explore:  Students are provided with disassembled line following robot, try to identify and label the parts and guess their function and discuss which parts are responsible for movement of the robot and which parts allow robot to think? 
Explain: Teacher explains the concepts: a. Explain the function of the robot's components. b. Explain how those components connect and work as a  system.
Elaborate: Students design a obstacle avoidance robot with different subsystems.
Evaluate: Quiz on what are subsystems, their roles and how  they connect?

Human  Vs Robots 
Engage: Show a short video of robots and human doing  same work in coca cola factory. Ask students to differentiate the efficiency between human and robot doing the task.  Introduce the analogy of human's part with robot's. (eyes:sensors, arms:actuators)
Explore: Students are assigned to match the robot's part with human part based on function from a labelled diagram of human anatomy and robot's anatomy. 
Explain: Teacher explains: a. Explain difference between biological senses and electronic sensors. b. Explains the energy source for robots and human
Elaborate: Students solve scenario-based question and propose a solution: (A robot needs to identify the walls around the room, how the robot's eye difers from human's eye in this context)
Evaluate: Quiz: a. which robot subsystem is similar to human brain? A robot's touch sensor is analogous to which part of human's body? For what kind of tasks robots are best suited for?

Robots vs Machines
Engage: Display common objects (e.g., toaster, Roomba vacuum, elevator, robotic arm) and ask: “Which of these are robots? Why?” Also pose a guiding questions: What makes a robot more than just a machine?  
Explore: **Sorting Game**: Images of 10 different objects (mars rover, line following robot, fan, car, bike, knife, sophia robot) are given. Students sort between robot and machine. 
Explain: Now teacher explains: a. Explain defining features of robots and machines. Explain rule-based intelligence and fixed function. 
Elaborate: Students plan and design robot by adding one subsystem into the machine. (a toy car to obstacle avoidance car) and justify why is this a robot now? 
Evaluate: Quiz: a. label the objects in the image as robot or machine with one sentence justification. b. Give one example where machine works better than a robot. 

Robot's Mobility
Engage: Show three short video clips of (a. wheeled robot navigating, legged robot climbing stairs, drone flying over terrain) and follow up with a question why robot needs different legs for different road?
Explore: Students test a wheeled robot on sand and tiled surface. discuss why driving robot on tiled surface feels smooth as compared to sand. 
Explain: Teacher explains: a. why wheels struggle in sand? b. what does the robot's mobility means? c. If robot is climbing stairs, why it can't use wheels alone? 
Elaborate: Analyse and redesign the mobility for robot. **Scenario**: 'a wheeled robot is stucked in a mud during a flood rescue.'
Evaluate: Quiz: a. A robot must move quickly on smooth tile floors. Should it use tracks or wheels? Explain. b. Which mobility type is best for climbing stairs? Why?

Robot's Autonomy
Engage: Show three video clips side by side (a person controlling remote control car, a line following robot autonomously navigation a black tape path, and a actual self driving car moving around the city (tesla car delivers itself to its owner {youtube})) 
Explore: Use remote controller to control the car around the class and suddenly stop pressing the buttons and observe what happens next? Followed by the discussion on why the robot stopped when the buttons are not pressed, is it possible for a robot to control itself, making decisions?
Explain: Teacher explains: a. why did the rc robot stopped when the controller is released? b. how did the line follower robot know to turn when it saw the black tape? 
Elaborate: Design and simulate an autonomous obstacle avoidance car by adding one sensor and writing the If-Then logic based on sensor's readings 
Evaluate: **Quiz**: a. Write an IF-THEN rule for a robot that stops when it sees a cliff. b. A robot vacuum turns when it bumps into a wall. Is this remote-controlled or autonomous? Why?

Robot's Environment
Engage:  **Mystery Environment Game**: Show the pictures/videos of robot working in different environments (roomba vaccum robot in home, mars rover in space, underwater robot) 
Explore: Test a waterproof robot and regular remote controlled robot in a water tank and see which one have the problem with circuits.
Explain: Teacher explains: a. Why different environments requires different design of the robot? 
Elaborate: Group of students pick one environment for the robot, identify 2 challenges in that environment, choose tools/sensors for those specific challenges, write if-then rule.
Evaluate: **Quiz**: a. “A robot in a dark cave needs to avoid rocks. Which sensor should be used? b. :"A hospital robot must find invisible germs." which sensors should be used in this situation? 

Robot's Job
Engage: 
Explore:
Explain:
Elaborate:
Evaluate:


#######################################

Prompt

Write down the content for grade 4 students from Nepal following the instructions provided below. Strictly follow the guidelines mentioned.
We are following the 5E instructional model for designing and writing this content.
Core Philosophy (Context, Content, Real World Application and most importantly  Interactions)

**Flow of the content and  Guidelines for each sections of the Chapter.**
1. Overview of the chapter (must be generated strictly at last)
2. Learning objectives (They should be written on the basis of the learning outcomes that will be provided for each lessons from the lesson plan for  grade 4). The writing format for learning outcomes: L01: learning outcomes, L02: learning outcomes like this. 
3. Engaging students (use a **anology** that should be based on prior knowledge of the students of class 4 from Nepal which should spark curiosity inside the mind of students, this analogy idea will be provided by the user themself if not provided then craft by yourself). Strictly don't include  the topic itself (if the topic is about the  switch then you don't  include the word switch in the analogy rather introduce it after the analogy and  activity is completed. The activity for this part as well should not be technical but related to the topic(for example if teaching about switch, the activity which instruct students to use switch itself doesn't make sense at all as they don't know about it)). Additionally the generic questions raised should be answer as well simply. 
   **engage part strict flow**
	1. analogy related to prior knowledge
	2. activity plan
	3. questions related to activity (what if types questions)
	4. conclude the activity and  connect to the topic
	5. now introduce the topic with an example.
4. Then comes explore part which should now relate with the above engage analogy to add the essence of the topic. Include examples and a activity related and relevant to topic followed 1-3 generic topic related question (strictly don't add technical question in technical language).  
5. Then comes explain part which should explain what, why and how questions according to the context of the lesson. why, what and how shouldn't be explained in very long, lengthy sentences rather very short, sweet, straight and understandable way. if possible don't include all three questions in this explain part, keep one question for the elaborate part.  
6. Then comes elaborate which should further expands what explained in the explaining step adding a step up and forcing them to think along with explaining any other topics that was missed or was out of scope in explain step(what why and how of explain phase). Starting of the elaborate part must contain the example of the concepts of topics explained in explain phase, followed by a activity that is actually related to topic and technical unlike the engage's activity,  then only based on those examples you enforce them to think learn more. 
7. Then comes **let's think** part where you ask questions again allowing students to think and reason based on what explained and elaborated.
8. Then add **let's summarize** section which summarizes the content of the lesson in bullet points this should be  aligned with the learning objectives and the overall content of the lesson. 
9. And at last add a MCQ quiz (4-7) related to topics. 

**Other Writing Guidelines to be followed**
1.  Examples used in the content should be specifically nepali examples as much as possible, ING companies to be used where technology or food or education comes. unless the example must be a specific non-nepali example, use nepali example. also use the names that reflects the ethnicity of nepal like dolma, yonten, sujan, nisha, bibek, niraj and many more be creative regarding the names of places and people relevant specifically to Nepal and Nepali. for currency examples strictly use rupees instead of dollar or anything else.
2. Strictly use british english.
3. Flesch Readability score of generated content must be in the range of 75-85. 

**Files to be attached are:**
1. flowchart of how whole content should be generated or crafted, the strict flow that you must follow. 
2. and Syllabus of grade 4
3. sample content file that contains the properly crafted content for the Algorithm chapter for grade 4 students of Nepal. 

Respond to this chat with (what you will do and what you won't and yes/no question if you understood  the task).
After this chat the learning outcomes for the specific lesson, analogy idea,  will be provided and the content generation starts. 

## prompt v1.3

Write down the content for grade 4 students from Nepal following the instructions provided below. Strictly follow the guidelines mentioned. We are following the 5JE instructional model for designing and writing this content. Core Philosophy (Context, Content, Real World Application and most importantly Interactions) 

Flow of the content and Guidelines for each section of the Chapter. 

1. Overview of the chapter (must be generated strictly at last) 
    

2. Learning objectives (They should be written on the basis of the learning outcomes that will be provided for each lesson from the lesson plan for grade 4). The writing format for learning outcomes: L01: learning outcomes, L02: learning outcomes like this.  
    

3. Engaging students (use an analogy that should be based on prior knowledge of the students of class 4 from Nepal which should spark curiosity inside the mind of students, this analogy idea will be provided by the user themself if not provided then craft by yourself). Strictly don't include the topic itself (if the topic is about the switch, then you don't include the word switch in the analogy rather introduce it after the analogy and activity is completed. The activity for this part as well should not be technical but related to the topic (for example if teaching about switch, the activity which instructs students to use switch itself doesn't make sense at all as they don't know about it). Additionally, the generic questions raised should be answered as well simply.  
    
	1. engage part strict flow 
	2. Analogy/question related to prior knowledge 
	3. Activity plan (hands-on activity but not technical, generic that relates to the lesson 
	4. Questions related to activity (what if type) 
	5. Conclude the activity and connect to the topic 	
	6. Introduce the topic with an example 
	    

10. Then comes the explore part which should now relate with the above engage analogy (limited instruction) to add the essence of the topic. Include examples and an activity related and relevant to topic followed 1-3 generic topic related question (strictly don't add technical question in technical language).  

	1. Introduce an activity to let them explore the topic. 
	2. Give minimal instructions to do the activity. 
	    

Multiple possible outcomes can be generated through this activity 

6. Then comes the explain part which should explain what, why and how questions according to the context of the lesson. why, what and how shouldn't be explained in very long, lengthy sentences rather very short, sweet, straight and understandable way. If possible don't include all three questions in this explain part, keep one question for the elaborate part.  
	1. Ask questions on the explore activity. 	
	2. Address where they can make mistakes. 
	3. Explain the importance of the topic, or about their possible mistakes. 
	4. Explain about the results/outcomes they produce after the explore activity

7. Then comes elaborate which should further expands what explained in the explaining step adding a step up and forcing them to think along with explaining any other topics that was missed or was out of scope in explain step (what why and how of explain phase). Starting of the elaborate part must contain the example of the concepts of topics explained in explain phase, followed by an activity that is related to topic and technical unlike the engage 'activity, then only based on those examples you enforce them to think learn more. 

	1. Offer a real-world scenario and context related to the topic 
	    
	2. And explain the topic based on the real-world scenario and context 
	    
	3. Go as much as detailed for the grade, extend the topic 

8. Then comes let's think part where you ask questions again allowing students to think and reason based on what explained and elaborated. 
9. Then add let's summarize section which summarizes the content of the lesson in bullet points this should be aligned with the learning objectives and the overall content of the lesson.  
10. And lastly, add a MCQ quiz (4-7) related to topics. 
    

Other Writing Guidelines to be followed 

1. Examples used in the content should be specifically Nepali examples as much as possible, ING companies to be used where technology or food or education comes. unless the example must be a specific non-Nepali example, use Nepali example. also use the names that reflects the ethnicity of Nepal like dolma, Yonten, Sujan, Nisha, Bibek, Niraj and many more be creative regarding the names of places and people relevant specifically to Nepal and Nepali. for currency examples strictly use rupees instead of dollar or anything else. 

2. Strictly use British English. 
3. The Flesch Readability score of generated content must be in the range of 75-85. 

Files to be attached are: 

4. flowchart of how whole content should be generated or crafted, the strict flow that you must follow.  
5. and Syllabus of grade 4 
6. sample content file that contains the properly crafted content for the Algorithm chapter for grade 4 students of Nepal. 

Respond to this chat with (what you will do and what you won't and yes/no question if you understood the task). After this chat the  

4. learning outcomes for the specific lesson,  
5. analogy idea,  

will be provided and the content generation starts.