# Problem description:
# Path connections for server rack
# svr -> out
# must visit dac and fft

from pathlib import Path
import time
import networkx as nx

# get correct subfolder path
script_path = Path(__file__).resolve()
script_dir = script_path.parent

input_path = script_dir / "input.txt"
# input_path = script_dir / "example2.txt"

input_file = open(input_path)


def get_answer():
    answer = 0
    map = {}

    for line in input_file:
        parts = line.split(": ")
        map[parts[0]] = parts[1].strip().split(" ")

    graph = nx.DiGraph(map)

    # svr > dac > fft > out
    s1 = len(list(nx.all_simple_paths(graph, "svr", "dac")))
    s2 = len(list(nx.all_simple_paths(graph, "dac", "fft")))
    s3 = len(list(nx.all_simple_paths(graph, "fft", "out")))
    answer += s1 * s2 * s3

    # svr > fft > dac > out
    s1 = len(list(nx.all_simple_paths(graph, "svr", "fft")))
    s2 = len(list(nx.all_simple_paths(graph, "fft", "dac")))
    s3 = len(list(nx.all_simple_paths(graph, "dac", "out")))
    answer += s1 * s2 * s3

    return answer


# start timer and run main code
start_time = time.perf_counter()
answer = get_answer()
execution_time_ms = (time.perf_counter() - start_time) * 1000

# output results
print(f"{script_path.parent.name} - {script_path.name}")
print(f"Timing: {execution_time_ms:.3f} ms")
print(f"Answer: {answer}")
