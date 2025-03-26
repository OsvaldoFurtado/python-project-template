"""
Python Projects
Project Zero: A template for other projects
"""

import shlex
import subprocess
from pathlib import Path

from behave import then, when  # type: ignore


@when('we run command "{command}"')
def run_command(context, command):
    output_path = Path("output.log")
    with output_path.open("w") as target:
        status = subprocess.run(
            shlex.split(command),
            check=True,
            text=True,
            stdout=target,
            stderr=subprocess.STDOUT,
        )
    context.status = status
    context.output = output_path.read_text()
    output_path.unlink()
    # print(f"{context=} {context.status=} {context.output=}")


@then('output has "{expected_output}"')
def check_output(context, expected_output):
    # print(f"{context=} {context.status=} {context.output=}")
    assert context.status.returncode == 0
    assert expected_output in context.output
