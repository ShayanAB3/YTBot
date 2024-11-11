from src.provider.provider import Provider
from src.helpers.path.path import Path

class Module(Provider):
    modules:list[str] = []

    def get_module_names(self) -> list[str]:
        module:list[str] = []
        path:Path = Path(self.dirname)

        for path_name in path.read(self.remove_paths,self.endswith):
            path.set_path(path_name)
            module_path = path.convert_path_to_module()
            if module_path not in self.remove_modules:
                module.append(module_path)
        return module

    def get_modules(self) -> list[str]:
        return self.get_module_names()