# Problem description:
# Compare area of presents to tree

from pathlib import Path
import time
import math

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    answer = 0

    i = -1
    for line in input_file:
        i += 1

        # Skip first part
        if i < 30:
            continue

        parts = line.split(":")
        sizes = parts[0].split("x")
        counts = parts[1].strip().split(" ")

        max_count = math.floor(int(sizes[0]) / 3) * math.floor(int(sizes[1]) / 3)

        current_count = 0
        for count in counts:
            current_count += int(count)

        if current_count <= max_count:
            answer += 1

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
