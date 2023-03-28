import os.path

fileName = "test.txt"

isFilePresent = os.path.isfile(fileName)
fileExists = os.path.exists(fileName)

print(fileExists)
