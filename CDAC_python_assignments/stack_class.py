class Stack:
     def __init__(self):
         self.new_stack = []

     def push(self, item):
         self.new_stack.append(item)

     def pop(self):
         return self.new_stack.pop()

     def top(self):
         return self.new_stack[len(self.new_stack)-1]


        
    
