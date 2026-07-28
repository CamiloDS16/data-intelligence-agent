class ConversationMemory:
    def __init__(self):
        self.list_store = []

    def add(self, role, content):
        self.list_store.append({"role": role,
                                "content": content})
        
    def get_history(self): 
        return self.list_store

    def last_n(self, n):
        if n == 0:
            return []
        else:
            return self.list_store[-n:] 
