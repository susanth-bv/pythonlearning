textToWrite = "opening a new file"
fileToWrite = open("write_demo.txt", 'a')
fileToWrite.write(textToWrite)
print("Completed the file writing part")
fileToWrite.close()