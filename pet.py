class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """
        Eats food, updating hunger and happiness levels.
        The hunger is decreased, and happiness is increased slightly."""
        self.hunger = max(10, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. Hunger: {self.hunger}, Happiness: {self.happiness}")


    def sleep(self):
        #Sleeping increases energy and happiness slightly.
        # The energy is capped at 10, and happiness is increased by 5.
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Energy: {self.energy}")
 

    def play(self):
        """
        Plays with the pet, updating its energy, happiness, and hunger levels.
        The energy decreases, happiness increases, and hunger increases slightly.
        """
        self.energy = max(0, self.energy -2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def train(self, trick):
        """
        Trains the pet to learn a new trick. If the trick is already known, a message is displayed.
        If the trick is new, it is added to the list of tricks, and the pet's energy and happiness are updated."""
        if trick  not in self.tricks:
            self.tricks.apppend(trick)
            self.energy = max(0, self.energy - 1)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} has learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        """
        Displays the tricks learned by the pet. If no tricks are learned, a message is displayed."""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")  
        else:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
            

    def get_status(self):
        """
        Displays the current status of the pet, including hunger, energy, happiness, and tricks learned.
        If any of the attributes are below a certain threshold, a warning message is displayed.
        """
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: len({self.tricks})")
        if self.hunger > 7:
            print(f"{self.name} is very hungry!")
        if self.energy < 3:
            print(f"{self.name} is very tired!")
        if self.happiness < 3:
            print(f"{self.name} is very sad!")
