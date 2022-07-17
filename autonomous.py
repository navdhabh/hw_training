#!/usr/bin/env python

from roboclaw import RoboClaw
import rospy

#---------------------------------------------------- 

class Drive:
    def __init__(self,driver1,driver2):
        self.rightClaw = driver1
        self.leftClaw = driver2
         

    def drive_callback(self,inp):
        # A bit of help! These are arrays of data
        axes = inp.axes
        buttons = inp.buttons
        f = buttons[0]
        b = buttons[1]
        r = buttons[2]
        l = buttons[3]
        val = 1
        if (f==1):
            RoboClaw.ForwardM2(self,val)
            RoboClaw.ForwardM1(self,val)
        elif b==1:
            RoboClaw.BackwardM1(self,val)
            RoboClaw.BackwardM2(self,val)
        elif r==1:
            RoboClaw.ForwardM2(self,val)
            RoboClaw.BackwardM1(self,val)   #M1 on right, M2 on left
        elif l==1:
            RoboClaw.ForwardM1(self,val)
            RoboClaw.BackwardM2(self,val)
                
        

    def current_limiter(self):
        """BONUS: 

        Try to implement this function as well. It is a saftey feature. 
        How would you decide the current threshold? - Please elaborate
        """
        return False
                

#---------------------------------------------------                



