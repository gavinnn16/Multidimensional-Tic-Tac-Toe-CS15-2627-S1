grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]



def display_grid(grid):
    for row in grid:
        print(row)


def determine_winner(grid):
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != " ":
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " ":
        return grid[0][2]
    for row in grid:
        if " " in row:
            return None
    return "Tie"
print("Winner:", determine_winner(grid_1))
display_grid(grid_1)
print("Winner:", determine_winner(grid_2))
display_grid(grid_2)
print("Winner:", determine_winner(grid_3))
display_grid(grid_3)
print("Winner:", determine_winner(grid_4))
display_grid(grid_4)