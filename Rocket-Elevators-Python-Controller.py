elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1

class Column(): 
    def __init__ (self, _id, _status, _amountOfFloors, _amountOfElevators) :
        self.ID = _id   
        self.status = _status 
        self.amountOfFloors = _amountOfFloors
        self.amountOfElevators = _amountOfElevators
        self.elevatorsList = []
        self.callButtonsList = []

        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)
    
    def createCallButtons(self, _amountOfFloors): 
        buttonFloor = 1
        for i in range(_amountOfFloors):
            if buttonFloor < _amountOfFloors :
                callButton =  CallButton(callButtonID, 'OFF', buttonFloor, 'Up') 
                self.callButtonsList.append(callButton)
                callButtonID +=1
            
            if buttonFloor > 1 :
             callButton =  CallButton(callButton, 'OFF', buttonFloor, 'Down') 
            self.callButtonsList.append(callButton)
            callButtonID +=1
            

    def createElevators(self, _amountOfFloors, _amountOfElevators): 
        for i in range(_amountOfElevators):
            elevator =  Elevator(elevatorID, 'idle', _amountOfFloors, 1) 
            self.elevatorsList.append(elevator)
            print(elevator)
            elevatorID+=1

    def requestElevator(self, _floor, _direction): 
        elevator = self.findElevator(_floor, _direction)
        elevator.floorRequestList.append(_floor)
        elevator.sortFloorList()
        elevator.move()
        elevator.operateDoors()
        return elevator
    
    def findElevator(self, requestedFloor, requestedDirection): 
        bestElevatorInformations = {
            "bestElevator": None,
            "bestScore": 5,
            "referenceGap": 100000000 }

        for elevator in self.elevatorsList: 
            if requestedFloor == elevator.currentFloor and elevator.status == 'stopped' and requestedDirection == elevator.direction : 
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)
            
            elif requestedFloor > elevator.currentFloor and elevator.direction == 'Up' and requestedDirection == elevator.direction :
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
            
            elif requestedFloor < elevator.currentFloor and elevator.direction == 'Down' and requestedDirection == elevator.direction : 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
            
            elif elevator.status == 'idle' :
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)
               
            else: 
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)
            return bestElevatorInformations["bestElevator"]

    

    def checkIfElevatorIsBetter(self, scoreToCheck, Elevator, bestElevatorInformations, floor): 
        if scoreToCheck < bestElevatorInformations["bestScore"] :  
            bestElevatorInformations["bestScore"] = scoreToCheck
            bestElevatorInformations["bestElevator"] = Elevator
            bestElevatorInformations["referenceGap"] = abs(Elevator.currentFloor - floor)
        elif bestElevatorInformations["bestScore"] == scoreToCheck : 
            gap = abs(Elevator.currentFloor - floor)
            if bestElevatorInformations["referenceGap"] > gap : 
                bestElevatorInformations["bestScore"] = scoreToCheck
                bestElevatorInformations["bestElevator"] = Elevator
                bestElevatorInformations["referenceGap"] = gap 
        return bestElevatorInformations

class Elevator(object): 
    def __init__ (self, _id, _status, _amountOfFloors, _currentFloor):
        self.ID = _id
        self.status = _status
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = _currentFloor
        self.direction
        self.door =  Door (_id, 'closed')
        self.floorRequestButtonsList = []
        self.floorRequestList = []
        self.createFloorRequestButtons(_amountOfFloors)

    def createFloorRequestButtons(self, _amountOfFloors): 
        buttonFloor = 1
        for i in range(_amountOfFloors):
            floorRequestButton =  FloorRequestButton(floorRequestButtonID, 'OFF', buttonFloor)
            self.floorRequestButtonsList.append(floorRequestButton)
            buttonFloor+=1
            floorRequestButtonID+=1
     
    def requestFloor(self, floor): 
        self.floorRequestList.append(floor)
        self.sortFloorList
        self.move
        self.operateDoors

    def move(self):
        while self.floorRequestList.len !=0 :
            destination = self.floorRequestList[0]
            self.status = 'moving'
            if self.currentFloor < destination: 
                self.direction = 'Up'
                while self.currentFloor < destination : 
                    self.currentFloor+=1
                
            elif self.currentFloor > destination :
                self.direction = 'Down'
                while self.currentFloor < destination : 
                    self.currentFloor-=1
            self.status = 'stopped'
            self.floorRequestList.shift()
        
    def sortFloorList(self):
        if  self.direction == 'Up' :
            self.floorRequestList.sort()
           
        else:
            self.floorRequestList.sort(reverse = True)
      #fixing 131 - in des order.   
    def operateDoors(self):
        self.doorStatus = 'opened'

        if not self.overweight : 
            self.door.status = 'closing'
            if not self.door.obstruction: 
                self.door.status = 'closed'
            else:
                self.door.obstruction = False
                self.operateDoors() 
               
        else:
            while self.overweight: 
                self.overweight = False 

 
class CallButton(object): 
    def __init__(self, _id, _status, _floor, _direction):
        self.ID = _id
        self.status = _status
        self.floor = _floor
        self.direction = _direction
        print(self.direction)
class FloorRequestButton(object):
    def __init__ (self, _id, _status, _floor):
        self.ID = _id 
        self.status = _status 
        self.floor = _floor
        print(self.floor)

class Door(object):  
    def __init__(self, _id, _status): 
        self.ID = _id 
        self.status = _status  
        print(self.status)    
    

#========================Scenario 1 =======================
column =  Column(1, 'online', 10, 2) 
column.elevatorsList[0].currentFloor
column.elevatorsList[1].currentFloor =6
elevator=column.requestElevator(3, 'Up')

module.exports = Column, Elevator, CallButton, FloorRequestButton, Door