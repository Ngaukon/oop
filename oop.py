#A Class with attribute

class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength
    
    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and my strength level is {self.strength}!")


#Create Objects

hero1 = Superhero("Iron Man", "Tech Genius", 85)
hero2 = Superhero("Hulk", "Super Strength", 100)

hero1.introduce()
hero2.introduce()

#Output
#I am Iron Man, my power is Tech Genius, and my strength level is 85!
#I am Hulk, my power is Super Strength, and my strength level is 100!

#Inheritance
class Villain(Superhero):
    def __init__(self, name, power, strength, evil_plan):
        super().__init__(name, power, strength)   # reuse parent init
        self.evil_plan = evil_plan
    
    def introduce(self):   # Polymorphism (method override)
        print(f"I am {self.name}, FEAR my {self.power}! My evil plan is {self.evil_plan} 😈")


#ASSIGNMENT TWO

#Define a Base Class
class Vehicle:
    def move(self):
        print("This vehicle moves in some way...")


#Create Sub-class
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on water!")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling along the path!")

#Polymorphism
# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Call move() for each one
for v in vehicles:
    v.move()

