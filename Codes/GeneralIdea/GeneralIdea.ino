//Not the version I use as it needs me to clean it
//But this give the general idea

#include <Servo.h>

// Define the servos for the two joints
Servo joint1;
Servo joint2;

// Define the pins for the servos
const int joint1Pin = 9;  // Adjust pin numbers as needed
const int joint2Pin = 10;


// Placeholder for the kinematics matrix (2x2)
float kinematicsMatrix[4][4] = {
  {X, X, 0, X},  // Replace these values with your actual matrix values
  {X, X, 0, X},
  {X, X, 1, 0},
  {0, 0, 0, 1}
};

void setup() {
  // Attach the servos to their respective pins
  joint1.attach(joint1Pin);
  joint2.attach(joint2Pin);
}

void loop() {
  //make it do what you need
}

// Function to convert radians to degrees if needed
float radians_to_degrees(float radians) {
  return radians * 180.0 / PI;
}
