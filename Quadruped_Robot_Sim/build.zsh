#convert xacro to urdf
xacro description/quadruped_robot.xacro > description/quadruped_robot.urdf


#create free sdf
xacro description/quadruped_robot.xacro > simulation/models/quadruped_robot/quadruped_robot.urdf && gz sdf -p simulation/models/quadruped_robot/quadruped_robot.urdf > simulation/models/quadruped_robot/quadruped_robot.sdf

#create fixed sdf
xacro description/quadruped_robot.xacro > simulation/models/quadruped_robot_fixed/quadruped_robot_fixed.urdf is_fixed:=true && gz sdf -p simulation/models/quadruped_robot_fixed/quadruped_robot_fixed.urdf > simulation/models/quadruped_robot_fixed/quadruped_robot_fixed.sdf

export GAZEBO_MODEL_PATH=/home/louis/Quadruped-Robot/Quadruped_Robot_Sim/simulation/models

gazebo simulation/worlds/quadruped_robot_fixed.world
