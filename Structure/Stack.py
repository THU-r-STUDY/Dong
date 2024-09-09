# Stack list
stack = []
#Stack max size
max_size = 10
#is Full
def isFull(stack):
    return len(stack) == max_size
#is Empty
def isEmpty(stack):
    return len(stack) == 0

#push
def push(stack, item):
    if isFull(stack):
        print("Stack is Full.")
    else:
        stack.append(item)
        print("Data input to stack")

#pop
def pop(stack):
    if isEmpty(stack):
        print("Stack is Empty")
        return None
    else:
        return stack.pop()