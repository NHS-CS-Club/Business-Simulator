from enum import Enum

class Product:
    def __init__(self, price: float, salestax: float) -> Product:
        self.price = price
        self.salestax = salestax
    
    def finalPrice(self) -> float:
        return self.price * (1+self.tax)


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
    

class BusinessCategories(Enum):
    FARMER = 0

class Products(Enum):
    FARMER = {
        "APPLES" : Product(4, 6),
        "BANANAS" : Product(1.2, 6),
        "TOMATOES" : Product(1.5,6),
        "CUCUMBERS" : Product(3,6),
    }

class BusinessOwner:
    PRODUCTS = {}
    def __init__(self, category: BusinessCategories):
        match category:
            case 0:
                PRODUCTS = Products.FARMER
    def change_price(self, product, newPrice):
        PRODUCTS[product].price = newPrice

class FarmProducts:
    def __init__(self) -> None:
        self.products = {

        }
    
class Farmer(BusinessOwner):
    def __init__(self):
        super().__init__()
    
