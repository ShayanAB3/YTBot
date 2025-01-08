from typing import TypeVar, Generic

T = TypeVar('T')

class Queue(Generic[T]):
    queue:list[T] = []
    def set(self,data:T):
        self.queue.append(data)
    
    def get(self) -> T:
        return self.queue.pop(0)
    
    def peek(self) -> T:
        return self.queue[0]

    def clear(self):
        self.queue = []

    def len(self) -> int:
        return len(self.queue)
    
    def extend(self,data:list):
        self.queue.extend(data)