from sympy.logic.boolalg import And, Or, Not
from sympy.abc import P, Q, R, S  # Symbolic variables

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.agent_x, self.agent_y = 0, 0
        self.wumpus_x, self.wumpus_y = 2, 2
        self.gold_x, self.gold_y = 1, 1

    def check_percepts(self):
        percepts = []

        if (self.agent_x, self.agent_y) == (self.wumpus_x, self.wumpus_y):
            percepts.append("Stench")
        if (self.agent_x, self.agent_y) == (self.gold_x, self.gold_y):
            percepts.append("Glitter")

        return percepts

    def is_valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def move(self, direction):
        x, y = self.agent_x, self.agent_y
        if direction == "up" and self.is_valid(x - 1, y):
            self.agent_x = x - 1
        elif direction == "down" and self.is_valid(x + 1, y):
            self.agent_x = x + 1
        elif direction == "left" and self.is_valid(x, y - 1):
            self.agent_y = y - 1
        elif direction == "right" and self.is_valid(x, y + 1):
            self.agent_y = y + 1

    def has_wumpus(self):
        return (self.agent_x, self.agent_y) == (self.wumpus_x, self.wumpus_y)

    def has_gold(self):
        return (self.agent_x, self.agent_y) == (self.gold_x, self.gold_y)


# Example usage:
if __name__ == "__main__":
    size = 3
    game = WumpusWorld(size)
    print("Welcome to Wumpus World!")
    print("You are in a 3x3 grid world. Your mission is to find the gold and avoid the Wumpus!")
    print("You have the following percepts:")
    print(game.check_percepts())

    while True:
        action = input("Enter action (up/down/left/right/exit): ").lower()
        if action == "exit":
            break

        if action in ["up", "down", "left", "right"]:
            game.move(action)
            print("You moved to position: ({}, {})".format(game.agent_x, game.agent_y))
        else:
            print("Invalid action! Please try again.")

        percepts = game.check_percepts()
        print("Percepts: ", percepts)

        if game.has_wumpus():
            print("You got eaten by the Wumpus! Game over.")
            break
        elif game.has_gold():
            print("Congratulations! You found the gold and won the game.")
            break
