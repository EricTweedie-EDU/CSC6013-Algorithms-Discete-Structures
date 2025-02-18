# program that reads a data file of numbers, stores them in an array and then sorts it
# take the array and sort it into a linkedlist and finally ask the user for an integer and if it is the list remove it, if not add it in the sorted place

# opening the data.txt file
# creating a list and sorting it from the file
data = open("data.txt").read().splitlines()
a = list(map(int, data))
a.sort()

# Classes for the node and linkedlist

class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None

class LinkedList:
    def __init__(self, d=None):
        if (d == None): # an empty list
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header
    def nextCurrent(self):
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header
    def resetCurrent(self):
        self.Current = self.Header
    def getCurrent(self):
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None
    def insertBeginning(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp
    def insertCurrentNext(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp
    def removeBeginning(self):
        if (self.Header is None): # if list is empty
            return None
        else:                     # if list not empty
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans
    def removeCurrentNext(self):
        if (self.Current.Next is None): # if there is no node
            return None                 #        after Current
        else:                           # if there is
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans
    def printList(self,msg="====="):
        p = self.Header
        print("=====",msg)
        while (p is not None):
            print(p.Data, end=" ")
            p = p.Next
        if (self.Current is not None):
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")
        input("----------------")
    
    def pos_search(self, x):
        Current = self.Header
        position = 0
        while Current != self.Current.Next:
            if Current.Data == x:
                return f"Value {x} found at position {position}."
            Current = Current.Next
            position += 1
        return f"Value {x} not found."
    
    def search(self, x):
        Current = self.Header
        while Current != self.Current.Next:
            if Current.Data == x:
                return True
            Current = Current.Next
        return False
    
    def search_and_modify(self, x):
        Current = self.Header
        prev = None
        found = False

    #search for the number
        while Current and Current.Data <= x:
            if Current.Data == x:
                found = True
                break
            prev = Current
            Current = Current.Next
    # if found remove the number
        if found:
            if prev:
                prev.Next = Current.Next
            else:
                self.Header = Current.Next
                Current = None
        else:  # if not found, insert the number
            new_node = Node(x)
            if prev:
                new_node.Next = prev.Next
                prev.Next = new_node
            else:
                new_node.Next = self.Header
                self.Header = new_node

def main():
    L = LinkedList()
    for i in reversed(a):
        L.insertBeginning(i)
    L.printList()
    x = int(input("Enter a number: "))
    print(L.search(x))
    print(L.pos_search(x))
    L.search_and_modify(x)             
    L.printList()

main()
