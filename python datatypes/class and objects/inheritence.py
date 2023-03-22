class Person:

    def __init__(self, firstname, lastname, city, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.gender = gender

    def printPersonDetails(self):
            print("person details :", self.firstname, self.lastname, self.city, self.gender)

class Employee(Person):

    def __init__(self, firstname, lastname, city,gender):
        super().__init__( firstname, lastname, city,gender)
        self.comany = company
        self.salary = salary

emp1 = Employee("susanth", "bondalapati", "arlington","male")
emp1.printPersonDetails()
