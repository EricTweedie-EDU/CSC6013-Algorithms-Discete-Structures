# Program that reads a list of people from a file called people.csv (contains 15 people), store the people in a stack.
# Ask the user repeatedly for a number between 1-4, according to the number pop that amount of people from the stack and pring the remaining.
# Prgram stops when the stack is empty

import csv

# Person class 
class Person:
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age = age
    def get_name(self):
        return self.name
    def get_FullName(self):
        return self.name + " " + self.famN
    def get_familyName(self):
        return self.famN
    def get_age(self):
        return self.age

# empty people dictionary
people = {}
def readPeople(fileName):
    infile = open(fileName, "r")
    for line in infile:
        info = line.split(",")
        people.update({info[0]: Person(info[1], info[2], int(info[3]))})
    return people

def printPeople(people):
    print("=======================")
    print("Nickname Name          ")
    print("=======================")
    for k in people.keys():
        print("{0:>9}    {1:<15}".format(k, people[k].get_FullName()))

# function that adds the people from the file to a stack
stack = []
def addPeople(people):
    for k in people.keys():
        stack.append(people[k].get_FullName())
    return stack


# asking the user for int input from 1-4 to remove that many people from the stack
def removePeople(stack):
    while True:
        x = int(input("Enter a number between 1-4:"))
        if x == 1:
            stack.pop()
            print(stack)
            if stack == []:
                print("Stack is empy of names.")
                break
        elif x == 2:
            stack.pop()
            stack.pop()
            print(stack)
            if stack == []:
                print("Stack is empy of names.")
                break
        elif x == 3:
            stack.pop()
            stack.pop()
            stack.pop()
            print(stack)
            if stack == []:
                print("Stack is empy of names.")
                break
        elif x == 4:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            print(stack)
            if stack == []:
                print("Stack is empy of names.")
                break
        else:
            print("Invalid input. Try again.")


def main():
    fileName = input("Enter the file name with people info: ")
    everyone = readPeople(fileName)
    printPeople(everyone)
    addPeople(people)
    removePeople(stack)

main()