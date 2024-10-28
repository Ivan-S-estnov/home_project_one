class Product:
    """Создание класса Product"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

if __name__=="__main__":
    product = Product("Smartphone", "Phone", 5000.20, 4)
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)