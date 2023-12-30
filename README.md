# Quadruped-Robot

This is the README file for my project of a Quadruped Robot.

It is still a work in progress and it contain 2 main aspects, one is the 3d model which I've began to 3d print. The rest is file for simulation on GAZEBO. The 3d model is made using Solidworks.

This is the 3d model of the leg, following the 3d printed version :

![3d Model of the leg](https://github.com/louislelay/Quadruped-Robot/blob/main/Images/leg3d.png)

![3d Printed Version](https://github.com/louislelay/Quadruped-Robot/blob/main/Images/leg.jpg)

From this, I've find the kinematics and I've tested them, I'm now able to control them and know exactly where will be the end of the leg.

https://www.youtube.com/watch?v=jixDbttGpBg&ab_channel=LouisLeLay

The next step is now to 3d print the rest and test it.

![3d Model of the Quadruped Robot](https://github.com/louislelay/Quadruped-Robot/blob/main/Images/quad.png)

I've began by creating a ".xacro" file in order to simplify the creation of a ".urdf" file. The goal was to simulate a simple verson of the robot on GAZEBO. In order to see easily how I was going, I used this website : https://mymodelrobot.appspot.com/
 
It makes it easier to see what I'm doing as I advance. This is what I ended up with :
 
 
![1st conception](https://github.com/louislelay/Quadruped-Robot/blob/main/Images/URDF.png)

After this was done, I've created the other files to simulate in gazebo. If you want to modify the values in ".xacro", don't forget to run these command in a terminal inside /Quadruped-Robot/Quadruped_Robot_Sim :

```bash
#convert xacro to urdf
xacro description/quadruped_robot.xacro > description/quadruped_robot.urdf

#create free sdf
xacro description/quadruped_robot.xacro > simulation/models/quadruped_robot/quadruped_robot.urdf && gz sdf -p simulation/models/quadruped_robot/quadruped_robot.urdf > simulation/models/quadruped_robot/quadruped_robot.sdf

#create fixed sdf
xacro description/quadruped_robot.xacro > simulation/models/quadruped_robot_fixed/quadruped_robot_fixed.urdf is_fixed:=true && gz sdf -p simulation/models/quadruped_robot_fixed/quadruped_robot_fixed.urdf > simulation/models/quadruped_robot_fixed/quadruped_robot_fixed.sdf
```


And to run the model, in the same terminal do (don't forget to adapt to your path) : 

```bash
export GAZEBO_MODEL_PATH=/home/louis/Quadruped-Robot/Quadruped_Robot_Sim/simulation/models
gazebo simulation/worlds/quadruped_robot_fixed.world
```
