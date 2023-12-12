from array_stack import ArrayStack
from linked_stack import LinkedStack
from stack_using_queues import StackUsingQueues

def main():
    # Example usage of ArrayStack
    array_stack = ArrayStack(5)
    array_stack.push(1)
    array_stack.push(2)
    array_stack.push(3)

    print("ArrayStack size:", array_stack.size())
    print("ArrayStack top element:", array_stack.peek())

    while not array_stack.is_empty():
        print("Popped from ArrayStack:", array_stack.pop())

    print("ArrayStack size after popping:", array_stack.size())

    # Example usage of LinkedStack
    linked_stack = LinkedStack()
    linked_stack.push("One")
    linked_stack.push("Two")
    linked_stack.push("Three")

    print("\nLinkedStack size:", linked_stack.size())
    print("LinkedStack top element:", linked_stack.peek())

    while not linked_stack.is_empty():
        print("Popped from LinkedStack:", linked_stack.pop())

    print("LinkedStack size after popping:", linked_stack.size())

    # Example usage of StackUsingQueues
    stack_using_queues = StackUsingQueues()
    stack_using_queues.push('A')
    stack_using_queues.push('B')
    stack_using_queues.push('C')

    print("\nStackUsingQueues size:", stack_using_queues.size())
    print("StackUsingQueues top element:", stack_using_queues.peek())

    while not stack_using_queues.is_empty():
        print("Popped from StackUsingQueues:", stack_using_queues.pop())

    print("StackUsingQueues size after popping:", stack_using_queues.size())


if __name__ == "__main__":
    main()
