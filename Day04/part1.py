# Problem description:
# Rolls of paper (@)
# Which rolls can be accessed?

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

    x_off = [-1, -1, -1, 0, 0, 1, 1, 1]
    y_off = [-1, 0, 1, -1, 1, -1, 0, 1]

    # parse input
    map = []  # x-y map, top left is 0/0 (x is downwards!)

    x = -1
    for line in input_file:
        x += 1
        map.append(list(line.strip()))

    x = -1
    for line in map:
        x += 1
        y = -1

        for char in line:
            y += 1

            # not a roll
            if char != "@":
                continue

            # count nearby rolls
            nearby_rolls = 0
            for i in range(0, 8):
                if is_roll(map, x + x_off[i], y + y_off[i]):
                    nearby_rolls += 1
        
                if nearby_rolls == 4:
                    break

            if nearby_rolls == 4:
                continue

            answer += 1

    return answer


def is_roll(map, x, y):
    if x >= len(map) or x < 0:
        return False
    elif y >= len(map[x]) or y < 0:
        return False
    else:
        return map[x][y] == "@"


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
