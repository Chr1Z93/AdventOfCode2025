# Problem description:
# Each line is a bank of batteries
# Turn on twelve and combine numbers (2 + 4 -> 24)
# Sum up joltage

from pathlib import Path
import time

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
#input_path = script_dir / "example.txt"

input_file = open(input_path)

batterie_count = 12

def get_max_joltage(bank):
    size = len(bank)

    resulting_numbers = [-1] * batterie_count

    bank_index = -1
    for batterie_index in range(0, batterie_count):
        for i in range(bank_index + 1, size - (batterie_count - batterie_index) + 1):
            num = int(bank[i])
            if num > resulting_numbers[batterie_index]:
                resulting_numbers[batterie_index] = num
                bank_index = i
            if num == 9:
                break # find next batterie

    # build number
    result = ""
    for number in resulting_numbers:
        result += str(number)

    return int(result)


def get_answer():
    answer = 0

    for line in input_file:
        joltage = get_max_joltage(line.strip())
        answer += joltage

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
