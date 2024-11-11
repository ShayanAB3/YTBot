from middleware.kernel import kernel as kernel_middleware
from route.facade.facade import decorator

class Middleware:
    name:str
    def set_middleware(self,middleware:str):
        if middleware and self.name:
            kernel_middleware.set_cmd_middleware(self.name,middleware)
        return decorator