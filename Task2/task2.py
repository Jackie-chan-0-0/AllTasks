from typing import List, Dict
import sys

def get_circle(file: str) -> Dict[str, float]:
    """Считывание параметров окружности из файла."""
    circle = {}

    try:
        with open(file, 'r') as circle_file:
            line = circle_file.readline().strip().split(" ")
            circle['x'] = float(line[0])
            circle['y'] = float(line[1])
            radius = float(circle_file.readline().strip())
            circle['r2'] = radius ** 2
    except IOError as ex:
        raise RuntimeError(f"Ошибка чтения файла circle: {ex}")
    except ValueError as ex:
        raise ValueError(f"Ошибка при разборе данных в файле circle: {ex}")

    return circle


def get_points(file: str) -> List[List[float]]:
    """Считывание списка точек из файла."""
    points = []

    try:
        with open(file, 'r') as points_file:
            for line in points_file:
                point = list(map(float, line.strip().split(" ")))
                points.append(point)
    except IOError as ex:
        raise RuntimeError(f"Ошибка при чтении файла с точками: {ex}")
    except ValueError as ex:
        raise ValueError(f"Ошибка при анализе данных точек: {ex}")

    return points


def create_positions(circle: Dict[str, float], points: List[List[float]]) -> List[int]:
    """Определяет положение каждой точки относительно окружности."""
    position_list = []

    for point in points:
        diff = (point[0] - circle['x']) ** 2 + (point[1] - circle['y']) ** 2 - circle['r2']

        if diff > 0:
            position_list.append(2)  # Точка снаружи окружности.
        elif diff == 0:
            position_list.append(0)  # Точка на окружности.
        else:
            position_list.append(1)  # Точка внутри окружности.

    return position_list


def main(circle_file: str, points_file: str) -> None:
    """Основная функция для выполнения программы."""
    circle = get_circle(circle_file)
    points = get_points(points_file)
    position_list = create_positions(circle, points)

    for position in position_list:
        print(position)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Запустите в командной строке: python task2.py circle.txt points.txt")
    else:
        main(sys.argv[1], sys.argv[2])