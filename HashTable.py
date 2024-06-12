class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def delete(self,data):
        temp=self.head
        prev=None
        if temp is not None:
            if temp.data==data:
                self.head=temp.next
                temp=None
                return
            
        
        while temp is not None:
             if temp.data==data:
                 break
             prev=temp
             temp=temp.next
             
             
        if temp is None:
            print("we couldn't find!")
        else:
            prev.next=temp.next
            temp=None
             
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
            
    def search(self,d):
        temp=self.head
        
        found=False
        while temp is not None:
            if temp.data==d:
                found=True
                break
            temp=temp.next
        
        if found:
            print("Found it!")
        else:
            print("Didn't find!")
class HashTable:
    def __init__(self,size):
        self.size=size
                

        self.table=[LinkedList()  for _ in range(size)]
        
    
    def insert(self,data):
        insertcol = data % self.size
        self.table[insertcol].insert(data)
        
    def delete(self,data):
        delcol=data%self.size
        self.table[delcol].delete(data)
    
    def search(self,data):
        col=data%self.size
        self.table[col].search(data)
        
    def traverse(self):
        for i in range(self.size):
            print(self.table[i].traverse())
            
            
            
ht = HashTable(10)
ht.insert(5)
ht.insert(15)
ht.insert(25)
ht.traverse()
ht.search(15)
ht.delete(15)
ht.traverse()
ht.search(15)
            
        
                
                
            
