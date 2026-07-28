from tool_registry import ToolRegistry
from conversation_memory import ConversationMemory


class SimpleAgent:
    def __init__(self):
        self.registry = ToolRegistry()
        self.memory = ConversationMemory()

    def add_tool(self, name, func, description):
        self.registry.register(name, func, description)

    def run(self, user_message, tool_name, *args, **kwargs): 
        self.memory.add(role="user", content=user_message)
        result = self.registry.execute(tool_name, *args, **kwargs)
        self.memory.add(role="assistant", content=result)
        return result
    

def greet(name):
    return f"Hello, {name}!"

agent = SimpleAgent()
agent.add_tool("greet", greet, "Greets a person by name")
print(agent.run("say hi to camilo", "greet", "Camilo"))
print(agent.memory.get_history())
        

