cmake_minimum_required(VERSION 3.8)

project(quadruped_description)

find_package(ament_cmake REQUIRED)


# Free (in the world) model, urdf and sdf generation
add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped.urdf
  DEPENDS
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped.xacro
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/gazebo.xacro
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/inertias.xacro
  COMMAND xacro quadruped.xacro -o quadruped.urdf
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/urdf
  COMMENT "Generating ${PROJECT_NAME} robot URDF"
  VERBATIM
)

# Cmake needs a custom target to execute a custom command
add_custom_target(
  ${PROJECT_NAME}_urdf
  DEPENDS
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped.urdf
)

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/simulation/models/quadruped/quadruped.sdf
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped.urdf ${PROJECT_NAME}_urdf
  COMMAND gz sdf -p urdf/quadruped.urdf > simulation/models/quadruped/quadruped.sdf
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Generating ${PROJECT_NAME} robot SDF"
  VERBATIM
)

add_custom_target(
  ${PROJECT_NAME}_sdf
  DEPENDS ${PROJECT_NAME}_urdf
)

# Model fixed to simulation world, urdf and sdf.
add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped_fixed.urdf
  DEPENDS
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped.xacro
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/gazebo.xacro
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/inertias.xacro
  COMMAND xacro quadruped.xacro is_fixed:=true -o quadruped_fixed.urdf
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/urdf
  COMMENT "Generating ${PROJECT_NAME} robot fixed in world URDF"
  VERBATIM
)

add_custom_target(
  ${PROJECT_NAME}_fixed_urdf
  DEPENDS
  ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped_fixed.urdf
)

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/simulation/models/quadruped_fixed/quadruped_fixed.sdf
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/urdf/quadruped_fixed.urdf ${PROJECT_NAME}_fixed_urdf
  COMMAND gz sdf -p urdf/quadruped_fixed.urdf > simulation/models/quadruped_fixed/quadruped_fixed.sdf
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Generating ${PROJECT_NAME} fixed robot SDF"
  VERBATIM
)

add_custom_target(
  ${PROJECT_NAME}_fixed_sdf
  DEPENDS ${PROJECT_NAME}_fixed_urdf
)

# Requires that python package "onshape-to-robot" has been installed
# These are manual commands, they only need to be launched
# when the cad has changed. The generated files are versionned in git.
add_custom_target(actuator_urdf
  COMMAND onshape-to-robot actuator
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/urdf
  COMMENT "Generating ${PROJECT_NAME} actuator URDF files"
  VERBATIM
)

add_custom_target(actuator_sdf
  COMMAND onshape-to-robot actuator
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/simulation/models
  COMMENT "Generating ${PROJECT_NAME} actuator SDF files"
  VERBATIM
)

add_custom_target(quadruped_urdf
  COMMAND onshape-to-robot quadruped
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/urdf
  COMMENT "Generating ${PROJECT_NAME} quadruped URDF files"
  VERBATIM
)

add_custom_target(quadruped_sdf
  COMMAND onshape-to-robot quadruped
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/simulation/models
  COMMENT "Generating ${PROJECT_NAME} quadruped SDF files"
  VERBATIM
)

add_custom_target(left_leg_urdf
  COMMAND onshape-to-robot left_leg
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/urdf
  COMMENT "Generating ${PROJECT_NAME} quadruped URDF files"
  VERBATIM
)

# See https://samthursfield.wordpress.com/2015/11/21/cmake-dependencies-between-targets-and-files-and-custom-commands/
# for explanation on dependency management and custom_commands.
add_custom_target(
  ${PROJECT_NAME}_generated ALL
  DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/simulation/models/quadruped/quadruped.sdf
    ${CMAKE_CURRENT_SOURCE_DIR}/simulation/models/quadruped_fixed/quadruped_fixed.sdf
)

install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME})

install(DIRECTORY simulation
  DESTINATION share/${PROJECT_NAME})

# Install launch files
install(DIRECTORY launch/
        DESTINATION share/${PROJECT_NAME}/launch)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
