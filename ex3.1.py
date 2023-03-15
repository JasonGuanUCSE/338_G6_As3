import sys

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.val

    def is_empty(self):
        return self.size == 0

def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operand2 is None:
                print("Invalid expression")
                return None
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 // operand2)
        elif token == '(':
            continue
        elif token == ')':
            continue
        else:
            print("Invalid token")
            return None
    if stack.size != 1:
        print("Invalid expression")
        return None
    return stack.pop()

if __name__ == '__main__':
    expression = sys.argv[1]
    result = evaluate_expression(expression)
    if result is not None:
        print(result)
