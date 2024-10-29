def test_one_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 3
    assert first_category.category_count == 1
    assert first_category.product_count == 3


def test_two_category_init(second_category):
    assert second_category.name == "Телевизоры"
    assert (
        second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(second_category.products) == 1
    assert second_category.category_count == 1
    assert second_category.product_count == 1


def test_three_category_init(third_category):
    assert third_category.name == "Товар закончился"
    assert third_category.description == "Нет в наличие"
    assert len(third_category.products) == 1
    assert third_category.category_count == 1
    assert third_category.product_count == 1

