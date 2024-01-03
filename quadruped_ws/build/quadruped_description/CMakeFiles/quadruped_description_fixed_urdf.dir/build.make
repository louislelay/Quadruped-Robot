# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/louis/.local/lib/python3.10/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/louis/.local/lib/python3.10/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/louis/Documents/Quadruped-Robot/quadruped_ws/build/quadruped_description

# Utility rule file for quadruped_description_fixed_urdf.

# Include any custom commands dependencies for this target.
include CMakeFiles/quadruped_description_fixed_urdf.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/quadruped_description_fixed_urdf.dir/progress.make

CMakeFiles/quadruped_description_fixed_urdf: /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/quadruped_fixed.urdf

/home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/quadruped_fixed.urdf: /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/quadruped.xacro
/home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/quadruped_fixed.urdf: /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/gazebo.xacro
/home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/quadruped_fixed.urdf: /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/inertias.xacro
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/louis/Documents/Quadruped-Robot/quadruped_ws/build/quadruped_description/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating quadruped_description robot fixed in world URDF"
	cd /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf && xacro quadruped.xacro is_fixed:=true -o quadruped_fixed.urdf

quadruped_description_fixed_urdf: CMakeFiles/quadruped_description_fixed_urdf
quadruped_description_fixed_urdf: /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description/urdf/quadruped_fixed.urdf
quadruped_description_fixed_urdf: CMakeFiles/quadruped_description_fixed_urdf.dir/build.make
.PHONY : quadruped_description_fixed_urdf

# Rule to build all files generated by this target.
CMakeFiles/quadruped_description_fixed_urdf.dir/build: quadruped_description_fixed_urdf
.PHONY : CMakeFiles/quadruped_description_fixed_urdf.dir/build

CMakeFiles/quadruped_description_fixed_urdf.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/quadruped_description_fixed_urdf.dir/cmake_clean.cmake
.PHONY : CMakeFiles/quadruped_description_fixed_urdf.dir/clean

CMakeFiles/quadruped_description_fixed_urdf.dir/depend:
	cd /home/louis/Documents/Quadruped-Robot/quadruped_ws/build/quadruped_description && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description /home/louis/Documents/Quadruped-Robot/quadruped_ws/src/quadruped_description /home/louis/Documents/Quadruped-Robot/quadruped_ws/build/quadruped_description /home/louis/Documents/Quadruped-Robot/quadruped_ws/build/quadruped_description /home/louis/Documents/Quadruped-Robot/quadruped_ws/build/quadruped_description/CMakeFiles/quadruped_description_fixed_urdf.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/quadruped_description_fixed_urdf.dir/depend
