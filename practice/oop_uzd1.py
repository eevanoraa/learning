class Product():
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    def get_total_price(self):
        total_price = self.__price * self.__quantity
        return total_price

    def get_product_name(self):
        return self.__name


class ShoppingCart():
    def __init__(self):
        self.items = []

    def add_product_to_cart(self, product):
        self.items.append(product)
        print("Produkts", product.get_product_name(), "pievienots grozam!")

    def remove_product_to_cart(self, product):
        self.items.remove(product)
        print("Produkts", product.get_product_name(), "nodzests no groza!")
    
    def get_total_price(self):
        total_price = 0
        for product in self.items:
            total_price += product.get_total_price()
        print("Kopeja summa:", total_price)


class SystemUser():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def set_user_info(self, new_username, new_password, new_email):
        self.username = new_username
        self.password = new_password
        self.email = new_email
        print("Informacija ir nomainita!")
    
    def get_user_info(self):
        print("--- Informacija par lietotaju ---")
        print("Lietotajvards:", self.username)
        print("Parole:", self.password)
        print("E-pasts:", self.email)


class Customer(SystemUser):
    def __init__(self, username, password, email, customer_id, purchase_history, membership_status):
        super().__init__(username, password, email)
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_status = membership_status
    def set_user_info(self, new_username, new_password, new_email, new_customer_id, new_purchase_history, new_membership_status):
        super().set_user_info(new_username, new_password, new_email)
        self.customer_id = new_customer_id
        self.purchase_history = new_purchase_history
        self.membership_status = new_membership_status
    def get_user_info(self):
        super().get_user_info()
        print("Klienta ID:", self.customer_id)
        print("Pirkumu vesture:", self.purchase_history)
        print("Piederiba programmai:", self.membership_status)


Maize = Product("Baltmaize", 1.50, 2)
print(Maize.get_total_price())
Desa = Product("Doktordesa", 3.50, 2)
print(Desa.get_total_price())

IepirkumuGrozs = ShoppingCart()
IepirkumuGrozs.add_product_to_cart(Maize)
IepirkumuGrozs.add_product_to_cart(Desa)
IepirkumuGrozs.get_total_price()
IepirkumuGrozs.remove_product_to_cart(Maize)
IepirkumuGrozs.get_total_price()

Vasya = SystemUser("Vasya1234", "ABC1234", "Vasya1234@gmail.com")
Vasya.set_user_info("Vasya1234", "99847362", "Vasya1234@gmail.com")
Vasya.get_user_info()

Anna = Customer("Anna1234", "DEF1234", "Anna1234@gmail.com",  13, "", "")
Anna.set_user_info("Anna1234", "DEF1234", "Anna1234@gmail.com",  13, "Vizbulites", "")
Anna.get_user_info()