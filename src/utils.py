# Импортируем json и datetime
import json
from datetime import datetime


def load_list_operations(filename):
    """
    Загрузка данных из файла json
    """
    with open(filename, 'rt', encoding="utf8") as f:
        list_operations = json.loads(f.read())
    return list_operations


def list_operation(all_list_operations):
    """
    Убирает пустые элементы списка
    """
    new_data = [value for value in all_list_operations if value.get("from")]
    return new_data


def sort_list_executed(operation_list):
    """
    Сортирует список по выполненным операциям
    """
    list_executed = [value for value in operation_list if value["state"] == "EXECUTED"]
    return list_executed


def sort_list_date(list_executed):
    """
    Сортирует список операций по дате
    """
    sorted_list = sorted(list_executed, key=lambda x:x.get('date'), reverse = True)
    return sorted_list


def last_five_operations(list_date):
    """
    Делает срез первых 5 операций
    """
    list_five_operations = list_date[:5]
    return list_five_operations


def final_information(five_operations):
    """
    Вывод последних 5 операций в формате указанном в ТЗ
    """

    # Добавление итоговой информации в список
    final_information_list = []

    # Перебор циклом 5 последних операций для вывода в нужном формате
    for data in five_operations:

        # Изменение формата вывода даты
        format_date = data["date"]
        d = datetime.strptime(format_date, '%Y-%m-%dT%H:%M:%S.%f')
        new_format_date = d.strftime("%d.%m.%Y")

        # Подсчёт количества чисел в строке
        words = data["from"].split()
        numbers = [word for word in words if word.isdigit()]
        sum_numbers = len(numbers[0])

        # Добавление * в номера карт и счётов отправителя
        if sum_numbers == 16:
            if data["from"][0:10] == 'MasterCard':
                from_score = data["from"][11:]
                new_from_score = data["from"][0:10] + ' ' + from_score[0:4] + ' ' + from_score[4:6]\
                                 + '**' + ' ' + '****' + ' ' + from_score[12:16]
            elif data["from"][0:9] == 'Visa Gold':
                from_score = data["from"][10:]
                new_from_score = data["from"][0:9] + ' ' + from_score[0:4] + ' ' + from_score[4:6]\
                                 + '**' + ' ' + '****' + ' ' + from_score[12:16]
            elif data["from"][0:12] == 'Visa Classic':
                from_score = data["from"][13:]
                new_from_score = data["from"][0:12] + ' ' + from_score[0:4] + ' ' + from_score[4:6]\
                                 + '**' + ' ' + '****' + ' ' + from_score[12:16]
            elif data["from"][0:13] == 'Visa Platinum':
                from_score = data["from"][14:]
                new_from_score = data["from"][0:13] + ' ' + from_score[0:4] + ' ' + from_score[4:6]\
                                 + '**' + ' ' + '****' + ' ' + from_score[12:16]
            else:
                from_score = data["from"][8:]
                new_from_score = data["from"][0:7] + ' ' + from_score[0:4] + ' ' + from_score[4:6]\
                                 + '**' + ' ' + '****' + ' ' + from_score[12:16]
        else:
            from_score = data["from"][5:]
            new_from_score = data["from"][0:4] + ' ' + '**' + from_score[2:6]

        # Добавление * в номера карт и счётов получателя
        to_score = data["to"][5:]
        new_to_score = data["to"][0:4] + ' ' + '**' + to_score[2:6]

        # Добавление в список выводы нужных форматов
        final_information_list.append(f'{new_format_date} {data["description"]}\n{new_from_score}'
                                      f' -> {new_to_score}\n{data["operationAmount"]["amount"]}'
                                      f' {data["operationAmount"]["currency"]["name"]}\n')

    return final_information_list