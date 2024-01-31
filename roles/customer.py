from random import random
# from roles import business ??
from business import Product 
from enum import Enum

class BusinessIndex(Enum):
    Farmer = 1
    
class Customer:
    budget = 500
    income = 150 # Adds income to budget at the start of each day
    business_preference = [] # weights for each business
    
    def __init__(self) -> None:
        # for business in list(BusinessCategories):
        #     if business.value == preferred_business_index:
        #         self.business_preference = business
        self.money = Customer.budget

    def buy_item(self, product: Product, amt: int, business_index: int) -> None:

        pass
    
    # Weighted average to decide from who to buy
    # Weighted average to decide what type of item to buy
    # ^ Does this until it runs out of budget
    def bot_buy(self) -> None:
        pass