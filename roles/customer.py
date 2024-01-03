from random import random
from roles import business
from business import BusinessCategories

class Customer:
    budget = 150
    business_preference = None
    def __init__(self) -> None:
        preferred_business_index = int(random*len(BusinessCategories))
        for business in list(BusinessCategories):
            if business.value == preferred_business_index:
                self.business_preference = business
