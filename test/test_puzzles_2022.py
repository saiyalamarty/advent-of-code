from importlib import import_module

import pytest


@pytest.mark.parametrize(
    "day, result",
    [
        ("day_1", (70116, 206582)),
    ],
    ids=["Day 1"],
)
def test_puzzles(day, result):
    import_path = f"src.year_2022.{day}.puzzle"
    module = import_module(import_path)
    main = getattr(module, "main")

    assert main() == result
