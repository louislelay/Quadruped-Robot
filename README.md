# Quadruped-Robot

This is the README file for my project of a Quadruped Robot.
 
 
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


And to run the model, in the same terminal do : 

```bash
export GAZEBO_MODEL_PATH=/home/Quadruped-Robot/Quadruped_Robot_Sim/simulation/models
gazebo simulation/worlds/quadruped_robot_fixed.world
```
