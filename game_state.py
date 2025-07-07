class GameState:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.is_running = False
            cls._instance.score = 0
            cls._instance.level = 1
        return cls._instance
    
    def start_game(self):
        pass
    
    def update(self):
        pass
    
    def end_game(self):
        pass