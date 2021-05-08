/***************************************************************
   Motor driver function definitions - by James Nugen
   *************************************************************/

void initMotorController();
void setMotorSpeed(int i, int spd);
#ifdef L298N
void setMotorSpeeds(int leftSpeed, int rightSpeed);
#endif
#ifdef L298N_4WD
void setMotorSpeeds(int leftSpeed_1, int leftSpeed_2, int rightSpeed_1, int rightSpeed_2);
#endif
