def read_file(filename):
    try:
        with open(filename, 'r') as file:
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
    calibration_numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    reversed_calibration_numbers = ("eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin")
    # Getting first number
    for char in current_line:
        counter = 1
        if char.isdigit():
            calibration_list.append(char)
            break
        if current_line.startswith(calibration_numbers):
            for num in calibration_numbers:
                if current_line.startswith(num):
                    calibration_list.append(str(calibration_numbers.index(num) + 1))
                    break
            break
        else:
            current_line = current_line[counter:]
            counter += 1
    # Getting second number
    for char in reversed_line:
        counter = 1
        if char.isdigit():
            calibration_list.append(char)
            break
        if reversed_line.startswith(reversed_calibration_numbers):
            for num in reversed_calibration_numbers:
                if reversed_line.startswith(num):
                    calibration_list.append(str(reversed_calibration_numbers.index(num) + 1))
                    break
            break
        else:
            reversed_line = reversed_line[counter:]
            counter += 1
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
