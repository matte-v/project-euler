from pathlib import Path

PROBLEM_FILES_PATH = Path(__file__).parent.parent.resolve() / 'problem_files'


def read_problem_file(filename) -> str:
    with (PROBLEM_FILES_PATH / filename).open() as f:
        content = f.read()
    return content
