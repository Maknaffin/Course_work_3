from src.utils import final_information, sort_list_executed


def test_final_information(test_five_operations):
    assert final_information(test_five_operations) == ['07.12.2019 Перевод организации\nVisa Classic 2842 87** **** '
                                   '9012 -> Счет **1585\n48150.39 USD\n', '19.11.2019 Перевод '
                                   'организации\nMaestro 7810 84** **** 5568 -> Счет **2411\n'
                                   '30153.72 руб.\n', '13.11.2019 Перевод со счета на счет\nСчет '
                                   '**6114 -> Счет **7654\n62814.53 руб.\n', '30.10.2019 Перевод '
                                   'с карты на счет\nVisa Gold 7756 67** **** 2839 -> Счет **9438\n'
                                   '23036.03 руб.\n', '29.09.2019 Перевод со счета на счет\nСчет '
                                   '**4214 -> Счет **7230\n45849.53 USD\n', '15.01.2019 Перевод '
                                   'организации\nVisa Platinum 2241 65** **** 8487 -> Счет **4942\n'
                                   '90688.44 USD\n', '31.07.2018 Перевод организации\nMasterCard '
                                   '8532 49** **** 2395 -> Счет **2381\n34380.08 USD\n']

def test_sort_list_executed(test_operation_list):
    assert sort_list_executed(test_operation_list) == [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {
                "amount": "50870.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086"
        }
    ]