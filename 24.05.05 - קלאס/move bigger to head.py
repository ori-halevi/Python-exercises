import StackClassUsingLinkedList
def move_bigger_to_head(some_stack: StackClassUsingLinkedList.Stack):
    new_stack = StackClassUsingLinkedList.Stack()
    bigger = some_stack.peek()
    while some_stack.peek() is not None:
        i = some_stack.pop()
        if some_stack.peek():
            if i > some_stack.peek():
                bigger = i
            else:
                new_stack.push(i)
        else:
            new_stack.push(i)
    new_stack.push(bigger)
    return new_stack

stack = StackClassUsingLinkedList.Stack()
stack.push(3)
stack.push(2)
stack.push(5)
stack.push(7)
stack.push(1)
print(stack)

# while stack.peek() is not None:
#     print(stack.pop())


print(move_bigger_to_head(stack))