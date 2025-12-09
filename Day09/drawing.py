# Problem description:
# Map of red tiles (top left is 0, 0)
# Red tiles are connected by green tiles
# Area in the middle is also green

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

        previous_red_tile = red_tile

    plot_tiles(green_tiles)


def plot_tiles(green_tiles):
    green_x = [tile["x"] for tile in green_tiles]
    green_y = [tile["y"] for tile in green_tiles]

    plt.figure(figsize=(40, 40))
    plt.scatter(green_x, green_y, color="green", marker="s", s=100, label="Green Tiles")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Plot of Green Tiles")
    plt.locator_params(axis="x", nbins=10)
    plt.locator_params(axis="y", nbins=10)
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("tiles_plot.png")


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
