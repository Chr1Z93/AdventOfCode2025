# Problem description:
# Path connections for server rack
# you -> out

from pathlib import Path
import time
import networkx as nx


# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example.txt"

input_file = open(input_path)


def get_answer():
    map = {}

    for line in input_file:
        parts = line.split(": ")
        map[parts[0]] = parts[1].strip().split(" ")

    G = nx.DiGraph(map)
    paths = list(nx.all_simple_paths(G, "you", "out"))
    answer = len(paths)

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
