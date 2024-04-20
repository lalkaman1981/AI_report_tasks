#Here I combined every good suggestion
# Chat GPT made

"""Cafeteria orders"""
RECIPE = {
        "espresso": {'espresso': 30},
        "latte": {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15},
        "macchiato": {'espresso': 60, 'foamed_milk': 15},
        "flat white": {'espresso': 60, 'steamed_milk': 120},
        "dopio": {'espresso': 60},
        "cappuccino": {'espresso': 60, 'steamed_milk': 60, 'foamed_milk': 60},
        "lungo": {'espresso': 90},
        "cortado": {'espresso': 60, 'steamed_milk': 60}
        }

class Track:
    '''Class to track orders'''

    __beans = 5000
    __milk = 20000
    safety = True

    ###
    t_beans = 0
    t_milk = 0
    t_revenue = 0
    ###

    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    orders = []

    def __init__(self, date) -> None:
        self.date = date

    @property
    def beans(self):
        '''gets protected beans'''
        return self.__beans

    @beans.setter
    def beans(self, res):
        self.__beans = res

    @property
    def milk(self):
        '''gets protected milk'''
        return self.__milk

    @milk.setter
    def milk(self, liters):
        self.__milk = max(liters, 0)


    def place_order(self, order:'Coffee'):
        '''Function to place an order'''
        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."
        elif not self.safety:
            return 'Unfortunately, now it is not safe to make coffee.'
        ###
        espresso = order.espresso
        milk = order.milk
        name = order.name
        ###
        try:
            price = self.MENU[name] * order.count
        except KeyError:
            return "Unfortunately, we don't have such kind of coffee in the menu."
        if self.beans >= espresso // 5 and self.milk >= milk:
            self.beans -= espresso // 5
            self.milk -= milk
        else:
            return "Unfortunately, we don't have enough ingredients."
        self.orders.append(order)
        order.price = price
        order.is_paid = True
        return 'Done!'

    def total_revenue(self):
        '''count a total of revenue'''
        ###
        return sum(order.price for order in self.orders)
        ###

    def total_milk(self):
        '''count a total of milk, necessary for orders'''
        ###
        return sum(order.milk for order in self.orders)
        ###

    def total_beans(self):
        '''count a total of beans, necessary for orders'''
        ###
        return sum(order.espresso // 5 for order in self.orders)
        ###

    def milk_spoil(self, grams):
        '''filters the spoiled milk
        >>> day_track = Track('24.01.2024')
        >>> Track.set_limit_milk(21000)
        >>> day_track.milk_spoil(1000)
        >>> day_track.milk
        20000
        '''
        ###
        self.milk -= grams if grams <= self.milk else 0
        ###

    @classmethod
    def change_air_state(cls):
        '''Air alarm on/of'''
        if cls.safety:
            cls.safety = False
        else:
            cls.safety = True

    @classmethod
    def set_limit_milk(cls, liters):
        '''set the new max amount of milk avaliable'''
        cls.__milk = liters


class Coffee:
    '''Class to describe a regular coffee'''
    __recipe = {}
    is_paid = False

    def __init__(self, name, count=1) -> None:
        self.name = name
        self.count = count
        if self.name in self.__recipe:
            self.is_paid = False

    @property
    def espresso(self):
        '''get the amount of espresso necessary to make an order'''
        ###
        recipe = self.__recipe.get(self.name, {})
        return recipe.get('espresso', 0) * self.count
        ###


    @property
    def milk(self):
        '''get the amount of milk necessary to make an order'''
        ###
        recipe = self.__recipe.get(self.name, {})
        return (recipe.get('steamed_milk', 0) + recipe.get('foamed_milk', 0)) * self.count
        ###

    def __str__(self) -> str:
        if self in Track.orders:
            return f'Preparing {self.count} {self.name}...'
        elif not self.__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        elif self.name not in self.__recipe:
            return  "Order cannot be created. We don't have recipe for it."
        return f'Order "{self.count} {self.name}" is created.'

    def __repr__(self) -> str:
        return f'{self.count} {self.name}'

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.count == __value.count

    @classmethod
    def set_recipe(cls, recipe):
        '''Set coffee recipes for a day'''
        cls.__recipe = recipe

class FlavorMixin:
    '''Mixin class to add flavours'''

    def add_flavor(self, sugar, cinamon, syrup=None):
        '''Adds flavour if the order is paid'''
        if self.is_paid:
            self.sugar = sugar*self.count
            self.cinammon = cinamon
            if syrup:
                self.syrup = syrup
            self.flavor = True
            return 'Done!'
        return 'Please, pay for it.'



class CustomCoffee(Coffee, FlavorMixin):
    '''Class to describe a custom made coffee'''
    def __init__(self, name, count=1) -> None:
        super().__init__(name, count)
        self.flavor = False

    def __str__(self) -> str:
        ###
        if self.flavor and self.is_paid:
            sugar_str = "1 sticker of sugar" if self.sugar == 1 else f"{self.sugar} stickers of sugar"
            if sugar_str:
                sugar_str += ', ' if self.cinammon or self.syrup else ''
            cinnamon_str = "cinammon" if self.cinammon else ""
            if cinnamon_str:
                cinnamon_str += ', ' if self.syrup else ' '
            syrup_str = f"{self.syrup} syrup" if self.syrup else ""
            return f'Your best {self.name} is ready! It has: {sugar_str}{cinnamon_str}{syrup_str}.'
        ###
        elif self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        elif not Coffee._Coffee__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        elif self.name not in Coffee._Coffee__recipe:
            return  "Order cannot be created. We don't have recipe for it."
        return f'Order "{self.count} custom {self.name}" is created.'

    def __repr__(self) -> str:
        return f'{self.count} custom {self.name}'

    def __eq__(self, __value: object) -> bool:
        if not self.flavor and not isinstance(__value, CustomCoffee):
            return super().__eq__(__value)
        elif self.flavor and not isinstance(__value, CustomCoffee):
            return False
        return all(map(
            lambda x: self.__dict__[x] == __value.__dict__[x]
            if x not in ['is_paid', '_Coffee__price'] else True, self.__dict__))


def test_CafeteriaClass():
    """
    Print Done if all tests passed
    """
    print("Testing Cafeteria class...")
    # We track the orders during the day
    day_track = Track('07.02.2024')
    day_track.date = '07.02.2024'
    # Our cafeteria has a lot of different beverages in the menu and
    # all of them are connected to coffee.
    # The cafeteria use classical RECIPE that provided as a
    # constant.
    order1 = Coffee('latte')
    assert str(order1) == 'Order cannot be created. Recipe has not been set.'
    # We need to set the recipe before creating the instances.
    assert order1.__dict__ == {'name': 'latte', 'count': 1}
    Coffee.set_recipe(RECIPE)
    # A client can order only some kind of coffee.
    order1 = Coffee('latte', 2)
    assert order1.name == 'latte'
    assert order1.count == 2
    # also when the client ask for some order the is_paid attribute is
    # created and it is False from the start.
    assert order1.is_paid is False
    # Coffee have three main ingredients that provide variety of the drinks:
    # espresso, steamed milk and foamed milk. But on the side of the client we
    # provide only name of the drink and total amount of espresso
    # and milk in ml.
    assert order1.espresso == 120
    assert order1.milk == 270
    assert Coffee._Coffee__recipe[order1.name] == {
    'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
    assert str(order1) == 'Order "2 latte" is created.'
    #now we are ready to place this order
    assert Track.MENU == {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    assert day_track.place_order(order1) == 'Done!'
    assert order1.price == 140
    assert order1.is_paid == True
    assert str(order1) == 'Preparing 2 latte...'
    assert len(day_track.orders) == 1

    # it is possible that we have a coffee in recipe but
    # don't have in a menu
    order2 = Coffee("macchiato")
    assert str(order2) == 'Order "1 macchiato" is created.'
    assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}
    assert day_track.place_order(order2) == "Unfortunately, \
we don't have such kind of coffee in the menu."
    assert len(day_track.orders) == 1

    order2 = Coffee("mocca")
    assert str(order2) == "Order cannot be created. We don't have recipe for it."

    assert order2.__dict__ == {'name': 'mocca', 'count': 1}
    # Each customer can ask for adding sugar, cinammon or syrup
    # thus creating custom coffee.
    order2 = CustomCoffee('cappuccino')
    assert isinstance(order2, CustomCoffee)
    assert isinstance(order2, Coffee)
    assert isinstance(order2, FlavorMixin)
    assert not isinstance(order1, CustomCoffee)
    assert not isinstance(order1, FlavorMixin)

    assert order2.name == 'cappuccino'
    assert order2.count == 1
    assert order2.espresso == 60
    assert order2.milk == 120
    assert order2.flavor == False

    assert day_track.place_order(order2) == 'Done!'
    assert len(day_track.orders) == 2
    assert str(order2) == 'Preparing 1 cappuccino...'
    assert order2.price == 60

    assert order2.add_flavor(2, True, 'almond') == 'Done!'
    assert order2.sugar == 2 #number of stickers
    assert order2.cinammon == True #just to add some
    assert order2.syrup == 'almond' #type of syrup
    assert str(order2) == 'Your best cappuccino is ready! \
It has: 2 stickers of sugar, cinammon, almond syrup.'

    #of course we track the orders
    assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]'
    assert day_track.total_revenue() == 200
    assert day_track.total_milk() == 390
    #we need approx 6 grams of coffee beans to prepare
    # one espresso
    assert day_track.total_beans() == 36
    assert not isinstance(order2, Track)
    # of course we have some reserves of milk and beans
    # but they are limited. At the beginning of the day we usually
    #have 20 litres of milk and 5 kg of beans
    assert Track._Track__beans == 5000
    assert Track._Track__milk == 20000
    assert day_track.beans == 4964
    assert day_track.milk == 19610

    order3 = Coffee('Irish Coffee', 3)
    # unfortunately we don't have this kind of drinks
    # please let our customer know about it
    assert day_track.orders == [order1, order2]

    order3 = CustomCoffee('latte', 2)
    assert order3 == order1
    assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
    assert day_track.place_order(order3) == 'Done!'
    assert order3.add_flavor(3, False, 'green banana') == 'Done!'
    assert order3.sugar == 6
    print(str(order3))
    assert str(order3) == 'Your best latte is ready! \
It has: 6 stickers of sugar, green banana syrup.'
    assert order3 != order1
    print(order3.__dict__)

    # order7 =CustomCoffee('latte', 1)
    # print(day_track.place_order(order7))
    # order7.add_flavor(0, False, 'surop')
    # print(order7)

    # Sometimes we have situation when the milk spoiled
    # in grams
    day_track.milk_spoil(19340)
    assert day_track.milk == 0
    order4 = Coffee('latte', 2)
    assert day_track.place_order(order4) == "Unfortunately, we don't have enough ingredients."
    assert len(day_track.orders) == 3
    #oneday our founder bought new fridge
    # and we can store more milk
    Track.set_limit_milk(30000)
    assert Track._Track__milk == 30000


    order5 = "Coffee"
    assert not isinstance(order5, CustomCoffee)
    assert day_track.place_order(order5) == "We can't \
create anything that is not a Coffee instance."

    #and sure we don't work in air alert time
    Track.change_air_state()
    assert Track.safety == False
    order6 = CustomCoffee('lungo', 2)
    assert day_track.place_order(order6) == 'Unfortunately, now it is not safe to make coffee.'
    Track.change_air_state()
    assert Track.safety == True
    order6 = CustomCoffee('lungo')
    assert str(order6) == 'Order "1 custom lungo" is created.'
    assert day_track.place_order(order6) == 'Done!'
    assert day_track.total_revenue() ==  390
    assert day_track.total_milk() == 660
    assert day_track.total_beans() == 78



    print(str(CustomCoffee.__mro__))
    print('Done!')


if __name__ == '__main__':
    test_CafeteriaClass()

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
