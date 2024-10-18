import random

def generate_grid(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    num_pre_filled = random.randint(size, size * 2)

    for _ in range(num_pre_filled):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        while grid[row][col] != 0:
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[row][col] = generate_valid_number(grid, row, col, size)

    return grid

def generate_valid_number(grid, row, col, size):
    valid_numbers = list(range(1, size + 1))
    random.shuffle(valid_numbers)

    for num in valid_numbers:
        if is_valid_placement(grid, row, col, num, size):
            return num
    return 0

def is_valid_placement(grid, row, col, num, size):
    # check the row
    if num in grid[row]:
        return False

    # check the column
    for r in range(size):
        if grid[r][col] == num:
            return False

    # check the sub-grid (square)
    sub_grid_size = int(size ** 0.5)
    start_row, start_col = row // sub_grid_size * sub_grid_size, col // sub_grid_size * sub_grid_size

    for r in range(start_row, start_row + sub_grid_size):
        for c in range(start_col, start_col + sub_grid_size):
            if grid[r][c] == num:
                return False

    return True

def print_grid(grid, size):
    sub_grid_size = int(size ** 0.5)
    for row in range(size):
        if row % sub_grid_size == 0 and row != 0:
            print('-' * (size * 3))
        for col in range(size):
            if col % sub_grid_size == 0 and col != 0:
                print('| ', end='')
            print(f'{grid[row][col]} ', end='')
        print()

def get_user_input(grid, size):
    while True:
        print_grid(grid, size)
        print("\nenter 'q' to quit")

        try:
            userinput = input("enter row, column, and number (like:  2 3 4): ").strip()
            if userinput.lower() == 'q':
                break

            row, col, num = map(int, userinput.split())
            row, col = row - 1, col - 1

            if row < 0 or col < 0 or num <= 0 or num > size:
                print("invalid input try again")
                continue

            if grid[row][col] != 0:
                print("cannot modify pre-filled block try again")
                continue

            if is_valid_placement(grid, row, col, num, size):
                grid[row][col] = num
            else:
                print("invalid placing try again")
        except ValueError:
            print("invalid input try again")

    print("thanks for playing!")


size = 3
sudoku_grid = generate_grid(size)
get_user_input(sudoku_grid, size)

