import json
import sys

def load_json(file_path):
    """Загрузка данных из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def fill_values(test_structure, values):
    """Заполнение полей 'value' в структуре тестов."""
    for test in test_structure:
        # Найти соответствующее значение по ID
        for value in values:
            if test['id'] == value['id']:
                test['value'] = value['value']
                break

        # Если есть вложенные тесты, рекурсивно заполняются их значения
        if 'values' in test:
            fill_values(test['values'], values)

def main(values_file, tests_file, report_file):
    """Основная функция для формирования отчета."""
    # Загрузка данных из файлов
    values = load_json(values_file)['values']
    tests = load_json(tests_file)['tests']

    # Заполнение значений в структуре тестов
    fill_values(tests, values)

    # Запись результата в report.json
    with open(report_file, 'w', encoding='utf-8') as report:
        json.dump({'tests': tests}, report, ensure_ascii=False, indent=4)
        print("Результат успешно записан в report.json")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Запустите в командной строке: python task3.py <путь_к_values.json> <путь_к_tests.json> <путь_к_report.json>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])