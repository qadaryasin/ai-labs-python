# Question 1:
# Implement Stack using Python. 

class Stack:
    def __init__(self):
        self.stack=[]      #here stack is a list in python 
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def top(self):
        if self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        if len(self.stack)==0:
              return True
        else:
            return False
        
    def display(self):
        print("Stack from top to bottom",self.stack[::-1])

# Example usage
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
print("Popped:",s.pop())
s.display



# Question 2
# Implement Queue using Python. 


class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None 
    
    def is_empty(self):
        if len(self.queue)==0:
            return True
        return False
    
    def display(self):
        print("Queue is: "self.queue)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("Dequeued:", q.dequeue())
q.display()




# Question 3
# Binary search in python.. 

def binary_search(arr,element):
        start=0
        end=len(arr)-1

        while end>=start:
           
            mid=(start+end) //2  # // operator rounds down to the nearest whole number.
            
            if arr[mid]==element:
                 return mid
            elif arr[mid]>element:
                 end=mid-1
            else:
                  start=mid+1

        return -1

# Example usage
data = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binary_search(data, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found")