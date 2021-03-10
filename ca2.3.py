class node:
    def __init__(self,data):
        self.next = None
        self.data = data
class link_list:
    def __init__(self):
        self.init_node = None
    def add_node(self,data):
        new_node = node(data)
        new_node.next = self.init_node
        self.init_node= new_node
    def print_datas(self):
        datas = ""
        n = self.init_node
        while 1:
            if n is None:
                break
            datas += str(n.data) + "->"
            n = n.next
        print(datas[:-2])

inp = input()
nums = inp.split('->')
linked_list = link_list()
linked_list_odd = link_list()
linked_list_even = link_list()
for i in nums:
    linked_list.add_node(int(i))
while linked_list.init_node is not None:
    temp_data = linked_list.init_node.data
    if temp_data %2 == 1:
        linked_list_odd.add_node(temp_data)
    else:
        linked_list_even.add_node(temp_data)
    linked_list.init_node = linked_list.init_node.next
linked_list_odd.print_datas()
linked_list_even.print_datas()
    