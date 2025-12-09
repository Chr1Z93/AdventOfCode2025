# Problem description:
# Map of red tiles (top left is 0, 0)
# Find largest rectangle

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    answer = 0

    red_tiles = []
    for line in input_file:
        split = line.strip().split(",")
        red_tiles.append([int(split[0]), int(split[1])])

    tile_index = -1
    for a in red_tiles:
        tile_index += 1
        for b in red_tiles[tile_index:]:
            size = calculate_size(a, b)
            if size > answer:
                answer = size

    return answer


def calculate_size(a, b):
    return (abs((a[0] - b[0])) + 1) * (abs((a[1] - b[1])) + 1)


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
