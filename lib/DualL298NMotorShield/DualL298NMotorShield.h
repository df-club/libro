#ifndef DualL298NMotorShield_h
#define DualL298NMotorShield_h

#include <Arduino.h>

class DualL298NMotorShield
{
  public:  
    // CONSTRUCTORS
    DualL298NMotorShield(); // Default pin selection.
    DualL298NMotorShield(unsigned char M1DIR, unsigned char M1PWM,
                           unsigned char M2DIR, unsigned char M2PWM); // User-defined pin selection. 

    // PUBLIC METHODS
    void init(); // Initialize TIMER 1, set the PWM to 20kHZ. 
    void setM1Speed(int speed); // Set speed for M1.
    void setM2Speed(int speed); // Set speed for M2.
    void setSpeeds(int m1Speed, int m2Speed); // Set speed for both M1 and M2.

  private:
    static const unsigned char _M1DIR = 4;
    static const unsigned char _M2DIR = 7;
    static const unsigned char _M1PWM = 5;
    static const unsigned char _M2PWM = 6;
};

#endif