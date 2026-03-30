class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_value = Node(value)
        if not self.head:
            self.head = new_value
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_value   

    def print(self):
        current = self.head
        while current:
            print(current.value, end="  ")
            current = current.next
        print("None")   

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.value 

linked = Linkedlist()
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)
linked.append(5)
linked.append(6)

linked.print()
print("middle node:", linked.find_middle())
# 1 2 3 4 5 6
#Reverse linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_data = Node(data)
        if not self.head:
            self.head = new_data
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_data

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("None")

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

# Test
ll = Linkedlist()
ll.append(3)
ll.append(2)
ll.append(1)

ll.print_list()
ll.reverse()
ll.print_list()