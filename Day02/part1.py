# Problem description:
# Parse ID ranges
# Identify IDs with first half = second half
# Sum up those IDs

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example.txt"

input_file = open(input_path)


def parse_input():
    list_of_ranges = []

    for line in input_file:
        for range_data in line.strip().split(","):
            range_split = range_data.split("-")
            range_dict = {"start": int(range_split[0]), "end": int(range_split[1])}
            list_of_ranges.append(range_dict)
    return list_of_ranges

cache = {}
def is_invalid(number):
    if number in cache:
        return cache[number]

    number_string = str(number)
    length = len(number_string)

    # odd number of digits can't be invalid
    if length % 2 == 1:
        cache[number] = False
        return False

    first_half = number_string[0 : int(length / 2)]
    second_half = number_string[int(length / 2) :]
    result = first_half == second_half

    cache[number] = result
    return result


def get_answer():
    list_of_ranges = parse_input()

    answer = 0

    for range_dict in list_of_ranges:
        for number in range(range_dict["start"], range_dict["end"] + 1):
            if is_invalid(number):
                answer += number

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
