import sys

class PathCalculator:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.path = []

    def calculate_path(self):
        """Вычисляет путь по кругу."""
        current_position = 1
        while True:
            self.path.append(current_position)
            current_position = 1 + (current_position + self.m - 2) % self.n
            if current_position == 1:
                break

    def display_path(self):
        """Выводит полученный путь."""
        print("Полученный путь:", ''.join(map(str, self.path)))

def main():
    # Проверка аргументов командной строки
    if len(sys.argv) != 3:
        print("Запустите в командной строке: python task1.py <n> <m>")
        sys.exit(1)

    try:
        input_user_n = int(sys.argv[1])
        input_user_m = int(sys.argv[2])
    except ValueError:
        print("Пожалуйста, введите целые числа для n и m.")
        sys.exit(1)

    # Создание экземпляра класса
    path_calculator = PathCalculator(input_user_n, input_user_m)

    # Вычисление и вывод пути
    path_calculator.calculate_path()
    path_calculator.display_path()

if __name__ == "__main__":
    main()