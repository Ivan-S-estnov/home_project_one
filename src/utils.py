import json
import os

from unicodedata import category

from src.product import Product
from src.category import Category
from tests.conftest import product


def read_json(path: str) -> dict:
    """Читаем данные из JSON-файла"""
    products_path = os.path.abspath(path)
    with open(products_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def create_objects_from_json(data):
    categories = []
    for i in data:
        product = []
        for j in category['products']:



if __name__ == '__main__':
    raw_data = read_json("../data/products.json")
    category_data = create_objects_from_json(raw_data)
    print(category_data)