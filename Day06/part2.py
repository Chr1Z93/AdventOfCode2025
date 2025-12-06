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

    data = []
    i = -1
    for line in input_file:
        i += 1
        data.append(line)

    operators = data[i]
    line_length = len(operators) - 1

    j = -1
    for char in operators:
        j += 1
        if char == " " or char == "\n":
            continue
        #print(f"j: {j} | char: {char}")

        result = 0
        if char == "*":
            result = 1

        for k in range(j, j + 5):
            if k > line_length or (k != j and operators[k] != " "):
                break

            num = build_number(data, k)
            if num == False:
                break

            #print(f"k: {k} | num: {num}")
            if char == "+":
                result += num
            elif char == "*":
                result *= num

        #print(f"result: {result}")
        answer += result

    return answer


def build_number(data, id):
    string = ""
    for line in data:
        char = line[id]
        if char != "+" and char != "*":
            string += line[id]
    string = string.strip()
    if string == "":
        return False
    return int(string)


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
