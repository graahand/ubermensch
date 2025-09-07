## Overview

This lesson teaches how a robot can use an IR sensor to sense distance (near / far) and light (light / dark) and then follow simple **if–then** rules to decide what to do: **go**, **stop** or **turn**. Students will make rule tables, test their rules on a paper track or classroom map, and improve rules that do not work.

# Learning objectives

By the end of this lesson, students will read and write simple rules for a robot using an IR sensor, use a rule table to choose actions, test those rules on a map or paper track, and work well in teams while explaining their ideas.

- Read simple **if–then** rules for a robot that uses an IR sensor.
    
- Make a rule table to decide robot actions (go, stop, turn) from what the sensor reads (near / far, light / dark).
    
- Test their rules on a paper track or classroom map and fix rules that do not work.
    
- Plan and work in teams, take turns, and explain their thinking clearly.
# Introduction

Imagine a small robot helping people in Kathmandu traffic. The robot must stop when it sees a person close by. It must go when the road is clear. How does the robot know when to stop or go? An **IR sensor** can help it see if something is **near** or **far** and whether it is **light** or **dark**.

**Think:** If the robot sees a garbage bag in front of it on a street in Thamel, what should it do? Use that question as you plan simple rules for the robot.

# Concepts Explanation

## Key Terms

- **IR sensor**: a small device that uses infrared light to tell if something is near or far, or if it is bright or dark.
    
- **if–then rule**: a sentence that tells the robot what to do. Example: **If** the sensor reads near, **then** stop.
    
- **rule table**: a simple table that shows sensor readings and the robot action for each reading.
    
- **action**: what the robot does (for example, **go**, **stop**, **turn left**, **turn right**).
## Word Alerts

- **Near / far**: these words describe distance. _Near_ means something is close to the robot. _Far_ means it is not close.
    
- **Light / dark**: these words describe how bright the place is. An IR sensor can also show whether there is light or darkness.
    
- **Debug**: to find mistakes in the rules and fix them so the robot works correctly.

## How an If–Then Rule Looks

- A simple rule: **If** the sensor reads _near_, **then** _stop_.
    
- Another rule: **If** the sensor reads _far_ and it is _light_, **then** _go_.
    
Transition: Next we build a rule table that shows all possible readings and a robot action for each.

# Examples

### Example 1 — A Simple Rule Table

|sensor reading|action|
|---|---|
|**near**|**stop**|
|**far**|**go**|

**Context:** On a school playground in **Pokhara**, Dolma and Sujan test a toy robot. If the IR sensor says **near** (a ball is close), the robot **stops**. If the sensor says **far** (no ball close), the robot **goes**.

**Why this helps:** Simple rules are easy to test. If the robot keeps bumping the ball, the students will change the rule.

---

### Example 2 — Rule Table with Distance and Light 

Sometimes the robot needs more detail. Use both **distance** and **light** to decide.

|distance|brightness|action|
|---|---|---|
|near|light|stop|
|near|dark|turn right|
|far|light|go|
|far|dark|go slowly|

**Context:** In **Biratnagar**, Nisha designs a robot to deliver papers. If the path is **near** and **dark**, the robot turns right to avoid a shadow that might hide a hole. If it is **far** and **light**, it goes at normal speed. If it is **far** and **dark**, it goes slowly.

**Teacher note:** Keep actions simple: **go**, **stop**, **turn left**, **turn right**, **go slowly**.

---

### Worked Example — Test and Fix Rules on a Paper Track

1. Draw a paper track on the classroom floor that looks like a small road from **Ilām** to **Dhulikhel**. Mark **obstacles** (stone, puddle, parked cart).
    
2. Team A (Bibek, Yonten, and Nisha) writes this rule table:
    
|reading|action|
|---|---|
|near|stop|
|far|go|

3. They test the rule by moving a toy robot on the paper track. The robot stops well before a small obstacle but gets stuck when the obstacle is only half in front.
    
4. The team **debugs**: they add a rule for _near but light_ and _near but dark_ to decide whether to stop or turn. The robot now can turn around small obstacles.
    
**Reflection question:** Why did adding the brightness reading help Bibek’s robot? (Answer: the robot could treat shadows differently so it does not stop when there is only low light but no real obstacle.)

---

### Classroom Challenge — Real-World Problem

**Situation:** The small robot helps with goods at **Kavya School** fair in **Butwal**. There are children and plenty of light during the day but dark corners at the back of the hall. The robot should:

- **stop** if something is near,
    
- **go** if the path is clear and light,
    
- **turn** when near and dark to find a new path.
    

**Task for students (team)**: Make a rule table and test the rules on the class map. Try at least two different rules and pick the one that works best.

# Summary

- An **IR sensor** tells a robot if something is **near** or **far**, and if it is **light** or **dark**.
    
- Students make **if–then rules** and put them in a **rule table** to decide actions: **go**, **stop**, **turn**.
    
- Testing rules on a paper track or classroom map finds problems. Students should **debug** and improve rules.
    
- Teamwork matters: plan in teams, take turns, and explain your thinking clearly.
    

# Quiz and Evaluation

## Quick Quiz 

1. (Multiple choice) What does an IR sensor measure?  
    A. Colour only  
    B. Distance and light **(correct)**  
    C. Sound
    
2. (Multiple choice) Which rule should you write if something is very close in front of the robot?  
    A. If near then go  
    B. If near then stop **(correct)**  
    C. If far then stop
    
3. (Short answer) Write an if–then sentence for the robot that must turn when it sees darkness and something near.  
    **Expected answer:** If the sensor reads near and dark, then turn.
    
4. (Short answer) Name two actions a robot can take from this lesson.  
    **Expected answer:** go, stop (also accept turn left, turn right, go slowly)
    
5. (True / false) You should test rules on a paper track. **True**.
    

