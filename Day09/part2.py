# Problem description:
# Map of red tiles (top left is 0, 0)
# Red tiles are connected by green tiles
# Area in the middle is also green
# Only green tiles are eligible
# Find largest rectangle

from pathlib import Path
import time
import matplotlib.pyplot as plt

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    answer = 0

    # parse red tiles into list
    red_tiles = []
    for line in input_file:
        split = line.strip().split(",")
        red_tiles.append([int(split[0]), int(split[1])])

    # create list of green tile edges
    green_tile_edges = []

    previous = red_tiles[-1]
    for current in red_tiles:
        x1, y1 = previous[0], previous[1]
        x2, y2 = current[0], current[1]

        green_tile_edges.append(
            {
                "x_start": min(x1, x2),
                "x_end": max(x1, x2),
                "y_start": min(y1, y2),
                "y_end": max(y1, y2),
            }
        )

        previous = current

    # look for largest rectangle with green tiles
    tile_index = -1
    for a in red_tiles:
        tile_index += 1
        for b in red_tiles[tile_index:]:
            size = calculate_size(a, b)
            if size <= answer:
                continue

            if is_invalid(a, b, green_tile_edges):
                continue

            answer = size

    return answer


# make sure no edges intersect the rectangle
def is_invalid(a, b, green_tile_edges):
    x_min = min(a[0], b[0])
    x_max = max(a[0], b[0])
    y_min = min(a[1], b[1])
    y_max = max(a[1], b[1])

    for edge in green_tile_edges:
        if edge["x_start"] <= x_min and edge["x_end"] <= x_min:
            continue

        if edge["x_start"] >= x_max and edge["x_end"] >= x_max:
            continue

        if edge["y_start"] <= y_min and edge["y_end"] <= y_min:
            continue

        if edge["y_start"] >= y_max and edge["y_end"] >= y_max:
            continue

        return True

    return False


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
