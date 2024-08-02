import sys

def min_moves(nums):
    target = sum(nums) // len(nums)
    moves = 0
    for num in nums:
        moves += abs(num - target)
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Запустите в командной строке: python task4.py <путь_к_файлу>")
    else:
        with open(sys.argv[1], 'r') as file:
            nums = [int(line.strip()) for line in file]
        print(min_moves(nums))