class organisation:

    def __init__(self):

        self._assignment = "python training"

class Employee(organisation):

    def __init__(self, name, salary):

        self.name = name

        self.__salary = salary
        super().__init__()

    def displayDetails(self):
        print("Name = ", self.name, "salary =", self.__salary)
        print("printing assignment name from Organisation class :", self._assignment)

emp = Employee("susanth", 90000)
emp.displayDetails()