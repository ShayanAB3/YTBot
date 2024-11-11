from typing import TypeVar, Generic

T = TypeVar('T')

class Queue(Generic[T]):
    quare:list[T] = []
    def set(self,data:T):
        self.quare.append(data)
    
    def get(self) -> T:
        return self.quare.pop(0)
    
    def clear(self):
        self.quare = []