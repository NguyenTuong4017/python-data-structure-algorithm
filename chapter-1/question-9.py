# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
#     a restaurant_name and a cuisine_type. 
#     Make a method called describe_restaurant() that prints these two pieces of information, 
#     and a method called open_restaurant() that prints a message indicating that the restaurant is open.


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")
        

restaurant = Restaurant('Kotipizza', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()