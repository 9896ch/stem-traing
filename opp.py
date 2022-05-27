# oop
# defining a class and its attributes .
# creating instances (objects) of a class .
# class methods (functions belonging to a class).
# inheritance & polymorphism.
# methods overriding.

class Dog:
    def __init__(self,no_of_eyes,color,no_of_legs,no_of_ears):
        self.no_of_eyes = no_of_eyes
        self.color = color
        self.no_of_legs = no_of_legs
        self.no_of_ears = no_of_ears 
    def barking(self):
        print("woof woof!")
    def walking(self):
        print("slowly")
    def eating(self):
        print("greedy")        
german_shepherd = Dog(no_of_eyes=2,color="Grey",no_of_legs=4,no_of_ears=2)
dodger = Dog(no_of_eyes=1,color="Brown",no_of_legs=3,no_of_ears=2)
print(german_shepherd.no_of_eyes) 
print(dodger.color,dodger.no_of_eyes) 
dodger.color = "dark-brown"
print(dodger.color) 
print(dodger.color,dodger.no_of_eyes,dodger.no_of_legs,dodger.no_of_ears)
dodger.barking()
dodger.walking()
dodger.eating()



