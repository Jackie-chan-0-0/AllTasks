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
    # Получение входных данных от пользователя
    input_user_n = int(input("Введите значение n: "))
    input_user_m = int(input("Введите значение m: "))

    # Создание экземпляра класса
    path_calculator = PathCalculator(input_user_n, input_user_m)

    # Вычисление и вывод пути
    path_calculator.calculate_path()
    path_calculator.display_path()


if __name__ == "__main__":
    main()