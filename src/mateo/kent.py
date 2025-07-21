numbers = [None for _ in range(5)]
print(numbers)

CASHE_SIZE = 16
_cache = [None for _ in range(CASHE_SIZE)]
print(_cache)

rows, cols = 5, 5
grid = [['x' for _ in range(cols)] for _ in range(rows)]
print(grid)

for row in range(rows):
    temp_row = []
    for col in range(cols):
        temp_row.append('o' if col > row else 'x')
    grid.append(temp_row)
print(grid)


# dictionary comprehension

