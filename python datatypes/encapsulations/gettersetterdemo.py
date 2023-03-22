class Customer:

    def __init__(self, fname, lname, ssn):
        self.fname = fname
        self.lname = lname
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, ssn):
        self.__ssn = ssn

customer1 = Customer("susanth", "bondalapati", "444-333-rrr")
print("current ssn for customer1 is:", customer1.get_ssn())

customer1.set_ssn("333-111-777")
print("current ssn for customer1 is:", customer1.get_ssn())