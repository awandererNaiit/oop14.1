class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._products = []
        Category.total_categories += 1

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    def add_product(self, product):
        self._products.append(product)
        Category.total_unique_products += 1

    def remove_product(self, product):
        self._products.remove(product)
        Category.total_unique_products -= 1

    def get_products_info(self):
        products_info = []
        for product in self._products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.amount} шт."
            products_info.append(product_info)
        return products_info

    def __str__(self):
        total_products = len(self)
        return f"{self.name}, количество продуктов: {total_products} шт."

    def __len__(self):
        return sum(product.amount for product in self._products)


class Product:
    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.__price = price
        self.amount = amount

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: Цена должна быть больше нуля.")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.amount} шт."

    def __len__(self):
        return self.amount

    def add(self, quantity):
        self.amount += quantity
        print(f"Количество продукта '{self.name}' увеличено на {quantity}. Текущий остаток: {self.amount} шт.")

    def __add__(self, other):
        total_value = (self.price * self.amount) + (other.price * other.amount)
        return total_value

    @staticmethod
    def create_product(name, description, price, amount):
        return Product(name, description, price, amount)