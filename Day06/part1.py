# Problem description:
# cephalopods homework
# list of numbers to add / multiply

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
    results = []

    i = -1
    for line in input_file:
        i += 1

        parts = line.strip().split(" ")
        j = -1
        for part in parts:
            stripped = part.strip()
            if stripped == "":
                continue

            j += 1
            if part == "+":
                answer += results[j][0]

            elif part == "*":
                answer += results[j][1]
    
            else:
                num = int(stripped)
                if i == 0:
                    results.append([num, num])
                else:
                    results[j] = [results[j][0] + num, results[j][1] * num]

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
