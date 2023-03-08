class Person:

    def __int__(self, firstName, lastName, city):
        self.firstName = firstName
        self.lastName = lastName
        self.city = city

    # trainingTopic = "Python"
    # trainingLevel = "Basics to Advanced"
    # trainingDuration ="8 weeks"
    # dailyHours = "2 hours"
#
# training = MyTraining()
# print(training.trainingTopic)
# print(training.trainingLevel)
# print(training.trainingDuration)
# print(training.dailyHours)

person1 = Person("Saurabh" , "deshpande" , "pune")
print("First Name : " ,person1.firstName)
print("Last Name : " ,person1.lastName)
print("city :" , person1.city )

person2 = Person("susanth" , "Bondalapati" , "Usa")
print("First Name : " ,person2.firstName)
print("Last Name : " ,person2.lastName)
print("city :" , person2.city )

