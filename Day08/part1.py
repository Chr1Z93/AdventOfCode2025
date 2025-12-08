# Problem description:
# List of junction boxes
# Each line is one box (x, y, z)
#
#

from pathlib import Path
import time
from functools import cache

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

# input_path = script_dir / "input.txt"
input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    answer = 0

    boxes = []
    for line in input_file:
        strings = line.strip().split(",")
        boxes.append((int(strings[0]), int(strings[1]), int(strings[2])))

    box_count = len(boxes)
    for box in boxes:
        closest_index = get_index_of_closest_box(box, boxes, box_count)
        print(closest_index)
        print(boxes[closest_index])
        return
    return answer


def get_index_of_closest_box(box, boxes, box_count):
    closest_index = -1
    closest_distance = 0
    for i in range(0, box_count):
        d = get_distance(box, boxes[i])
        if d != 0 and (closest_distance > d or closest_distance == 0):
            closest_index = i
            closest_distance = d
    return closest_index


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
