




class Chat(object):
    def __init__(self) -> None:
        self.content = []

    def update_chat(self, msg):
        self.content.append(msg)

    def get_chat(self):
        return self.content
    
    def __len__(self):
        return len(self.content)
    
    def __str__(self) -> str:
        return "".join(self.content)
    
    def __repr__(self) -> str:
        return str(self)
        
