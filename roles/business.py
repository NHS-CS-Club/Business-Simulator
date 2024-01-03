from enum import Enum

class Product(Enum):
    APPLE = "APPLES", #????
    BANANA = "BANANA",
    TOMATO = "TOMATO",
    CUCUMBER = "CUCUMBER",

class __OLD_Product__:
    def __init__(self, price: float, sales_tax: float) -> Product:
        self.price = price
        self.sales_tax = sales_tax
    
    def final_price(self) -> float:
        return self.price * (1 + self.tax)


    
# Economy state???
# Theo you should clean this up and make it work properly
"""
class MoneyOperations():
    INCOME = 0
    REVENUE = 0
    FIXED_COSTS = 0
    VARIABLE_COSTS = 0
    TOTAL_COSTS = FIXED_COSTS + VARIABLE_COSTS
    PROFIT_TAX = PROFITS * INCOME_TAX
    PROFITS = REVENUE - TOTAL_COSTS - PROFIT_TAX
    MONEY = PROFITS + INCOME
    if(INCOME <= 10275):
        INCOME_TAX = 0.10
    elif(INCOME > 10275):
        INCOME_TAX = 0.12
    elif(INCOME > 41775):
        INCOME_TAX = 0.22
    elif(INCOME > 89075):
        INCOME_TAX = 0.24
    elif(INCOME > 170050):
        INCOME_TAX = 0.32
    elif(INCOME > 215950):
        INCOME_TAX = 0.35
    elif(INCOME > 539900):
        INCOME_TAX = 0.37
"""

class BusinessCategories(Enum):
    FARMER = 0

class Producer(Enum):
    FARMER = {
        "APPLES" : Product(4, 6),
        "BANANAS" : Product(1.2, 6),
        "TOMATOES" : Product(1.5,6),
        "CUCUMBERS" : Product(3,6),
    }

class BusinessOwner:
    INITIAL_BUDGET = 1000.00

    def __init__(self, category: BusinessCategories):
        self.money = BusinessOwner.INITIAL_BUDGET
        self.products = { }
        # match category:
        #     case 0:
        #         self.products[] Producer.FARMER

    def change_price(self, product: Product, new_price: float):
        self.products[product].price = new_price
    
class Farmer(BusinessOwner):
    def __init__(self):
        super().__init__()


    
