# Problem description:
# Map with "." and "^"
# Starting point -> Beams emitted
# Count number of splits

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
    beams = {start}

    for row in range(1, len(data)):
        beam_splits = 0
        for col in set(beams):
            if data[row][col] == ".":
                data[row][col] = "|"
            else:
                beams.remove(col)
                new_beam_1 = col - 1
                new_beam_2 = col + 1
                beam_splits += 1

                if new_beam_1 not in beams:
                    beams.add(new_beam_1)
                    data[row][new_beam_1] = "|"

                if new_beam_2 not in beams:
                    beams.add(new_beam_2)
                    data[row][new_beam_2] = "|"

        if beam_splits > 0:
            #print(f"Splits: {beam_splits}")
            answer += beam_splits

    #for line in data:
    #    print(" ".join(line))
    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
