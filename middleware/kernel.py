from middleware.handlers.first_middleware import FirstMiddleware

from src.middleware.cmdkernel import CmdKernel
from middleware.middleware import Middleware

class Kernel(CmdKernel):
    middleware:dict[str,Middleware] = {
        "first_middleware": FirstMiddleware,
    }

kernel = Kernel()