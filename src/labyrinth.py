import queue

def read_input(input_file_path):
    with open(input_file_path, "r") as file:
        start_point = tuple(map(int, file.readline().strip().split(", ")))
        end_point = tuple(map(int, file.readline().strip().split(", ")))
        rows, cols = map(int, file.readline().strip().split())
        grid = []
        for _ in range(rows):
            row = list(map(int, file.readline().strip().split()))
            grid.append(row)

    return start_point, end_point, rows, cols, grid

def is_valid_move(x, y, rows, cols, grid, visited):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1 and not visited[x][y]

def find_shortest_path(start_point, end_point, rows, cols, grid, output_file_path):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = queue.Queue()
    start_x, start_y = start_point
    q.put((start_x, start_y, 0))

    visited = [[False for _ in range(cols)] for _ in range(rows]
    visited[start_x][start_y] = True

    found_destination = False

    while not q.empty() and not found_destination:
        x, y, steps = q.get()
        if (x, y) == end_point:
            found_destination = True
            with open(output_file_path, "w") as output_file:
                output_file.write(str(steps))
            break

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, rows, cols, grid, visited):
                q.put((new_x, new_y, steps + 1))
                visited[new_x][new_y] = True

    if not found_destination:
        return -1

    return steps

if __name__ == "__main":
    input_file_path = "../test/input.txt"
    output_file_path = "../test/output.txt"

    start_point, end_point, rows, cols, grid = read_input(input_file_path)

    shortest_path = find_shortest_path(start_point, end_point, rows, cols, grid, output_file_path)
