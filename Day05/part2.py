# Problem description:
# Two lists: fresh and available ingredients
# Fresh are ranges (inclusive)
# Count available ingredients that are fresh

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

    fresh_ranges = []
    last_fresh = 0

    for line in input_file:
        # parse ranges into 2-element lists
        if "-" in line:
            range_split = line.strip().split("-")
            fresh_ranges.append([int(range_split[0]), int(range_split[1])])
            continue

        # sort the lists by first element
        if line == "\n":
            fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
            continue

        # check the available ingredients for freshness
        for fresh_range in fresh_ranges:
            a = fresh_range[0]
            b = fresh_range[1]

            # hardcoded case study :)
            if a > last_fresh:
                answer += b - a + 1
                last_fresh = b
                continue

            if a == last_fresh:
                answer += b - a
                last_fresh = b
                continue

            if b <= last_fresh:
                continue

            if b > last_fresh:
                answer += b - last_fresh
                last_fresh = b
                continue

        # we stop caring about the available ingredients, so break out of the loop
        break

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
