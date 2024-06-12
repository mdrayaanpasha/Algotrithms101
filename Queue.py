class Queue:
    def __init__(self,size):
        self.front=-1
        self.back=-1
        self.arr=[None] * size
        self.size=size
        
    def isFull(self):
        return self.back == self.size-1
    
    def isEmpty(self):
        return self.front == -1 or self.front > self.back
        
    def Enqueue(self,ele):
        if self.isFull():
            print("Your Queue is full!, can't insert: ",ele)
        else:
            if self.front == -1:
               self.front=0
            self.back+=1
            self.arr[self.back]=ele
   
                
            
            
    def Dequeue(self):
        if self.isEmpty():
            print("Your Queue is Empty!")
        else:
            self.arr[self.front]=None
            self.front+=1
            
            if self.front > self.back:
                self.front=self.back=-1
   
                
                
    def traverse(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            for i in range(self.front, self.back + 1):
                print(self.arr[i])
                
                
Q = Queue(6)
Q.Dequeue()
Q.Enqueue(4)
Q.Enqueue(5)
Q.traverse()
Q.Dequeue()
Q.Dequeue()
Q.Dequeue()
Q.traverse()
# print(Q.arr[0])
