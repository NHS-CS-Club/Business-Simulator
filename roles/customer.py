from random import random
# from roles import business ??
from business import Product 
from enum import Enum
from business_manager import BusinessManager

class Customer:
    budget: int = 500_00
    income: int = 150_00 # Adds income to budget at the start of each day
    business_preference = [] # weights for each business
    
    def __init__(self) -> None:
        # for business in list(BusinessCategories):
        #     if business.value == preferred_business_index:
        #         self.business_preference = business
        self.money = Customer.budget

    def buy_item(self, product_name: str, amt: int, business_index: int, business_manager: BusinessManager) -> None:
        pass
    
    # Weighted average to decide from who to buy
    # Weighted average to decide what type of item to buy
    # ^ Does this until it runs out of budget
    def bot_buy(self) -> None:
        pass