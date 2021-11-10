#Apartment.py
#Nealson Setiawan
#rent -> meters -> condition
class Apartment:

    def __init__(self,rent=0,metersFromUCSB=0,condition="N/A"):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(\
            self.getRent(),self.getMetersFromUCSB(),self.getCondition())
    
    def __gt__(self,rhs):
        if(self.getRent() > rhs.getRent()):
            return True
        elif(self.getRent() < rhs.getRent()):
            return False
        else:
            if(self.getMetersFromUCSB() > rhs.getMetersFromUCSB()):
                return True
            elif(self.getMetersFromUCSB() < rhs.getMetersFromUCSB()):
                return False
            else:
                scoreSelf = 0
                scoreRhs = 0
                if(self.getCondition() == "average"):
                    scoreSelf = 1
                elif(self.getCondition() == "excellent"):
                    scoreSelf = 2

                if(rhs.getCondition() == "average"):
                    scoreRhs = 1
                elif(rhs.getCondition() == "excellent"):
                    scoreRhs = 2

                if(scoreSelf < scoreRhs):
                    return True
                elif(scoreSelf > scoreRhs):
                    return False

    def __lt__(self,rhs):
        if(self.getRent() < rhs.getRent()):
            return True
        elif(self.getRent() > rhs.getRent()):
            return False
        else:
            if(self.getMetersFromUCSB() < rhs.getMetersFromUCSB()):
                return True
            elif(self.getMetersFromUCSB() > rhs.getMetersFromUCSB()):
                return False
            else:
                scoreSelf = 0
                scoreRhs = 0
                if(self.getCondition() == "average"):
                    scoreSelf = 1
                elif(self.getCondition() == "excellent"):
                    scoreSelf = 2

                if(rhs.getCondition() == "average"):
                    scoreRhs = 1
                elif(rhs.getCondition() == "excellent"):
                    scoreRhs = 2

                if(scoreSelf > scoreRhs):
                    return True
                elif(scoreSelf < scoreRhs):
                    return False
    
    def __eq__(self,rhs):
        if((self.getRent() == rhs.getRent()) and (self.getMetersFromUCSB == \
            rhs.getMetersFromUCSB()) and (self.getCondition() == rhs.getCondition())):
            return True
        else:
            return False