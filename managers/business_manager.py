from roles import business
from managers import transaction_manager

class BusinessManager:
    businesses = []
    
    def __init__(self) -> None:
        self.businesses = []
    
    def create_business(self, category: business.BusinessCategories, name: str) -> None:
        new_business = business.BusinessOwner(category, name, [])
    
    def get_business(self, business_index: int) -> business.BusinessOwner:
        return self.businesses[business_index]