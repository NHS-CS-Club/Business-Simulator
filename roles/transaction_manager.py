from roles.business import BusinessError

class TransactionManager:
    def __init__(self):
        pass
    
    def sell(self, business, customer, product_name, amt):
        prod = business.get_product(product_name)
        if prod is BusinessError.ProductDoesNotExist:
            return prod # propogates the error
        
        total_cost = prod.price * amt  # Total cost that customer will have to pay at inputted product   

        # Can change if we want to error and have some other handling effect
        if customer.money < total_cost:
            amt = customer.money // prod.price
            total_cost = prod.price * amt

        business.money += total_cost        
        customer.money -= prod.price * amt
        
        return amt