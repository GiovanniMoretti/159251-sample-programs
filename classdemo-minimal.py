# A very simple demo of how to define classes in Python, 
# Giovanni - 2012

# Define the class
class car():
    def __init__(self, newColor):
        self.color = newColor
        
    def setColor(self, nowColor):       # Methods must include 'self' as a parameter
        self.color = nowColor

    def show(self):
        print "Object's color is " +self.color

# Create some instances
blueCar = car("blue")
redCar  = car("red")

blueCar.show()
redCar.show()

# Call a method
blueCar.setColor("Black")
blueCar.show()

# Add an attribute dynamically
blueCar.windows = False
print blueCar.windows

