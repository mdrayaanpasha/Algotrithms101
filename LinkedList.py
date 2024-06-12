class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,ele):
        temp = Node(ele)
        temp.next=self.head
        self.head=temp
        
    def delete(self,ele):

        prev=None
        temp=self.head
        
        if temp is not None:
            if temp.data==ele:
                self.head=temp.next
                temp=None
                print("deleted")
        
        while temp is not None:
            if temp.data==ele:
                break
            prev=temp
            temp=temp.next
            
        if temp == None:
            print("no couldnt find it!")
        else:
            prev.next=temp.next
            temp=None
            print("done deleted")
            
    def search(self,ele):
        null=None
    
        temp=self.head
        found=False
        while temp is not null:
            if temp.data==ele:
                found=True
                break
            

        
        print(result = "found!" if found else "Coudln't Find")
            
    def traverse(self):
        temp=self.head
        
        while temp.next!=None:
            print(temp.data)
            temp=temp.next
            
ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.delete(3)
ll.traverse()
