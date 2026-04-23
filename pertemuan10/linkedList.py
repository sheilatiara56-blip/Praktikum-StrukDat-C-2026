class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.top is None
    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count +=1
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        
        removed_url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return removed_url
    def peek(self):
        if self.is_empty():
            return None
        return self.top.url
    def size(self):
        return self.count


history_stack = StackLinkedList()
history_stack.push("google.com")
history_stack.push("facebook.com")

print(f"Peek: {history_stack.peek()}") 
print(f"Size: {history_stack.size()}")
print(f"Pop: {history_stack.pop()}") 
print(f"Peek: {history_stack.peek()}") 
print(f"Size: {history_stack.size()}") 
