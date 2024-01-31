from enum import Enum

class Product(Enum):
    APPLE = "APPLE", #????
    BANANA = "BANANA",
    TOMATO = "TOMATO",
    CUCUMBER = "CUCUMBER",

class BusinessCategories(Enum):
    FARMER = 0,

class BusinessOwner():
    intial_budget = 1000.00
    business_count = 0
    business_index = []
    name = ""

    def __init__(self, category: BusinessCategories, name: str): # something
        self.money = BusinessOwner.intial_budget
        self.products = set()
        self.category = category
        self.name = name
        BusinessOwner.business_index += [self]

    def add_product(self, product: Product, price: float, init_quantity: int = 0):
        self.products.add({
            'product': product,
            'price': price,
            'quantity': init_quantity
        })

    def set_price(self, product: Product, new_price: float):
        self.products.get('price') = new_price
    
    def set_quantity(self, product: Product, new_quantity: int):
        self.products.get(product)['quantity'] = new_quantity
    
    # Buys amount of products to restock
    # For now, it will just cost some constant amount of money
    def restock(self, product: Product, amt: int):
        PRICE = 5
        if PRICE * amt > self.money:
            amt = self.money // PRICE

        self.products.get(product)['quantity'] += amt
        self.money -= PRICE * amt

        
    
    def update():
        
        print("""
              
              






""")
        
        

        
        INCOME = 0
        INCOME_TAX_PERCENTAGE = 0.0

        if(INCOME <= 10275):
            INCOME_TAX_PERCENTAGE = 0.10
        elif(INCOME > 10275):
            INCOME_TAX_PERCENTAGE = 0.12
        elif(INCOME > 41775):
            INCOME_TAX_PERCENTAGE = 0.22
        elif(INCOME > 89075):
            INCOME_TAX_PERCENTAGE = 0.24
        elif(INCOME > 170050):
            INCOME_TAX_PERCENTAGE = 0.32
        elif(INCOME > 215950):
            INCOME_TAX_PERCENTAGE = 0.35
        elif(INCOME > 539900):
            INCOME_TAX_PERCENTAGE = 0.37

        REVENUE = 0
        FIXED_COSTS = 0
        VARIABLE_COSTS = 0
            
        TOTAL_COSTS = FIXED_COSTS + VARIABLE_COSTS
        PROFITS = (REVENUE - TOTAL_COSTS) * (1 + INCOME_TAX_PERCENTAGE)
        MONEY = PROFITS + INCOME


# class __OLD_Product__:
#     def __init__(self, price: float, sales_tax: float) -> Product:
#         self.price = price
#         self.sales_tax = sales_tax
    
#     def final_price(self) -> float:
#         return self.price * (1 + self.tax)



