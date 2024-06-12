class Stack:
    def __init__(self,size):
        self.size=size
        self.arr= [None] * size
        self.top=-1
        
    def isFull(self):
        return self.top>=self.size -1
    
    def isEmpty(self):
        return self.top < 0
        
    def push(self,ele):
        if self.isFull():
            print("Your Stack is full sorry, cant insert: ",ele)

        else:
            self.top+=1
            self.arr[self.top]=ele
           
    
    def pop(self):
        if self.isEmpty():
            print("There's nothing in stack to pop!")
        else:
            self.arr[self.top]=None
 
 
            
   
    def traverse(self):
        for i in range(self.size):
            print(self.arr[i])
            
    
Stack1=Stack(5)

Stack1.push(2)
Stack1.push(3)
Stack1.push(5)
Stack1.push(6)
Stack1.push(9)
Stack1.pop()
        
        
    
