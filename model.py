import json

class model:
    def __init__(self, model_path):
        with open(model_path, mode = "rt", encoding = "utf-8") as f:
            self.m = json.load(f)

    def states(self):
        return self.m["START"].keys()

    def start(self, state):
        return self.m["START"][state]

    def emit(self, state, symbol):
        return self.m["EMISSION"][state][symbol]
    
    def transition(self, state1, state2):
        return self.m["TRANSITION"][state1][state2]
