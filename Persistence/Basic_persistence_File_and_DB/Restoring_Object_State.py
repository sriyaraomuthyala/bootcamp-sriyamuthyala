import json
class Game:
    def __init__(self, level, score):
        self.level = level
        self.score = score

    def save_state(self):
        with open("game_state.json", "w") as file:
            json.dump(self.__dict__, file)

    def load_state(self):
        with open("game_state.json", "r") as file:
            data = json.load(file)
            self.__dict__.update(data)

game = Game(3, 1500)
game.save_state()

# Later, restore the state
new_game = Game(0, 0)
new_game.load_state()
print(new_game.level, new_game.score)
