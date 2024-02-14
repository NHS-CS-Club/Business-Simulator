from roles import customer, business, business_manager;

def main():
    businesses = business_manager.BusinessManager()
    businesses.create_business(business.BusinessCategories.FARMER,"TestBiz");

if __name__ == "main":
    main()