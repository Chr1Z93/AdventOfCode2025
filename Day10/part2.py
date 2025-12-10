# Problem description:
# Machine manual parsing
# One machine per line

from pathlib import Path
import time
import re
import numpy as np
import itertools

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

# input_path = script_dir / "input.txt"
input_path = script_dir / "example.txt"

input_file = open(input_path)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
joltage_pattern = r"\{.*\}"
button_pattern = r"\((.+?)\)"


def get_answer():
    answer = 0

    i = -1
    for line in input_file:
        i += 1

        # This vector holds the joltage to indicate the final state
        joltage_vector, size = get_joltage_vector(line)

        # This matrix holds [0, 1] in each element and each column corresponds to a single button
        button_matrix, button_count = get_button_matrix(line, size)  # type: ignore

        # Loop through all possible button press combinations until the smallest result is found
        min_presses = None
        for tuple in itertools.product(elements, repeat=button_count):
            vector = np.array(tuple)
            button_presses = np.sum(vector)

            if min_presses != None and button_presses >= min_presses:
                continue

            # If resulting state after pressing the buttons matches, this might be the new solution
            if (button_matrix @ vector == joltage_vector).all():
                min_presses = button_presses

        # Add the number of button presses to the answer
        if not min_presses:
            print("No solution found!")
        else:
            print("-" * 10)
            print(f"Line: {i + 1}")
            print(f"Presses: {min_presses}")
            answer += min_presses

    return answer


def get_joltage_vector(line):
    matches = re.search(joltage_pattern, line)
    components = []

    for section in matches[0].split(","):  # type: ignore
        string = section.replace("{", "").replace("}", "")
        components.append(int(string))

    return np.array(components), len(components)


def get_button_matrix(line, size):
    matches = re.findall(button_pattern, line)
    if matches:
        components = []
        button_count = 0
        for match in matches:
            button_count += 1
            button = [0] * size
            for value in match.split(","):
                button[int(value)] = 1

            components.append(button)

        return np.array(components).T, button_count


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
