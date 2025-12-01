# Problem description:
# Safe opening via dial
# Count any time it ends up on 0

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

        # Perform rotation
        if direction == "R":
            value += rotation
        else:
            value -= rotation

        # Only keep last two digits
        value = value % 100

        if value == 0:
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
