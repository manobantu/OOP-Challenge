class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(10, self.hunger - 30)
        self.happiness = min(10, self.happiness + 1)
        print=(f"{self.name} is eating. Hunger: {self.hunger}, Happiness: {self.happiness}")


    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print=(f"{self.name} is sleeping. Energy: {self.energy}")
 

    def play(self):
        self.energy = max(0, self.energy -2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print=(f"{self.name} is playing. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def train(self, trick):
        if trick  not in self.tricks:
            self.tricks.apppend(trick)
            self.energy = max(0, self.energy - 1)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} has learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        if not self.tricks:
            print=(f"{self.name} doesn't know any tricks yet.")  
        else:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
            

    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: len({self.tricks})")
        if self.hunger < 3:
            print(f"{self.name} is very hungry!")
        if self.energy < 3:
            print(f"{self.name} is very tired!")
        if self.happiness < 3:
            print(f"{self.name} is very sad!")
