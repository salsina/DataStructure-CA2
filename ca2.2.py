class node:
    def __init__(self,data):
        self.next = None
        self.data = data

class queue:
    def __init__(self):
        self.last_node = None
        self.first_node = None
    def enqueue(self,data):
        new_node = node(data)
        if self.first_node == None:
            self.last_node = new_node
            self.first_node = new_node
        else: 
            self.last_node.next = new_node
            self.last_node= new_node
    def dequeue(self):
        if self.first_node is not None:
            save = self.first_node
            self.first_node = self.first_node.next
            return save.data
    def front(self):
        if self.first_node is not None:
            return self.first_node.data

    
def print_output(map,Q):
    while Q.front() is not None:
        line = Q.front()
        output_line = ""
        for i in line:
            output_line +=i + " "
        print(output_line)
        Q.dequeue()
        
def is_empty(m,n,map,map_color):
    if m<0 or m>=len(map) or n<0 or n>=len(map[m]) or map[m][n] !=map_color:
        return False
    return True
def change_color(color,m,n,map):
    map[m][n] = color
    
inp_ask = input()
Q = queue()
split_inp = inp_ask.split()
N = int(split_inp[0])
M = int(split_inp[1])
color = split_inp[2]
map = []
while 1:
    try:
        inp = input()
        line = inp.split()
        map.append(line)
    except EOFError:
        break

map_color = map[M][N]
Q.enqueue([M,N])
while Q.front() is not None:
    [m,n] = Q.dequeue()
    if map[m][n] is color:
        continue
    change_color(color,m,n,map)
    if is_empty(m-1,n,map,map_color):
        Q.enqueue([m-1,n])
    if is_empty(m,n-1,map,map_color):
        Q.enqueue([m,n-1])
    if is_empty(m+1,n,map,map_color):
        Q.enqueue([m+1,n])
    if is_empty(m,n+1,map,map_color):
        Q.enqueue([m,n+1])
        
for i in range(len(map)):
    Q.enqueue(map[i])    
print_output(map,Q)