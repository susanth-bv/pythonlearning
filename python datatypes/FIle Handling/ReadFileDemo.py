testFile = open('test.txt', 'r')
# print(testFile.read())
print(testFile.readlines())
lines = testFile.readlines()
a = len(lines)
print (a)
testFile.close()


