class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        return self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        return "["+', '.join(reversed(self.data))+"]"
        # return f"[{', '.join(self.data[::-1])}]"


stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print(stack.is_empty())
print(stack)

# ss = Stack()
# [ss.push(str(randint(0, 100))) for _ in range(15)]
# print(ss)
# print(ss.pop())
# print(ss.peek())
# print(ss.is_empty())
# print(ss)