# Problem description:
# Map with "." and "^"
# Starting point -> Beams emitted
# Count number of different paths

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    beams = {}
    answer = 1
    row = -1
    for line in input_file:
        row += 1
        if row % 2 == 1:
            continue
    
        if row == 0:
            beams[line.find("S")] = 1
            continue

        for col in list(beams):
            if line[col] == "^":
                incoming_beams = beams[col]
                answer += incoming_beams
                del beams[col]

                add_beam(beams, col - 1, incoming_beams)
                add_beam(beams, col + 1, incoming_beams)

    return answer

def add_beam(beams, id, times):
    if id not in beams:
        beams[id] = times
    else:
        beams[id] += times

# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
