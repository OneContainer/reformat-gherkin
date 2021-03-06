from reformat_gherkin.options import (
    AlignmentMode,
    NewlineMode,
    Options,
    TagLineMode,
    WriteBackMode,
)


def make_options(
    *,
    step_keyword_alignment=AlignmentMode.NONE,
    tag_line_mode=TagLineMode.SINGLELINE,
    indent="  ",
):
    return Options(
        write_back=WriteBackMode.CHECK,
        step_keyword_alignment=step_keyword_alignment,
        newline=NewlineMode.KEEP,
        tag_line_mode=tag_line_mode,
        fast=False,
        indent=indent,
    )


OPTIONS = [
    make_options(step_keyword_alignment=alignment_mode)
    for alignment_mode in AlignmentMode
]

FILENAME_OPTION_MAP = {
    "expected_default": make_options(step_keyword_alignment=AlignmentMode.NONE),
    "expected_left_aligned": make_options(step_keyword_alignment=AlignmentMode.LEFT),
    "expected_right_aligned": make_options(step_keyword_alignment=AlignmentMode.RIGHT),
    "expected_multi_line_tags": make_options(tag_line_mode=TagLineMode.MULTILINE),
    "expected_use_tabs": make_options(indent="\t"),
}


def get_content(dir_name):
    with open(f"tests/data/valid/{dir_name}/input.feature") as f:
        return f.read()


def dump_to_stderr(*output: str) -> str:
    return "\n" + "\n".join(output) + "\n"
