from importlib import import_module

import pytest


@pytest.mark.parametrize(
    "day, result",
    [
        ("day_1", (70116, 206582)),
        ("day_2", (9177, 12111)),
        ("day_3", (8252, 2828)),
    ],
    ids=[
        "Day 1",
        "Day 2",
        "Day 3",
    ],
)
def test_puzzles(day, result):
    import_path = f"src.year_2022.{day}.puzzle"
    module = import_module(import_path)
    main = getattr(module, "main")

    assert main() == result
