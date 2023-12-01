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


def get_calibration_value(current_line):
    calibration_list = []
    reversed_line = "".join(current_line[::-1])
    # Getting first number
    for char in current_line:
        if char.isdigit():
            calibration_list.append(char)
            break
    # Getting second number
    for char in reversed_line:
        if char.isdigit():
            calibration_list.append(char)
            break
    # Return result as int
    return int(calibration_list[0] + calibration_list[1])


def main():
    filename = "input.txt"
    puzzle_input = read_file(filename)
    sum_of_calibration_values = 0
    for current_line in puzzle_input:
        calibration_values = get_calibration_value(current_line)
        sum_of_calibration_values += calibration_values
    print(sum_of_calibration_values)


if __name__ == '__main__':
    main()
