class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
    def is_empty(self):
         return len(self.items) == 0
         
    def push(self, url):
        self.items.append(url)
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop() # Menggunakan metode pop() untuk menghapus dan mengembalikan elemen terakhir
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1] # Mengakses elemen terakhir tanpa menghapusnya
        
    def size(self):
        return len(self.items)

history_stack = StackList()
history_stack.push("google.com")
history_stack.push("facebook.com")

print(f"Peek: {history_stack.peek()}") 
print(f"Size: {history_stack.size()}")
print(f"Pop: {history_stack.pop()}") 
print(f"Peek: {history_stack.peek()}") 
print(f"Size: {history_stack.size()}") 

