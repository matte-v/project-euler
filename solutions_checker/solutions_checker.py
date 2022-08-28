import json
import os
import re
from pathlib import Path
from typing import Dict

this_file_folder = Path(__file__).parent.resolve()
tmp_file_path = this_file_folder / "tmp_solutions_checker.txt"
solutions_file = this_file_folder / "solutions.json"


def run_all_problems():
    problem_files = [x for x in this_file_folder.parent.resolve().glob("*/*.py") if re.search(r'\d+', str(x))]
    problem_files.sort(key=lambda x: int(str(x.stem)))
    print(f"Running all problems...")
    for f in problem_files:
        os.system(f'echo Problem {f.stem} >> {tmp_file_path} '
                  f'&& python3 {f.absolute()} >> {tmp_file_path} 2>&1')
    print(f"Done")


def parse_outfile():
    problems = []
    solutions = []
    with Path(tmp_file_path).open() as f:
        while line := f.readline():
            if problem_match := re.search(r'Problem (\d+)', line):
                problems.append(problem_match.group(1))
            elif solution_match := re.search(r'The solution is ([-\d]+)', line):
                solutions.append(int(solution_match.group(1)))
            elif re.search('Traceback', line):
                solutions.append(None)
    return dict(zip(problems, solutions))


def cleanup():
    Path(tmp_file_path).unlink(missing_ok=True)


def load_solutions_dict():
    with solutions_file.open() as f:
        return json.load(f)


def run_comparison(expected: Dict, actual: Dict):
    common_keys = set(expected.keys()).intersection(set(actual.keys()))
    comparison = {}
    for k in sorted(common_keys, key=lambda kk: int(kk)):
        if expected[k] == actual[k]:
            comparison[k] = 'OK'
        elif actual[k] is None:
            comparison[k] = 'ERROR'
        else:
            comparison[k] = f'NOT OK - expected {expected[k]}, got {actual[k]}'
        print(f"{k} -> {comparison[k]}")
    print("---------- Comparison results ----------")
    if len(expected.keys()) != len(actual.keys()):
        print(f"Warning: {len(actual.keys())} problem files vs. {len(expected.keys())} solutions")
        missing_actual = set(expected.keys()) - set(actual.keys())
        if missing_actual:
            print(f"Problem files are missing for these problems: {missing_actual}")
        missing_expected = set(actual.keys()) - set(expected.keys())
        if missing_expected:
            print(f"Official solutions are missing for these problems: {missing_expected}")
    print(f"{len([v for v in comparison.values() if v == 'OK'])} problems OK")
    print(f"{len([v for v in comparison.values() if v.startswith('NOT OK')])} problems NOT OK")
    print(f"{len([v for v in comparison.values() if v == 'ERROR'])} problems ERROR")
    print("----------------------------------------")


if __name__ == '__main__':
    """
    This checks for regression in already-solved problems, e.g. after refactoring common functions
    """
    cleanup()
    official_solutions_dict = load_solutions_dict()
    run_all_problems()
    problem_solution_dict = parse_outfile()
    run_comparison(official_solutions_dict, problem_solution_dict)
