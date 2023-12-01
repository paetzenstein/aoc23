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


def create_output_file(filename, output):
    try:
        with open(filename, 'w') as file:
            for lines in output:
                file.write(lines)
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def main():
    pass


if __name__ == '__main__':
    main()
