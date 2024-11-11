from discord.ext.commands import Context

class Context:
    def set(self,ctx:Context):
        self.context = ctx
    def get(self):
        return self.context

context = Context()