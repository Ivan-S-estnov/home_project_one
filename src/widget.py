from src.masks import get_mask_account, get_mask_card_number

# Примеры входных данных для проверки функции:
account_and_card_numb = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """


def mask_account_card(user_info: str) -> str:
    """Функция для маскировки номера карты/счета"""
    if "Счет" in user_info:
        return get_mask_account(user_info)
    else:
        return get_mask_card_number(user_info)


print(mask_account_card(account_and_card_numb))


date_input = "2018-07-11T02:26:18.671407"


def get_date(date_input: str) -> str:
    """Функция, принимающая строку с датой и модифоцирующая её в формат "ДД.ММ.ГГГГ" """
    date = date_input.split("T")[0]
    date_format = f"{date[-2:]}.{date[5:7]}.{date[:4]}"

    return date_format


print(get_date(date_input))
