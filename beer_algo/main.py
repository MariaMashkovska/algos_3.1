def min_beer_types(N, B, preferences):
    beer_info = [{'index': i, 'count': 0} for i in range(B)]

    for i in range(N):
        for j in range(B):
            if preferences[i][j] == 'Y':
                beer_info[j]['count'] += 1

    sorted_beer_info = sorted(beer_info, key=lambda x: x['count'], reverse=True)

    min_beer_types = 0
    total_likes = 0
    for beer in sorted_beer_info:
        total_likes += beer['count']
        min_beer_types += 1
        if total_likes >= N:
            break

    return min_beer_types


def read_input(filename):
    with open(filename, "r") as file:
        input_lines = file.readlines()
    N, B = map(int, input_lines[0].split())
    preferences = [line.strip() for line in input_lines[1].split()]
    return N, B, preferences


def write_output(filename, result):
    with open(filename, "w") as file:
        file.write(str(result) + '\n')


if __name__ == "__main__":
    input_filename = "../beer_algo/input.txt"
    N, B, preferences = read_input(input_filename)

    result = min_beer_types(N, B, preferences)

    output_filename = "output.txt"
    write_output(output_filename, result)
