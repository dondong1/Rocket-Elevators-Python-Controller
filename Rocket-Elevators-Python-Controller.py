elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1

class Column(): 
    def __init__ (self, _id, _status, amountOfFloors, amountOfElevators) :
        self.ID = _id   
        self.status = _status 
        self.amountOfFloors = amountOfFloors
        self.amountOfElevators = amountOfElevators
        self.elevatorsList = []
        self.callButtonsList = []

        self.createElevators()
        self.createCallButtons(amountOfFloors)
    
    def createCallButtons(self, amountOfFloors): 
        buttonFloor = 1
        for i in range(self.amountOfFloors):
            if buttonFloor < self.amountOfFloors :
                self.callButtonsList.append(CallButton(i +1, 'OFF', buttonFloor +1 , 'Up'))
            
            if buttonFloor > 1 :
                self.callButtonsList.append(CallButton(i +1 , 'OFF', buttonFloor +1 , 'Down'))
            

    def createElevators(self): 
        for i in range(self.amountOfElevators): 
            self.elevatorsList.append(Elevator(i + 1, 'idle', self.amountOfFloors, 1))
            

    def requestElevator(self, floor, direction): 
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
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
        print()
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
    def __init__ (self, _id, _status, amountOfFloors, _currentFloor):
        self.ID = _id
        self.status = _status
        self.amountOfFloors = amountOfFloors
        self.currentFloor = _currentFloor
        self.direction = "none"
        self.door = Door (_id, 'closed')
        self.floorRequestButtonsList = []
        self.floorRequestList = []
        self.createFloorRequestButtons(amountOfFloors)
        self.overweight = 0
    def createFloorRequestButtons(self, amountOfFloors): 
        for i in range(self.amountOfFloors):
            self.floorRequestButtonsList.append(FloorRequestButton(i + 1, 'OFF', i +1))
            
     
    def requestFloor(self, floor): 
        self.floorRequestList.append(floor)
        self.sortFloorList()
        self.move()
        self.operateDoors()

    def move(self):
        while len(self.floorRequestList) != 0:
            destination = self.floorRequestList[0]
            self.status = 'moving'
            if self.currentFloor < destination: 
                self.direction = 'Up'
                while self.currentFloor < destination : 
                    self.currentFloor+=1
                    print("       Elevator"+ str(self.ID) + " move to current floor " + str(self.currentFloor))
            elif self.currentFloor > destination :
                self.direction = 'Down'
                while self.currentFloor > destination : 
                    self.currentFloor-=1
                    print("       Elevator"+ str(self.ID) + " move to current floor " + str(self.currentFloor))
            self.status = 'stopped'
            self.floorRequestList.pop()
        
    def sortFloorList(self):
        if  self.direction == 'Up' :
            self.floorRequestList.sort()
         
        else:
            self.floorRequestList.sort(reverse = True)
      #fixing 131 - in des order.   
    def operateDoors(self):
        self.doorStatus = 'opened'
        print(self.doorStatus)
        if not(self.overweight) : 
            self.door.Status = 'closing'
            if not(self.door.obstruction) : 
                self.door.Status = 'closed'
                print(self.door.Status)
            else:
                self.door.obstruction = False
                self.operateDoors() 
               
        else:
            while self.overweight: 
                self.overweight = False 
            self.operateDoors()
 
class CallButton(object): 
    def __init__(self, _id, _status, floor, direction):
        self.ID = _id
        self.status = _status
        self.floor = floor
        self.direction = direction
        
class FloorRequestButton(object):
    def __init__ (self, _id, _status, floor):
        self.ID = _id 
        self.status = _status 
        self.floor = floor
       

class Door(object):  
    def __init__(self, _id, _status): 
        self.ID = _id 
        self.status = _status  
        self.obstruction = False
          


#========================Scenario 1 =======================
''' ******* CREATE SCENARIO 1 ******* '''
def scenario1(): 
    print()
    print("****************************** SCENARIO 1: ******************************")
    columnScenario1 = Column(1, 'online', 10, 2)  
    columnScenario1.elevatorsList[0].floor = 2 #floor where the elevator 1 is
    columnScenario1.elevatorsList[1].floor = 6 #floor where the elevator 2 is
    
    print()
    print("Person 1: (elevator 1 is expected)")
    elevator = columnScenario1.requestElevator(3, 'Up') #parameters (requestedFloor, buttonDirection.UP/DOWN)
    elevator.requestFloor(7) #parameters (requestedFloor, requestedColumn)
    print("==================================")

''' ******* CREATE SCENARIO 2 ******* '''
def scenario2(): 
    print()
    print("****************************** SCENARIO 2: ******************************")
    columnScenario2 = Column(1, 'online', 10, 2)
    columnScenario2.elevatorsList[0].floor = 10
    columnScenario2.elevatorsList[1].floor = 3
    
    print()
    print("Person 1: (elevator 2 is expected)")
    elevator = columnScenario2.requestElevator(1, 'Up')
    elevator.requestFloor(6)
    print("----------------------------------")
    print()
    print("Person 2: (elevator 2 is expected)")
    elevator3 = columnScenario2.requestElevator(3, 'Up')
    elevator3.requestFloor(5)
    print("----------------------------------")
    print()
    print("Person 3: (elevator 1 is expected)")
    elevator1 = columnScenario2.requestElevator(9, 'Down')
    elevator1.requestFloor(2)
    print("==================================")

''' ******* CREATE SCENARIO 3 ******* '''
def scenario3(): 
    print()
    print("****************************** SCENARIO 3: ******************************")
    columnScenario3 = Column(1, 'online', 10, 2)
    columnScenario3.elevatorsList[0].floor = 10
    columnScenario3.elevatorsList[1].floor = 3
    columnScenario3.elevatorsList[1].status = 'Up'

    
    print()
    print("Person 1: (elevator 1 is expected)")
    elevator = columnScenario3.requestElevator(3, 'Down')
    elevator.requestFloor(2)
    print("----------------------------------")    
    print()

    # 2 minutes later elevator 1(B) finished its trip to 6th floor
    columnScenario3.elevatorsList[1].floor = 6
    columnScenario3.elevatorsList[1].status = 'idle'

    print("Person 2: (elevator 2 is expected)")
    elevator1 = columnScenario3.requestElevator(10, 'Down')
    elevator1.requestFloor(3)
    print("==================================")


''' -------- CALL SCENARIOS -------- '''
scenario1()
scenario2()
scenario3()

