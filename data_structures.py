#!/usr/bin/env python


from queue import Queue
from typing import Any


class FifoQueue(object):
    """FIFO queue made out of two stacks.
    
    This queue has an enqueue efficiency of O(1), but a worst-case
    dequeue efficiency of O(n) where n is the number of items currently in the
    queue.
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


class Stack(object):
    """Stack made out of two queues.
    
    """
    
    def __init__(self) -> None:
        self.input_queue = Queue()
        self.output_queue = Queue()
        
    def push(self, el: Any) -> None:
        pass
    
    def pop(self) -> Any:
        pass
    
    def size(self) -> int:
        pass

if __name__ == '__main__':
    # Problem 1:
    # Create a FIFO queue using only stacks.
    input = ['a', 'b', 'c']
    output = []
    queue = FifoQueue()
    for item in input:
        queue.enqueue(item)
    while queue.size() > 0:
        output.append(queue.dequeue())
    print('Problem #1:\nInput order:\t{}\nOutput order:\t{}'.format(
        input, output))
    
    # Problem 2:
    # Create a stack using only FIFO queues.
    
    # Problem 3:
    # Implement singly linked list.
    
    # Problem 4:
    # Implement a doubly linked list.
    pass