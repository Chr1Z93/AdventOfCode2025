# Problem description:
# List of junction boxes
# Each line is one box (x, y, z)
# Connect 1.000 closest boxes
# Multiply sizes of three largest circuits

from pathlib import Path
import time
from functools import cache
from itertools import combinations

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

# input_path = script_dir / "input.txt"
input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    max_pairs = 10
    evaluate_count = 3

    # parse input into list of tuples
    boxes = []
    for line in input_file:
        strings = line.strip().split(",")
        boxes.append((int(strings[0]), int(strings[1]), int(strings[2])))

    # this holds the IDs for easier handling
    box_ids = list(range(0, len(boxes)))

    # generate list of all combinations and their distance
    connection_data = []
    for connection in combinations(box_ids, 2):
        box_1 = boxes[connection[0]]
        box_2 = boxes[connection[1]]
        connection_data.append([connection, get_distance(box_1, box_2)])

    # sort by distance
    connection_data.sort(key=lambda x: x[1])

    # remove unwanted connections
    del connection_data[max_pairs:]

    # generate a dictionary that holds all box -> circuit members data
    circuits = {}
    for data in connection_data:
        box_1 = boxes[data[0][0]]
        box_2 = boxes[data[0][1]]
        perform_connection(box_1, box_2, circuits)

    # get all the unique circuits from that
    unique_circuits = circuits.copy()
    must_stay = {}

    for member, circuit in circuits.items():
        must_stay[member] = True

        for submember in circuit:
            if (
                submember != member
                and submember in unique_circuits
                and submember not in must_stay
            ):
                del unique_circuits[submember]

    # calculate the circuit sizes
    sizes = []
    for circuit in unique_circuits.values():
        sizes.append(len(circuit))

    # sort descending
    sizes.sort(reverse=True)

    # multiply the size of the largest circuits
    answer = 1
    for i in range(0, evaluate_count):
        answer *= sizes[i]

    return answer


def perform_connection(start, end, circuits):
    if start not in circuits and end not in circuits:
        # both points not connected
        circuits[start] = {start, end}
        circuits[end] = {start, end}

    elif start in circuits and end in circuits:
        # both points already connected
        boxes = circuits[start] | circuits[end]
        for box in boxes:
            circuits[box] = boxes

    elif start in circuits:
        # start already connected
        circuits[start].add(end)
        circuits[end] = circuits[start]

    elif end in circuits:
        # end already connected
        circuits[end].add(start)
        circuits[start] = circuits[end]


@cache
def get_distance(a, b):
    d = 0
    for i in range(0, 3):
        d += get_squared_diff(a[i], b[i])
    return d**0.5


@cache
def get_squared_diff(x1, x2):
    return (x1 - x2) ** 2


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
