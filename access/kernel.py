from access.permissions.admin_permission import AdminPermission
from access.check_failure_handler import CheckFailureHandler
from access.roles.admin_role import AdminRole
from src.access.access_kernel import AccessKernel

class Kernel(AccessKernel):
    permissions:dict[str,CheckFailureHandler] = {
        "administrantor_false": AdminPermission
    }

    roles:dict[str,CheckFailureHandler] = {
        "administrantor_role": AdminRole
    }

kernel = Kernel()