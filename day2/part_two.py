from functools import reduce

def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]
            return lines

    except FileNotFoundError:
        print(f"File not found at {filename}")
        return None

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None


def calculate_cubes_multiplied(game_input):
    # Get game sets
    game_sets = game_input.split(": ")[1].split(";")
    game_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for game in game_sets:
        # Get cubes of a game_set
        cubes = game.split(',')
        for cube in cubes:
            # Remove trailing space
            cube = cube.strip()
            # Compare values of minimal cubes required
            if game_cubes[cube.split(" ")[1]] < int(cube.split(" ")[0]):
                game_cubes[cube.split(" ")[1]] = int(cube.split(" ")[0])
    # Create anonymous function to multiply items of the game_cubes.values() list
    result = reduce(lambda x, y: x * y, game_cubes.values())
    return result


def main():
    # Change filename here of input
    filename = "input.txt"
    # Call the read_file to get the puzzle_input
    puzzle_input = read_file(filename)
    sum_of_cubes_multiplied = 0
    # Loop over puzzle input
    for game_input in puzzle_input:
        sum_of_cubes_multiplied += calculate_cubes_multiplied(game_input)
    # Print result of challenge
    print(sum_of_cubes_multiplied)


if __name__ == '__main__':
    main()
