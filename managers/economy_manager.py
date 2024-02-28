from managers import business_manager as bm, transaction_manager as tm
from roles import customer, business

class EconomyManager:
    customers: list[customer.Customer]

    def __init__(self):
        # Managers
        self.bm = bm.BusinessManager()
        self.tm = tm.TransactionManager()

        # Entities
        self.customers = [] # ???
        self.businesses = [] # ???

    def create_customer(self) -> customer.Customer:
        new_customer = customer.Customer()
        
        self.customers.append(new_customer)

        return self.customers[len(self.customers) - 1]
    
    def make_purchase(self):
        pass