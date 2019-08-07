import sys
import csv
import datetime
import os.path
from os import path

def createDb(filename):
  print("Creating %s" %(filename))
  with open(filename, "w") as csvFile:
    fileWriter = csv.writer(csvFile, delimiter=',')
    fileWriter.writerow(['Name'])
    fileWriter.writerow(['Student1'])
    fileWriter.writerow(['Student2'])
    fileWriter.writerow(['Student3'])

def updateDb(filename, name):
  attendance=raw_input("Enter attendance, type P for present and type A for absent:")
  print "Attendance sheet updated!"

def query(dbFile, name):
  found = False 
  if found:
    print("Query %s in %s" %(name, dbFile))
  return found 

def updateAttendance(name):
  filename = "attendance.csv"
  if (False == path.exists(filename)):
    createDb(filename)
  if (query(filename, name)):
    updateDb(filename, name)
  else:
    print("Query on %s failed!" %(filename))

def main():
  print "This python file keep track of attendence of students in class room!"
  name = raw_input("Enter your name:")
  updateAttendance(name)

if __name__ == "__main__":
  main()
    
