from os.path import join
from pathlib import Path
from typing import List

from src.utils import read_text_file


def get_current_file_dir() -> str:
    return f"{Path(__file__).absolute().parent.resolve()}"


TEST1_TXT = join(get_current_file_dir(), "inputs", "test1.txt")
TEST2_TXT = join(get_current_file_dir(), "inputs", "test2.txt")
INPUT_TXT = join(get_current_file_dir(), "inputs", "input.txt")
SAMPLE_TXT = join(get_current_file_dir(), "inputs", "sample.txt")


def get_parsed_input1(lines: List[str]):
    parsed = []
    for l in lines:
        parsed.append([_.strip() for _ in l.split(" ")])
    return parsed


def main(
    input_file: str = TEST1_TXT,
) -> List[int]:
    lines = read_text_file(input_file)

    _ = [print(_) for _ in lines]
