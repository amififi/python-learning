
import random
class Rock_scissors_paper:
    def __init__(self):
        self.choices = ["rock", "scissors", "paper"]
        self.urpoint = 0
        self.cpoint = 0

    def play(self):

        while self.urpoint < 3 and self.cpoint < 3:
            self.user = input("rock, scissors or paper?: " )

            if self.user not in self.choices:
                raise Exception("Sorry, your answer should be from the expected values")
            self.cc = random.choice(self.choices)
            print(f"computer choice: {self.cc}")

            if self.choices.index(self.user) == 2 and self.choices.index(self.cc) == 0:
                print("W")
                self.urpoint += 1
                print(f"computer point: {self.cpoint}")
                print(f"your point: {self.urpoint}")

            elif self.choices.index(self.user) > self.choices.index(self.cc):
                    print("L")
                    self.cpoint += 1
                    print(f"computer point: {self.cpoint}")
                    print(f"your point: {self.urpoint}")
            elif self.choices.index(self.user) < self.choices.index(self.cc):
                    print("W")
                    self.urpoint += 1
                    print(f"computer point: {self.cpoint}")
                    print(f"your point: {self.urpoint}")
            elif self.choices.index(self.user) == self.choices.index(self.cc):
                    print("T")
                    print(f"computer point: {self.cpoint}")
                    print(f"your point: {self.urpoint}")
        


p = Rock_scissors_paper()
p.play()

        




















