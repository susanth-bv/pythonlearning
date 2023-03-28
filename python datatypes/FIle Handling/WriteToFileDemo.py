textToWrite = "This sample content wil be written to a file with name write_demo.txt"
fileToWrite = open("write_demo.txt", 'w')
fileToWrite.write(textToWrite)
print("Completed the file writing part")
fileToWrite.close()