# Problem description:
# Machine manual parsing
# One machine per line

from pathlib import Path
import time
import re
import numpy as np
import pulp

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example.txt"

input_file = open(input_path)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
joltage_pattern = r"\{.*\}"
button_pattern = r"\((.+?)\)"


def get_answer():
    answer = 0

    line_id = -1
    for line in input_file:
        line_id += 1

        # This vector holds the joltage to indicate the final state (b)
        joltage_vector, size = get_joltage_vector(line)

        # This matrix holds [0, 1] in each element and each column corresponds to a single button (A)
        button_matrix, button_count = get_button_matrix(line, size)  # type: ignore

        # Setup the problem: Minimize the objective
        prob = pulp.LpProblem("", pulp.LpMinimize)

        # Define Variables (x_i are the button presses, constrained to [0, 9] and Integer)
        button_vars = []
        for j in range(button_count):
            button_vars.append(
                pulp.LpVariable(f"x_{j}", lowBound=0, upBound=9, cat="Integer")
            )

        # Define Objective Function (Minimize the sum of presses: min ||x||_1)
        prob += pulp.lpSum(button_vars)

        for j in range(size):
            # Calculate the left-hand side (LHS) of the j-th equation: (A[j,:] dot x)
            lhs = pulp.lpSum(
                button_matrix[j, i] * button_vars[i] for i in range(button_count)
            )

            # Constraint: LHS must equal the RHS (joltage_vector[j])
            prob += lhs == joltage_vector[j]

        prob.solve(pulp.PULP_CBC_CMD(msg=0))  # type: ignore

        min_presses = None
        if prob.status == pulp.LpStatusOptimal:
            min_presses = pulp.value(prob.objective)

        # Add the number of button presses to the answer
        if not min_presses:
            print(f"Line {line_id+1}: No solution found!")
        else:
            print(f"{line_id}: {min_presses}")
            answer += int(min_presses)  # type: ignore

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
