class Employees:
    def __init__(self,name,last)->None:
        self.name = name
        self.last = last

class Supervisor(Employees):
    def __init__(self,name,last,password)->None:
        super().__init__(self,name,last)
        self.password = password

class Chefs(Employees):
    def leaveRequest(self, days):
         return "May I take a leave for " + str(days)+" days"


adrian = Supervisor("Adrian","A","apple")
Emily = Chefs("Emily","A")
Dry = Chefs("Dry","A")

print(Emily.leaveRequest(3))
