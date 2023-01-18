class Stack():
    
    def __init__(self):
        self.stack=[]
        
    def get_stack_elements(self):
        return self.stack.copy()
    
    def add_element(self, element):
        self.stack.append(element)
    
    def remove_element(self, element):
        self.stack.remove(element)
     
    def add_many_element(self, element, n):
        for i in range(n):
            self.stack.append(element)
                    
    def remove_many_elements(self, n):
        if n <= self.get_size():
            for i in range(n):
                self.stack.pop()
        else:
            for i in range(self.get_size()):
                self.stack.pop()
   
    def get_size(self):
        return len(self.stack)
    
    def print_elements(self):
        for element in self.stack:
            print("Element: ", element)                  

def main():
    My_Stack = Stack()
    print(My_Stack.get_stack_elements())
    My_Stack.add_element("Figrst")
    print(My_Stack.print_elements())

if __name__ == '__main__':
    main()
