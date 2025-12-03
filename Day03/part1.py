# Problem description:
# Each line is a bank of batteries
# Turn on two and combine numbers (2 + 4 -> 24)
# Sum up joltage

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
#input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_max_joltage(bank):
    size = len(bank)

    # get first number
    first_number = -1
    index = -1
    for i in range(0, size - 1):
        num = int(bank[i])
        if num > first_number:
            first_number = num
            index = i
        if num == 9:
            break

    # get second number
    second_number = -1
    for i in range(index + 1, size):
        num = int(bank[i])
        if num > second_number:
            second_number = num
        if num == 9:
            break

    return first_number * 10 + second_number


def get_answer():
    answer = 0

    for line in input_file:
        answer += get_max_joltage(line.strip())

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
