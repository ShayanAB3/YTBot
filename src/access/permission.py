from access.check_failure_handler import CheckFailureHandler
from src.reason.permission import Permission as ReasonPermission

class Permission(CheckFailureHandler):
    permission = ReasonPermission()
