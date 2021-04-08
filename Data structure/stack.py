class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s: str):
    match = {'}': "{", ']': '[', ")": '('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('[{()[]()[{}]{}}]'))
print(brace_match('[{()}]'))
print(brace_match('[{]'))
