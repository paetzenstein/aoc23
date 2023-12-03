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


# Create dictionary of possible cubes within a game
possible_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def calculate_possible_games(game_input):
    # Retrieve game_id
    game_id = game_input.split(":")[0].split(" ")[1]
    # Get game sets from game_input
    game_sets = game_input.split(": ")[1].split(";")
    for game in game_sets:
        # temporary dictionary for cubes within a game
        game_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        # Split cubes in a list
        cubes = game.split(',')
        # Loop over the cubes
        for cube in cubes:
            # Remove trailing whitespace
            cube = cube.strip()
            # Add cube value to the temporary dictonary
            game_cubes[cube.split(" ")[1]] += int(cube.split(" ")[0])
        # Compare values to check if the game is possible
        if game_cubes.get("red") > possible_cubes.get("red") \
                or game_cubes.get("green") > possible_cubes.get("green") \
                or game_cubes.get("blue") > possible_cubes.get("blue"):
            return 0
    # Return result as Integer
    return int(game_id)


def main():
    # Change filename here of input
    filename = "input.txt"
    # Call the read_file to get the puzzle_input
    puzzle_input = read_file(filename)
    sum_of_possible_game_ids = 0
    # Loop over puzzle input
    for game_input in puzzle_input:
        sum_of_possible_game_ids += calculate_possible_games(game_input)
    # Print result of the challenge
    print(sum_of_possible_game_ids)


if __name__ == '__main__':
    main()
