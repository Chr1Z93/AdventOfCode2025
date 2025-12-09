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

#  input_path = script_dir / "input.txt"
input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    answer = 0

    # parse red tiles into list
    red_tiles = []
    for line in input_file:
        split = line.strip().split(",")
        red_tiles.append({"x": int(split[0]), "y": int(split[1])})

    # create list of green tiles
    green_tiles = []

    previous_red_tile = red_tiles[-1]
    for red_tile in red_tiles:
        x1, y1 = previous_red_tile["x"], previous_red_tile["y"]
        x2, y2 = red_tile["x"], red_tile["y"]

        # vertical movement
        if x1 == x2:
            y_start = min(y1, y2) + 1
            y_end = max(y1, y2)
            for y in range(y_start, y_end):
                green_tile = {"x": x1, "y": y}
                green_tiles.append(green_tile)

        # horizontal movement
        elif y1 == y2:
            x_start = min(x1, x2) + 1
            x_end = max(x1, x2)
            for x in range(x_start, x_end):
                green_tile = {"x": x, "y": y1}
                green_tiles.append(green_tile)
        else:
            print("Diagonal!")

        previous_red_tile = red_tile

    # plot green and red tiles
    plot_tiles(red_tiles, green_tiles)

    # look for largest rectangle
    tile_index = -1
    for a in red_tiles:
        tile_index += 1
        for b in red_tiles[tile_index:]:
            size = calculate_size(a, b)
            if size > answer:
                answer = size

    return answer


def plot_tiles(red_tiles, green_tiles):
    red_x = [tile["x"] for tile in red_tiles]
    red_y = [tile["y"] for tile in red_tiles]
    green_x = [tile["x"] for tile in green_tiles]
    green_y = [tile["y"] for tile in green_tiles]

    plt.figure(figsize=(8, 6))

    # Plot red tiles using square markers ('s') for a tile effect
    plt.scatter(red_x, red_y, color="red", marker="s", s=100, label="Red Tiles")

    # Plot green tiles
    plt.scatter(green_x, green_y, color="green", marker="s", s=100, label="Green Tiles")

    # Set labels and title
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Plot of Red and Green Tiles")

    # Ensure the plot has a grid and square aspect ratio for tiles
    all_x = red_x + green_x
    all_y = red_y + green_y
    x_min, x_max = min(all_x) - 1, max(all_x) + 1
    y_min, y_max = min(all_y) - 1, max(all_y) + 1
    plt.xticks(range(int(x_min), int(x_max) + 1))
    plt.yticks(range(int(y_min), int(y_max) + 1))
    plt.grid(True)

    # Set aspect ratio to 'equal' so the squares look like tiles
    plt.gca().set_aspect("equal", adjustable="box")

    plt.legend(loc='upper left')
    plt.savefig("tiles_plot.png")


def calculate_size(a, b):
    return (abs((a["x"] - b["x"])) + 1) * (abs((a["y"] - b["y"])) + 1)


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
