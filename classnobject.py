class Robot:
    def introduce_self(self):
        print(f"Hello, my name is {self.name}.")

        r1 = Robot()
        r1.name = "Robo"
        r1.color = "Red"
        r1.weight = 50
        print(r1.introduce_self)