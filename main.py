# from roles import customer, business, business_manager;
from managers import business_manager, transaction_manager
from roles import business, customer

def main():
    businesses = business_manager.BusinessManager()
    businesses.create_business(business.BusinessCategories.FARMER,"TestBiz")
    transactions = transaction_manager.TransactionManager()
    test = customer.Customer()
    test.buy_item("test", 12, 0, businesses)
    pass

if __name__ == "__main__":
    main()