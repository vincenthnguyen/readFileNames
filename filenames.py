import os
import json

print("Enter the absolute file path to the directory you need filenames for...")
print("(Ex: 'C:\Users\Vincent\Desktop')")
filenamesPath = input("Enter path: ")
print("Enter the absolute file path to the directory where you want the text file to be generated...")
outputPath = os.path.join(input("Enter path: "), "filenames.txt")
output = open(outputPath, 'w')

files = []

# first pass to grab and fix names
for file in os.listdir(filenamesPath):
    # Note that these are specific to a friend's issues.
    if file[2] == ".":
        file = "0" + file
    elif file[1] == '.':
        file = "00" + file
    files.append(file)
files.sort() # sort

# second pass to write to file
for file in files:
    output.write("%s\n" % file)
output.close()

print("Finished! Exported to " + outputPath)