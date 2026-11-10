class Item :

    __items = []

    # A static  method that can access the private static variables
    @staticmethod
    def get_items() :
        return Item.__items

    # add name and age as parameters and set them as attributes
    def __init__(self, name, weight, price_history):
        Item.__items.append(self)
        self.name = name
        self.weight = weight
        self.price_history = price_history
        

    def __str__(self):
        return f'Item: {self.name} weights {self.weight}kg and has costed {self.price_history} over time'
