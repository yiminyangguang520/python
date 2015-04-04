__author__ = 'Administrator'
file1 = open("libraryall.txt", "a")
file2 = open("library5.txt", "r")
file1.write(file2.read())