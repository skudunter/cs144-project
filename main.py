import stdio
import sys
from simulation import Simulation
from bee import Bee, DesertBee, HoneyBee, Wasp
from beehive import BeeHive, DesertBeeHive, HoneyBeeHive, WaspHive
from flower import Flower, Pollen
from typing import Tuple, List


errors = {"INVALID_INPUT": "ERROR: Invalid argument: ", "TOO_FEW_ARGUMENTS":
          "ERROR: Too few arguments", "TOO_MANY_ARGUMENTS": "ERROR: Too many arguments",
          "INVALID_CONFIGURATION": "ERROR: Invalid configuration line", "INVALID_OBJECT": "ERROR: Invalid object setup on line ",
          "FLOWER_OCCUPIED": "ERROR: Cannot place flower at already occupied location",
          "HIVE_OCCUPIED": "ERROR: Cannot place hive at already occupied location", }
simulation = Simulation()


def read_cmd_arguments():
    # read input from command line and check if it is valid
    if (len(sys.argv) < 2):
        stdio.write(errors["TOO_FEW_ARGUMENTS"])
        sys.exit(1)
    elif (len(sys.argv) > 2):
        stdio.write(errors["TOO_MANY_ARGUMENTS"])
        sys.exit(1)
    elif (sys.argv[1] not in ["0", "1"]):
        stdio.write(errors["INVALID_INPUT"] + sys.argv[1])
        sys.exit(1)
    else:
        simulation.change_gui_mode(bool(int(sys.argv[1])))


def read_map_input():
    # get the board configuration and the board setup from input
    line_number = [-1]
    while True:
        if not stdio.hasNextLine():
            break
        line = stdio.readLine().strip().split()
        if line_number == [-1]:
            handle_configuration_line(line)
            line_number[0] += 1
        else:
            line_number[0] += 1
            handle_board_line(line, line_number)


def handle_configuration_line(line: List[str]):
    # check if the configuration line is valid
    if len(line) != 4:
        stdio.write(errors["INVALID_CONFIGURATION"])
        sys.exit(1)
    if not line[0].isdigit() or not line[1].isdigit():
        stdio.write(errors["INVALID_CONFIGURATION"])
        sys.exit(1)
    if int(line[0]) < 1 or int(line[0]) > 99:
        stdio.write(errors["INVALID_CONFIGURATION"])
        sys.exit(1)
    if line[2] not in ['f', 's']:
        stdio.write(errors["INVALID_CONFIGURATION"])
        sys.exit(1)
    if line[3] not in ['max', 'min', 'sum', 'sort']:
        stdio.write(errors["INVALID_CONFIGURATION"])
        sys.exit(1)
    if line[2] == 's' and line[3] != 'sort':
        stdio.write(errors["INVALID_CONFIGURATION"])
        sys.exit(1)

    simulation.change_size(int(line[0]))
    simulation.change_simulation_steps(int(line[1]))
    simulation.change_pollen_type(line[2])
    simulation.change_sorting_mode(line[3])


def handle_board_line(line: List[str], line_number: List[int]):
    # handle each line of the board setup
    try:
        if line[0] == 'F':
            col, row, num_pollen = get_position_and_entities(line)
            pollen_information = []
            validate_position(row, col, errors["FLOWER_OCCUPIED"])

            while num_pollen > 0:

                if not stdio.hasNextLine():
                    break
                line_number[0] += 1
                line = stdio.readLine().strip()

                if simulation.pollen_type == 'f':
                    try:
                        float(line)
                    except ValueError:
                        stdio.write(
                            errors["INVALID_OBJECT"] + str(line_number[0]))
                        sys.exit(1)
                    pollen_information.append(float(line))
                else:
                    pollen_information.append(line)
                num_pollen -= 1

            new_flower = Flower(row, col, simulation.pollen_type)

            for pollen_info in pollen_information:
                new_flower.add_pollen(Pollen(pollen_info))
            simulation.add_entity(row, col, new_flower)

        elif line[0] == 'H':
            col, row, num_entities = get_position_and_entities(line)

            validate_position(row, col, errors["HIVE_OCCUPIED"])

            line_number[0] += 1
            line = stdio.readLine().strip().split()
            speed = int(line[0])
            perception_range = int(line[1])
            new_hive = HoneyBeeHive(row, col, num_entities)

            for _ in range(num_entities):
                simulation.add_entity(row, col, HoneyBee(
                    row, col, speed, perception_range, new_hive))
            simulation.add_entity(row, col, new_hive)

        elif line[0] == 'B':
            col, row, num_entities = get_position_and_entities(line)

            validate_position(row, col, errors["HIVE_OCCUPIED"])

            line_number[0] += 1
            line = stdio.readLine().strip().split()
            speed = int(line[0])
            perception_range = int(line[1])
            new_hive = BeeHive(row, col, num_entities)

            for _ in range(num_entities):
                simulation.add_entity(row, col, Bee(
                    row, col, speed, perception_range, new_hive))

            simulation.add_entity(row, col, new_hive)
        elif line[0] == 'D':
            col, row, num_entities = get_position_and_entities(line)

            validate_position(row, col, errors["HIVE_OCCUPIED"])

            line_number[0] += 1
            line = stdio.readLine().strip().split()
            speed = int(line[0])
            perception_range = int(line[1])
            new_hive = DesertBeeHive(row, col, num_entities)

            for _ in range(num_entities):
                simulation.add_entity(row, col, DesertBee(
                    row, col, speed, perception_range, new_hive))
            simulation.add_entity(row, col, new_hive)

        elif line[0] == 'W':
            col, row, num_entities = get_position_and_entities(line)

            validate_position(row, col, errors["HIVE_OCCUPIED"])

            line_number[0] += 1
            line = stdio.readLine().strip().split()
            speed = int(line[0])
            new_hive = WaspHive(row, col, num_entities)

            for _ in range(num_entities):
                simulation.add_entity(row, col, Wasp(row, col, speed))
            simulation.add_entity(row, col, new_hive)

        else:
            stdio.write(errors["INVALID_OBJECT"] + str(line_number[0]))
            sys.exit(1)
    except (ValueError, IndexError, TypeError, EOFError):
        stdio.write(errors["INVALID_OBJECT"] + str(line_number[0]))
        sys.exit(1)


def get_position_and_entities(line) -> Tuple[int, int, int]:
    # return the position and number of entities from the input line
    col = int(line[1])
    row = int(line[2])
    num_entities = int(line[3])
    return col, row, num_entities


def validate_position(row, col, error_message):
    if not simulation.is_valid_position(row, col):
        stdio.write(error_message + f" ({str(col)},{str(row)})")
        sys.exit(1)


def do_main_game_loop():
    simulation.update()
    simulation.make_summary()


def main():
    read_cmd_arguments()
    read_map_input()
    do_main_game_loop()


if __name__ == '__main__':
    main()
