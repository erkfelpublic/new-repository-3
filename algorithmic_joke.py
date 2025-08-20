import random

def generate_maze(width=20, height=10):
    """
    Generates a maze using the recursive backtracking algorithm.
    """
    maze = [['#'] * width for _ in range(height)]
    start_x, start_y = (random.randint(0, width // 2 - 1) * 2, random.randint(0, height // 2 - 1) * 2)
    maze[start_y][start_x] = 'S'

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height

    def carve_passages_from(cx, cy):
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny) and maze[ny][nx] == '#':
                maze[cy + dy // 2][cx + dx // 2] = ' '
                maze[ny][nx] = ' '
                carve_passages_from(nx, ny)

    carve_passages_from(start_x, start_y)

    # Place the exit
    exit_x, exit_y = -1, -1
    while exit_x == -1 or maze[exit_y][exit_x] != ' ':
        exit_y = random.randint(0, height - 1)
        exit_x = random.randint(0, width - 1)
    maze[exit_y][exit_x] = 'E'

    return maze

def print_maze(maze):
    """
    Prints the maze to the console.
    """
    for row in maze:
        print("".join(row))

def tell_algorithmic_joke():
    """
    Generates and prints a maze, then tells a joke.
    """
    print("Why did the programmer get lost in the maze?")
    maze = generate_maze()
    print_maze(maze)
    print("\nBecause he was following a recursive algorithm and forgot the base case! (Find 'S' and get to 'E')")

if __name__ == "__main__":
    tell_algorithmic_joke()
