#include <Servo.h>

Servo myservo1;
Servo myservo2;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos1 = 0;    // variable to store the servo position
int pos2 = 0; 

void setup() {
  myservo1.attach(9);
  myservo2.attach(10);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  for (pos1 = 0; pos1 <= 90; pos1 += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo1.write(pos1);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos2 = 0; pos2 <= 30; pos2 += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo2.write(pos2);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos1 = 90; pos1 >= 0; pos1 -= 1) { // goes from 180 degrees to 0 degrees
    myservo1.write(pos1);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos2 = 30; pos2 >= 0; pos2 -= 1) { // goes from 180 degrees to 0 degrees
    myservo2.write(pos2);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}