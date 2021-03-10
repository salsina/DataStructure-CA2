class node:
    def __init__(self,data):
        self.next = None
        self.data = data
class stack:
    def __init__(self):
        self.init_node = None
    def push(self,data):
        new_node = node(data)
        new_node.next = self.init_node
        self.init_node= new_node
    def pop(self):
        if self.init_node is not None:
            self.init_node = self.init_node.next
    def peek(self):
        if self.init_node is not None:
            return self.init_node.data
    
def change_char(inp,j,char):
    return inp[:j] + char + inp[j+1:]
    
stack = stack()
inp = input()
stack.push(inp)

inp_number = stack.peek()
while 1:
    inp_number = stack.peek()
    if inp_number is None:
        break
    index = inp_number.find("?")
    if index == -1:
        print(inp_number)
        stack.pop()
        continue
    stack.pop()
    inp_number = change_char(inp_number,index,'0')
    stack.push(inp_number)
    inp_number = change_char(inp_number,index,'1')
    stack.push(inp_number)
                