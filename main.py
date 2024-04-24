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
    def __init__(self, name, price, category):
        self._name = name
        self._price = price
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def category(self):
        return self._category

    @name.setter
    def name(self, value):
        self._name = value

    @price.setter
    def price(self, value):
        self._price = value

    @category.setter
    def category(self, value):
        self._category = value

    @staticmethod
    def check_type(obj1, obj2):
        if type(obj1) != type(obj2):
            raise TypeError("Нельзя добавлять разные продукты")

    def __add__(self, other):
        self.check_type(self, other)
        return self.price + other.price

    @property
    def total_price(self):
        return self.price


class Smartphone(Product):
    def __init__(self, name, price, category, brand, model, storage, color):
        super().__init__(name, price, category)
        self._brand = brand
        self._model = model
        self._storage = storage
        self._color = color


class LawnGrass(Product):
    def __init__(self, name, price, category, origin, duration, color):
        super().__init__(name, price, category)
        self._origin = origin
        self._duration = duration
        self._color = color
