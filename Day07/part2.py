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
    data = []
    start = None
    for line in input_file:
        if not start:
            start = line.find("S")
        data.append(list(line.strip()))

    if start == None:
        print("Start not found!")
        return

    # this set holds the indices of the beams
    beams = {}
    beams[start] = 1

    timelines = 1
    for row in range(1, len(data)):
        if row % 2 == 1:
            continue

        for col in list(beams):
            if data[row][col] == "^":
                incoming_beams = beams[col]
                timelines += incoming_beams
                del beams[col]

                new_beam_1 = col - 1
                new_beam_2 = col + 1

                if new_beam_1 not in beams:
                    beams[new_beam_1] = incoming_beams
                else:
                    beams[new_beam_1] += incoming_beams

                if new_beam_2 not in beams:
                    beams[new_beam_2] = incoming_beams
                else:
                    beams[new_beam_2] += incoming_beams

    return timelines


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
