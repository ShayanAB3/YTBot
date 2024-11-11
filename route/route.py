from route.command.slash import Slash
from route.command.prefix import Prefix

class Route:
    slash = Slash()
    prefix = Prefix()
    
route = Route()