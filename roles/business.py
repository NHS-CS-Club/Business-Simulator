from enum import Enum
from customer import Customer

class BusinessError(Enum):
    ProductDoesNotExist = "This business does not sell the product that you are looking for"

class Product:
    product_name: str
    price: int
    quantity: int

    def __init__(self, name: str, price: int, quantity: int):
        self.product_name = name
        self.price = price
        self.quantity = quantity


class BusinessCategories(Enum):
    FARMER = 0,

class BusinessOwner:
    intial_budget:int = 1000_00 # _ after 2 places bc money is in cents, not dollars
    products: list[Product] = []
    name = ''

    def __init__(self, category: BusinessCategories, name: str, products: list[Product]): # something
        self.money = BusinessOwner.intial_budget
        self.products = products
        self.category = category
        self.name = name
        # Add itself to the BusinessManager instance


    def get_product(self, product: str) -> Product|BusinessError:
        for prod in self.products:
            if prod.product_name == product:
                return prod
        
        return BusinessError.ProductDoesNotExist

    def add_product(self, name: str, price: int, init_quantity: int = 0):
        self.products.append(Product(name, price, init_quantity))

    # Assumes that product with `name`
    def set_price(self, name: str, new_price: int):
        prod = self.get_product(name)
    
        if prod is not BusinessError.ProductDoesNotExist:
            prod.price = new_price
    
    # Buys amount of products to restock
    # For now, it will just cost some constant amount of money
    def restock(self, product: Product, amt: int):
        if product.price * amt > self.money:
            amt = self.money // product.price

        # If budget to buy is more than or equal to product restock price, then buy as many as possiblels si tc
        self.products[self.products.index(product)].quantity += amt
        self.money -= product.price * amt
        

    # The business has a sell function which the customer calls
    # Returns amt of money the customer subtracted from their balance
    # Assumes that product with name `product_name` exists in `self.products
    def sell(self, customer: Customer, product_name: str, amt: int) -> int|BusinessError:
        prod = self.get_product(product_name)
        if prod is BusinessError.ProductDoesNotExist:
            return prod # propogates the error
        
        total_cost = prod.price * amt  # Total cost that customer will have to pay at inputted product   

        # Can change if we want to error and have some other handling effect
        if customer.money < total_cost:
            amt = customer.money // prod.price
            total_cost = prod.price * amt

        # Do some tax stuff
        self.money += total_cost
        
        customer.money -= prod.price * amt
        
        return amt
        




























































    """def update():
        
        income = 0
        income_tax_percentage = 0.0

        if(income <= 10275):
            income_tax_percentage = 0.10
        elif(income > 10275):
            income_tax_percentage = 0.12
        elif(income > 41775):
            income_tax_percentage = 0.22
        elif(income > 89075):
            income_tax_percentage = 0.24
        elif(income > 170050):
            income_tax_percentage = 0.32
        elif(income > 215950):
            income_tax_percentage = 0.35
        elif(income > 539900):
            income_tax_percentage = 0.37

        revenue = 0
        fixed_costs = 0
        variable_costs = 0
            
        total_costs = fixed_costs + variable_costs
        profits = (revenue - total_costs) * (1 + income_tax_percentage)
        money = profits + income"""