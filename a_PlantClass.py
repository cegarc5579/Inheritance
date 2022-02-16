class Plant:
    # one attribute called color
    def __init__(self, color):
        self.__color = color

    # get method that returns color of the plant
    def get_color(self):
        return self.__color


# specialized version of a flower. flower inherits everything from Plant class
# put Plant in paranthesis to show that ur inheriting everything
# there is 2 attributes
# color is needed to initialize the superclass


class Flower(Plant):
    def __init__(self, color, petals):
        # create a plant first because it inherits from the superclass
        Plant.__init__(self, color)
        # petals only belongs to the subclass
        self.__petals = petals

    def get_petals(self):
        return self.__petals
