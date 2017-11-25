
from AriaPy import *
import numpy as np
from nn import neural_net
import sys


class ActionGo(ArAction):
  def __init__(self, maxSpeed, stopDistance):
    ArAction.__init__(self, "Go")
    self.myMaxSpeed = maxSpeed
    self.myStopDistance = stopDistance

    self.myDesired = ArActionDesired()
    self.mySonar = None

  def fire(self, currentDesired):

    self.myDesired.reset()

    if self.mySonar == None:
      deactivate()
      return None

    range = self.mySonar.currentReadingPolar(-70, 70) - self.getRobot().getRobotRadius()

    if (range > self.myStopDistance):
      speed = range * 60
      if (speed > self.myMaxSpeed):
        speed = self.myMaxSpeed
      self.myDesired.setVel(speed)
    else:
      self.myDesired.setVel(0)
    return self.myDesired


  def setRobot(self, robot):
    self.setActionRobot(robot)
    self.mySonar = robot.findRangeDevice("sonar")
    if (self.mySonar == None):
      ArLog.log(ArLog.Terse, "ActionGo: Warning: The robot had no sonar range device, deactivating!")
      deactivate()


class ActionTurn(ArAction):
  def __init__(self, turnThreshold, turnAmount):
    ArAction.__init__(self, "Turn")
    self.myDesired = ArActionDesired()
    self.myTurnThreshold = turnThreshold
    self.myTurnAmount = turnAmount
    self.Goal = (300,0)
    #load the models
    self.state=np.array([[-0.5,-0.5,-0.5]])
    self.model =neural_net(3, [128, 128], './Models/128-128-64-50000-80000.h5')
    print (self.state)
    self.myTurning = 0 # -1 == left, 1 == right, 0 == none


  def setRobot(self, robot):
    self.setActionRobot(robot)
    self.mySonar = robot.findRangeDevice("sonar")
    if (self.mySonar == None):
      ArLog.log(ArLog.Terse, "ActionTurn: Warning: I found no sonar, deactivating.")
      self.deactivate()

  def fire(self, currentDesired):

    self.myDesired.reset()

    if self.mySonar == None:
      self.deactivate()
      return None
    leftRange = (self.mySonar.currentReadingPolar(0, 100) -
          self.getRobot().getRobotRadius())
    #print(leftRange)
    rightRange = (self.mySonar.currentReadingPolar(-100, 0) - 
          self.getRobot().getRobotRadius())
    #print(leftRange)
    #Normalising readings from software onto hardware
    ls = [leftRange/120, (rightRange+leftRange)/240, rightRange/120]
    ls = [(x-20)/20 for x in ls]
    #print(ls)
    #predict action
    action = (np.argmax(self.model.predict(self.state, batch_size=1)))
    if (leftRange > self.myTurnThreshold  and  rightRange > self.myTurnThreshold):
      self.myTurning = 0
      self.myDesired.setDeltaHeading(0)

    elif (self.myTurning != 0):
      self.myDesired.setDeltaHeading(self.myTurnAmount * self.myTurning)
    elif (action==1):
      self.myTurning = -1
      self.myDesired.setDeltaHeading(self.myTurnAmount * self.myTurning)
    elif action==0 :
      self.myTurning = 1
      self.myDesired.setDeltaHeading(self.myTurnAmount * self.myTurning)
    leftRange = (self.mySonar.currentReadingPolar(0, 30) - 
          self.getRobot().getRobotRadius())
    #print(leftRange)
    rightRange = (self.mySonar.currentReadingPolar(-100, 0) - 
          self.getRobot().getRobotRadius())
    #print(leftRange)    
    ls = [leftRange/120, (rightRange+leftRange)/240, rightRange/120]
    ls = [(x-20)/20 for x in ls]
    if (self.Goal[0]-self.getRobot().getX() <= 500 and self.Goal[1]-self.getRobot().getY() <= 500):
        ls = [-1*x for x in ls]
        if (self.Goal[0]-self.getRobot().getX() <= 100 and self.Goal[1]-self.getRobot().getY() <= 100):
            ls = [-1*x for x in ls]
            exit()
    print(ls)
    #update state again to mirror te pattern in the game.
    self.state=np.array([ls])
    return self.myDesired



Aria.init()
saved_model = './Models/128-128-64-50000-80000.h5'
model = neural_net(3, [128, 128],  './Models/128-128-64-50000-80000.h5')
conn = ArSimpleConnector(sys.argv)
robot = ArRobot()
sonar = ArSonarDevice()


go = ActionGo(100, 300)
turn = ActionTurn(400, 10)
recover = ArActionStallRecover()

  
if not Aria.parseArgs():
  Aria.logOptions()
  Aria.exit(1)

if not conn.connectRobot(robot):
  ArLog.log(ArLog.Terse, "Could not connect to robotnot  Exiting.")
  Aria.exit(1)


robot.addRangeDevice(sonar)


robot.addAction(recover, 100)
robot.addAction(go, 50)
robot.addAction(turn, 49)

# Enable the motors
robot.enableMotors()

robot.run(1)
robot.disconnect()
Aria.shutdown()
