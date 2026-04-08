from abc import ABC, abstractmethod

class Govt(ABC):

    def __init__(self, user_name, user_age):
        self.user_name = user_name
        self.user_age = user_age

    @abstractmethod
    def get_license(self):
        return "Applied for the license"
    
class pizzaShop(Govt):

    def __init__(self, owner_name, owner_age):
        Govt.__init__(self, owner_name, owner_age)

    def get_license(self):
        return "Got the license"

pizzaIns = pizzaShop("Rohan", 35)
print(pizzaIns.get_license())