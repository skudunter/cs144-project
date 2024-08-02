import stdio
import sys
from simulation import Simulation
from compass import Compass
from handin1api import *

errors = {"INVALID_INPUT": "ERROR: Invalid argument: ", "TOO_FEW_ARGUMENTS":
          "ERROR: Too few arguments", "TOO_MANY_ARGUMENTS": "ERROR: Too many arguments", "INVALID_CONFIGURATION": "ERROR: Invalid configuration line", "INVALID_OBJECT": "ERROR: Invalid object setup on line "}
simulation = Simulation()


def read_input_from_cmd():
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
        simulation.change_gui_mode(bool(sys.argv[1]))


def read_board_input():
    # get the board configuration and the board setup from input
    first_line = True
    while True:
        if not stdio.hasNextLine():
            break
        line = stdio.readLine().strip()
        if first_line:
            handle_configuration_line(line)
            first_line = False
        else:
            break
            handle_board_line(line)


def handle_configuration_line(line):
    # check if the configuration line is valid
    line = line.split()
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


def handle_board_line(line):
    pass


def main():
    # main game loop
    read_input_from_cmd()
    read_board_input()


if __name__ == '__main__':
    main()
