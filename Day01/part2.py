# Problem description:
# Safe opening via dial
# Count any time it passes 0

import math
from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
#input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    value = 50
    answer = 0

    for line in input_file:

        txt = line.strip()
        direction = txt[0]
        rotation = int(txt[1:])

        #print(f"{answer}: {value} + {txt}")
        #if answer > 50:
        #    break

        # Get number of full rotations
        full_rotations = int(round_down(rotation, -2) / 100)
        answer += full_rotations
        rotation = rotation % 100

        # Perform rotation
        if direction == "R":
            value += rotation
        else:
            # Handle double-counting going into negative from 0
            if value == 0:
                answer -= 1
            value -= rotation

        # Case handling
        if value < 0:
            value += 100

        elif value == 0:
            value += 0
        
        elif value == 100:
            value -= 100

        elif value > 100:
            value -= 100

        else:
            continue

        answer += 1


    return answer


def round_down(n, decimals=0):
    multiplier = 10**decimals
    return int(math.floor(n * multiplier) / multiplier)


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
