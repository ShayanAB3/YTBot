from abc import ABC, abstractmethod

class Reason(ABC):
    
    @abstractmethod
    def get()-> dict[str | int, str | int | bool]:
        pass