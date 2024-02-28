from random import random
# from roles import business
from enum import Enum
from managers import business_manager as bm
# from managers import transaction_manager as tm


class Customer:
    budget: int = 500_00
    income: int = 150_00 # Adds income to budget at the start of each day
    business_preference = [] # weights for each business
    
    def __init__(self) -> None:
        self.money = Customer.budget

    def buy_item(self, product_name: str, amt: int, business_index: int, manager: bm.BusinessManager):
        business = manager.get_business(business_index)
        
        # money_owed = tm.TransactionManager(business, product_name, amt)
  
        if isinstance(money_owed, int):
            self.money -= money_owed
        
            
        

    # Weighted average to decide from who to buy
    # Weighted average to decide what type of item to buy
    # ^ Does this until it runs out of budget
    def bot_buy(self) -> None:
        pass