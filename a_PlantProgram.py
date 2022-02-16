import a_PlantClass as pc

# creating instances of the class
# primrose is a plant, and give it a color to create a instance
# this will just create a plant called primrose
primrose = pc.Plant("Green")

# creating this next one directly in subclass
sunflower = pc.Flower("Yellow", 12)
# for flower you need to give it two attributes because two attributes was set in class
# or else it gives error
print(primrose.get_color())

# can still do get_color because it inherits from it

print(sunflower.get_color())
# this method is in subclass so it can be called
print(sunflower.get_petals())

# get_petals is only in sub class and super class does not have access to this method
# print(primrose.get_petals())
