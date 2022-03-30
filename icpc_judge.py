import argparse
import os
import re
import resource
import subprocess
import sys
from enum import Enum


class STATUS(Enum):
    AC = 0
    WA = 1
    TLE = 2
    RTE = 3


def parse_args():
    parser = argparse.ArgumentParser(description="Custom judge for past ICPC problems.")
    parser.add_argument(
        "program",
        metavar="PROGRAM-PATH",
        type=str,
        help="Path to the python program to test.",
    )
    parser.add_argument(
        "problem", metavar="PROBLEM-PATH", type=str, help="Path to the problem folder."
    )
    parser.add_argument(
        "--use-pypy",
        action="store_true",
        help="The provided program will be run with pypy3 interpreter.",
    )
    parser.add_argument(
        "--practice-mode",
        action="store_true",
        help="Run the code against every test case, showing status for each of them.",
    )
    return parser.parse_args()


def locate_pypy():
    for path in os.environ["PATH"].split(":"):
        try:
            for file in os.listdir(path):
                if file == "pypy3":
                    return os.path.join(path, file)
        except FileNotFoundError:
            continue

    raise RuntimeError(
        f"pypy3 executable cannot be found in $PATH = {os.environ['PATH']}"
    )


def load_problem_config(problem_path):
    # Default time 1 secs, default heap size 2GiB, taken from:
    # https://pc2.ecs.csus.edu/cli/Problem_format_1.0.pdf
    config = {"time": 1, "memory": 2048}
    config_path = os.path.join(problem_path, "problem.yaml")

    if not os.path.exists(config_path):
        print(
            f"[WARNING] Problem config not found: {config_path}. Running with default limits."
        )
        return config

    with open(config_path, "r") as f:
        contents = f.readlines()

    limits_section = False
    for line in contents:
        if not limits_section and line.startswith("limits"):
            limits_section = True
        elif limits_section and not line.startswith("  "):
            break
        elif limits_section and line.startswith("  validation_time:"):
            match = re.search("  validation_time: (\d+)", line)
            config["time"] = int(match.group(1))
        elif limits_section and line.startswith("  memory:"):
            match = re.search("  memory: (\d+)", line)
            config["memory"] = int(match.group(1))

    return config


def exec_runner(interpreter, program_path, problem_path, practice_mode=False):
    config = load_problem_config(problem_path)
    for test_set in ["sample", "secret"]:
        test_set_path = os.path.join(problem_path, "data", test_set)
        for filename in filter(lambda x: x.endswith(".in"), os.listdir(test_set_path)):
            file_path = os.path.join(test_set_path, filename)
            result = execute([interpreter, program_path], file_path, config)
            if result != STATUS.AC and not practice_mode:
                print(result.name)
                return
            elif practice_mode:
                print(f"{result.name:3s} {filename}")

    if not practice_mode:
        print("All tests passed! Well done!")


def set_memory_limits(mem):
    if mem is not None:
        max_mem = mem * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (max_mem, max_mem))


def validate_answer(output, answer_file, save_output=True):
    if save_output:
        with open(f"{os.path.splitext(answer_file)[0]}.out", "w") as f:
            f.write(output)

    with open(answer_file, "r") as f:
        contents = f.read()

    if len(output) != len(contents):
        return STATUS.WA

    for idx in range(len(output)):
        if output[idx] != contents[idx]:
            return STATUS.WA

    return STATUS.AC


def execute(cmd, input_file, config):
    try:
        proc = subprocess.run(
            cmd,
            stdin=open(input_file, "r"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=config["time"],
            preexec_fn=lambda: set_memory_limits(config["memory"]),
        )

        if proc.returncode != 0:
            return STATUS.RTE

        answer_file = f"{os.path.splitext(input_file)[0]}.ans"
        return validate_answer(proc.stdout.decode("utf-8"), answer_file)
    except subprocess.TimeoutExpired:
        return STATUS.TLE


if __name__ == "__main__":
    args = parse_args()

    python_interpreter = sys.executable
    if args.use_pypy:
        python_interpreter = locate_pypy()

    exec_runner(
        python_interpreter, args.program, args.problem, practice_mode=args.practice_mode
    )
