import json
import os

from unicodedata import category

from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    """Читаем данные из JSON-файла"""
    products_path = os.path.abspath(path)
    with open(products_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    prod = []
    for i in data:
        desc = []
        for j in i["products"]:
            desc.append(Product(**j))
        i["products"] = desc
        prod.append(Category(**i))
    return prod


if __name__ == '__main__':
    raw_data = read_json("../data/products.json")
    category_data = create_objects_from_json(raw_data)
    print(category_data[0].name)
    print(category_data[0].description)
    print(category_data[0].products)