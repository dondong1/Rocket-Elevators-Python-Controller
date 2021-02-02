for elevatorID = 1
for floorRequestButtonID = 1
for callButtonID = 1

class Column(object) :
    def _init_(_id, _status, _amountOfFloors, _amountOfElevators): 
        self.ID = _id   
        self.status = _status 
        self.amountOfFloors = _amountOfFloors
        self.amountOfElevators = _amountOfElevators
        self.elevatorsList = []
        self.callButtonsList = []

        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)
    
    
   #-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-=1- Method -=1-=1-=1-=1-=1-=1-=1-=1-=1-=1-""""
    def createCallButtons(_amountOfFloors):
        for    buttonFloor = 1
        for (i in range(_amountOfFloors): 
            if(buttonFloor < _amountOfFloors): #If it's not the last floor"""
            return callButton = new CallButton(callButtonID, 'OFF', buttonFloor, 'Up')#id, status, floor, direction""""
            self.callButtonsList.push(callButon)
            callButtonID +=1
            
            if(buttonFloor > _amountOfFloors): #If it is not the first floor"""
            for callButton = new CallButton(callButton, 'OFF', buttonFloor, 'Down')#id, status, floor, direction""""
            self.callButtonsList.push(callButton)
            callButtonID +=1
            
        
    

    def createElevators(_amountOfFloors, _amountOfElevators):
        for(for i = 0; i < _amountOfElevators; i+=1): 
            for elevator = new Elevator(elevatorID, 'idle', _amountOfFloors, 1)#id, status, amountOfFloors, currentFloor""""
            self.elevatorList.push(elevator)
            elevatorID+=1
        
    


   #Simulate when a user press a button outside the elevator""""
    def requestElevator(_floor, _direction): 
        for elevator = self.findElevator(_floor, _direction);
        elevator.floorRequestList.push(_floor);
        sortFloorList();
        operateDoors();
    

    def findElevator(requestFloor, requestDirection): 
        for bestElevatorInformations = 
            bestElevator: null,
            bestScore: 5,
            referenceGap: 100000000
        
        self.elevatorList.forEach(elevator => 
           #The elevator is at my floor and going in the direction I want"""""
            if(requestedFloor == elevator.currentFloor and elevator.status == 'stopped' and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)
            
           #The elevator is lower than me, is coming up and I want to go up"""""
            elif(requestedFloor > elevator.currentFloor and elevator.direction == 'Up' and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
            
           #The elevator is higher than me, is coming down and I want to go down"""""
            elif (requestedFloor < elevator.currentFloor and elevator.direction == 'Down' and requestedDirection == elevator.direction): 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
            
           #The elevator is idle""""
            elif (elevator.status == 'idle'): 
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)
               
           #The elevator is not available, but still could take the call if nothing better is found """
            else 
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)
            
       #bestElevator = bestElevatorInformations.bestElevator
       #bestScore = bestElevatorInformations.bestScore
       #referenceGap = bestElevatorInformations.referenceGap""""
        );
        return bestElevatorInformations.bestElevator;

    

    def checkIfElevatorIsBetter(scoreToCheck, newElevator, bestElevatorInformations, floor): 
        if (scoreToCheck < bestElevatorInformations.bestScore): 
            bestElevatorInformations.bestScore = scoreToCheck
            bestElevatorInformations.bestElevator = newElevator
            bestElevatorInformations.referenceGap = Math.abs(newElevator.currentFloor - floor)
          elif (bestElevatorInformations.bestScore == scoreToCheck):
            for gap = Math.abs(newElevator.currentFloor - floor)
            if(bestElevatorInformations.referenceGap > gap): 
                bestElevatorInformations.bestScore = scoreToCheck
                bestElevatorInformations.bestElevator = newElevator
                bestElevatorInformations.referenceGap = gap 
            
        
        return bestElevatorInformations
    

"""" Column"""

class Elevator(object) 
    def __init__ (_id, _status, _amountOfFloors, _currentFloor): 
        self.ID = _id
        self.status = _status
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = _currentFloor
        self.direction;
        self.door = new Door (_id, 'closed')
        self.floorRequestButtonsList = []
        self.floorRequestList = []
        self.createFloorRequestButtons(_amountOfFloors)
    
    def createFloorRequestButtons(_amountOfFloors):
        for buttonFloor = 1
        for (for i =0; i < _amountOfFloors; i+=1): 
            for floorRequestButton = new FloorRequestButton(floorReqeustButtonID, 'OFF', buttonFloor)#id, status, floor"""
            self.floorRequestButtonsList.push(floorRequestButton)
            buttonFloor+=1
            floorReqeustButtonID+=1
        
    
   #Simulate when a user press a button inside the elevator#
    def requestFlorr(floor): 
        self.floorRequestList.push(floor)
        self.sortFloorList
        self.move
        self.operateDoors
    

    def move(): 
        while (self.floorRequestList.length !=0) 
            for destination = self.floorRequestList[0]
            self.status = 'moving'
            if(self.currentFloor < destination):
                self.direction = 'Up'
                while (self.currentFloor < destination) 
                    self.currentFloor+=1
                
             elif (self.currentFloor > destination):
                self.direction = 'Down'
                while (self.currentFloor < destination) 
                    self.currentFloor-=1
                
            
            self.status = 'stopped'
            self.floorRequestList.shift()
        
    
    def sortFloorList(): 
        if (self.direction == 'Up'): 
            self.floorRequestButtonsList.sort(function(a, b) return a-b);
         else 
            self.floorRequestList.sort(function(a, b) return b-a);
        
    

    def operateDoors(): 
        self.doorStatus = 'opened'
       #WAIT 5 seconds"""
        if (self.overweight): 
            self.door.status = 'closing'
            if (self.door.obstruction): 
                self.door.status = 'closed'
             else 
               #WAIT: for the person to clear the way"""
                self.door.obstruction = false
                self.operateDoors()
            
         else 
            while (self.overweight) 
               #Activate overweight alarm, and wait for someone to get out""""
                self.overweight = false
            
            self.operateDoors()
        
       
 # Elevator""""
 
 class CallButton(object): 
    def _init_ (_id, _status, _floor, _direction) 
         self.ID = _id
         self.status = _status
         self.floor = _floor
         self.direction = _direction
     
 
   #Simulate when a user press a button inside the elevator#
    def requestFloor() 
        class FloorRequestButton 
        constructor (_id, _status, _floor) 
            self.ID = _id 
            self.status = _status 
            self.floor = _floor
        
    

    class Door(object) 
        def __init__(_id, _status) 
        self.ID = _id 
        self.status = _status  
              
    


""""========================Scenario 1 =======================""""
for column = new column(1, 'online', 10, 2)#id, status, amountOfFloors, amountOfElevators"""
column.elevatorsList[0].currentFloor =2
column.elevatorsList[1].currentFloor =6
for elevator=colunm.requestElvator(3, 'Up')
elevator.requestFloor(7)
""""======================== End Scenario 1 =======================""""

"""" ==================================Scenario 2===================""""
for column = new column(1, 'online', 10, 2)
column.elevatorsList[0].currentFloor =10
column.elevatorsList[1].currentFloor =3

""""Part1"""
for elevator=column.requestElevator(1, 'Up')
elevator.requestFloor(6)

""""Part2""""
for elevator=column.requestElevator(3, 'Up')
elevator.requestFloor(5)

""""Part3"""
for elevator=column.requestElevator(9, 'Down')
elevator.requestFloor(2)

"""" ==================================End Scenario 2=================="""

""""=================================Scenario 3========================""""
for column = new column(1, 'online', 10, 2)
column.elevatorList[0].currentFloor= 10
column.elevatorList[1].currentFloor = 3
column.elevatorList[1].staus = 'Up'
column.elevatorList[1].destination = 6

""""Part 1""""
for.elevator=column.requestElevator(3, 'Down')
elevator.requestFloor(2)


""""Part 2""""
for.elevator=column.requestElevator(10, 'Down')
elevator.requestFloor(3)

""""==================================End Scenario 3===================="""


module.exports = Column, Elevator, CallButton, FloorRequestButton, Door