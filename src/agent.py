from tool_registry import ToolRegistry
from conversation_memory import ConversationMemory
from retrieval import search


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
    


if __name__ == "__main__":
    def greet(name):
        return f"Hello, {name}!"


    document = "Este texto habla sobre la vida diaria, la gratitud, y también menciona un zorro marrón que salta sobre un perro perezoso mientras el sol brilla. También explica que sirve para rellenar espacios vacíos en páginas web."
    def search_documents(query):
        return search(query, document, top_n=2)

    agent = SimpleAgent()
    agent.add_tool("greet", greet, "Greets a person by name")
    agent.add_tool("search_documents", search_documents, "Searches the knowledge base for relevant text")

    # testing greet
    print(agent.run("say hi to camilo", "greet", "Camilo"))

    # test the RAG tool - the agent calls retrieval
    result = agent.run("de que habla este texto?", "search_documents", "de que habla este texto")
    print("\nSearch result:")
    for chunk in result:
        print("-", chunk)


    print("\nHistory:")
    print(agent.memory.get_history())
                

