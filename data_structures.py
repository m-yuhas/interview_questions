#!/usr/bin/env python


from queue import Queue
from typing import Any, Union


class FifoQueueOfStacks(object):
    """FIFO queue made out of two stacks.
    
    This queue has an enqueue efficiency of O(1), but a worst-case
    dequeue efficiency of O(n) where n is the number of items currently in the
    queue.
    
    Unlike Python's built-in queue class, this implementation of a queue is not
    thread safe.
    """
    
    def __init__(self) -> None:
        self.input_stack = []
        self.output_stack = []
    
    def enqueue(self, el: Any) -> None:
        """Enqueue an element.
        
        Arguments:
            el: Any
                The element to enqueue
        """
        self.input_stack.append(el)
    
    def dequeue(self) -> Any:
        """Dequeue the next element.
        
        Returns:
            Any: The earliest element that was enqueued
            
        Raises:
            IndexError:
                if the queue is empty
        """
        if len(self.output_stack) > 0:
            return self.output_stack.pop()
        while len(self.input_stack) > 0:
            self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()
    
    def size(self) -> int:
        """Get the size of the queue.
        
        Returns:
            int: The size of the queue
        """
        return len(self.input_stack) + len(self.output_stack)


class StackOfQueues(object):
    """Stack made out of two queues.
    
    This stack has a push efficiency of O(1) and a worse case pop efficiency of
    O(n) where n is the number of elements in the stack.
    
    This stack is not thread safe.
    """
    
    def __init__(self) -> None:
        self.input_queue = Queue()
        self.output_queue = Queue()
        
    def push(self, el: Any) -> None:
        """Push an element onto the stack.
        
        Arguments:
            el: Any
                The element to push onto the stack.
        """
        self.input_queue.put(el)
    
    def pop(self) -> Any:
        """Pop an element from the stack.
        
        Returns:
            Any: The latest element that was pushed onto the stack
        
        Raises:
            Empty: If the stack is empty
        """
        while self.input_queue.qsize() > 1:
            self.output_queue.put(self.input_queue.get())
        while not self.output_queue.empty():
            self.input_queue.put(self.output_queue.get())
        return self.input_queue.get_nowait()
    
    def size(self) -> int:
        """Get the size of the stack.
        
        Returns:
            int: The size of the stack
        """
        return self.input_queue.qsize() + self.output_queue.qsize()

class FifoQueueOfLinkedList(object):
    """FIFO Queue implemented with a doubly-linked list.
    
    This queue has an enqueue efficiency of O(1) and a dequeue efficiency of
    O(1).
    
    This queue is not thread safe.
    """
    
    class Node(object):
        """Node for a doubly-linked list.
        
        Arguments:
            value: Any
                The value stored in this node
            previous: Union['Node', None]
                The previous node in the linked list
            next: Union['Node', None]
                The next node in the linked list
        """
        
        def __init__(self, value: Any,
                     previous: Union['Node', None],
                     next: Union['Node', None]) -> None:
            self.value = value
            self.previous = previous
            self.next = next

    def __init__(self) -> None:
        self.tail = self.Node(None, None, None)
        self.head = self.Node(None, None, self.tail)
        self.tail.previous = self.head
        
    def enqueue(self, el: Any) -> None:
        """Enqueue an element.
        
        Arguments:
            el: Any
                Element to enqueue
        """
        node = self.Node(el, self.head, self.head.next)
        node.next.previous = node
        self.head.next = node
        
    def dequeue(self) -> Any:
        """Dequeue an element.
        
        Returns:
            Any: the earliest element that arrived in the queue
            
        Raises:
            Empty: if the queue is empty
        """
        if self.tail.previous == self.head:
            raise Empty('Queue is empty.')
        el = self.tail.previous.value
        self.tail.previous = self.tail.previous.previous
        self.tail.previous.next = self.tail
        return el
    
    def size(self) -> int:
        """Return the size of the queue.
        
        Returns:
            int: the current size of the queue
        """
        size = 0
        current_node = self.head.next
        while current_node.next is not None:
            size += 1
            current_node = current_node.next
        return size


class StackOfLinkedList(object):
    """Stack implemented with a singly-linked list.
    
    This stack has a push efficiency of O(1) and a pop efficiency of O(1).
    
    This stack is not thread safe.
    """
    
    class Node(object):
        """Node for a singly-linked list.
        
        Arguments:
            value: Any
                The value stored in this node
            next: Union['Node', None]
                The next node in the linked list
        """
        
        def __init__(self, value: Any, next: Union['Node', None]) -> None:
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self.head = self.Node(None, None)

    def push(self, el: Any) -> None:
        """Push an element onto the stack.
        
        Arguments:
            el: Any
                The element to push onto the stack
        """
        self.head.next = self.Node(el, self.head.next)

    def pop(self) -> Any:
        """Pop an element from the stack.
        
        Returns:
            Any: the latest element pushed to the stack

        Raises:
            Empty: if the stack is empty
        """
        if self.head.next is None:
            raise Empty('Stack is empty.')
        el = self.head.next.value
        self.head.next = self.head.next.next
        return el

    def size(self) -> int:
        """Return the size of the stack.

        Returns:
            int: the size of the stack
        """
        size = 0
        current_node = self.head
        while current_node.next is not None:
            size += 1
            current_node = current_node.next
        return size


if __name__ == '__main__':
    # Problem 1:
    # Create a FIFO queue using only stacks.
    input = ['a', 'b', 'c']
    output = []
    queue = FifoQueueOfStacks()
    for item in input:
        queue.enqueue(item)
    while queue.size() > 0:
        output.append(queue.dequeue())
    print('Problem #1:\nInput order:\t{}\nOutput order:\t{}'.format(
        input, output))
    
    # Problem 2:
    # Create a stack using only FIFO queues.
    input = ['a', 'b', 'c']
    output = []
    stack = StackOfQueues()
    for item in input:
        stack.push(item)
    while stack.size() > 0:
        output.append(stack.pop())
    print('Problem #2:\nInput order:\t{}\nOutput order:\t{}'.format(
        input, output))
    
    # Problem 3:
    # Implement a FIFO queue using a doubly linked list.
    input = ['a', 'b', 'c']
    output = []
    queue = FifoQueueOfLinkedList()
    for item in input:
        queue.enqueue(item)
    while queue.size() > 0:
        output.append(queue.dequeue())
    print('Problem #3:\nInput order:\t{}\nOutput order:\t{}'.format(
        input, output))
    
    # Problem 4:
    # Implement a stack using a singly linked list.
    input = ['a', 'b', 'c']
    output = []
    stack = StackOfLinkedList()
    for item in input:
        stack.push(item)
    while stack.size() > 0:
        output.append(stack.pop())
    print('Problem #4:\nInput order:\t{}\nOutput order:\t{}'.format(
        input, output))