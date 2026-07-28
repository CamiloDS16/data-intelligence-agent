class ToolRegistry:
    def __init__(self):
        self.storage = {}

    def register(self, name, func, description):
        self.storage[name] = {"function": func, 
                              "description": description}

    def get(self, name):
        if name not in self.storage:
            raise KeyError (f"The tool {name} has not been registered yet.")
        else:
            return self.storage[name]["function"]
        
    def list_tools(self): 
        list_result = {}
        for n, v in self.storage.items():
            list_result[n] = v["description"]
        return list_result
    
    def execute(self, name, *args, **kwargs):
        tool = self.get(name)
        return tool(*args, **kwargs)
