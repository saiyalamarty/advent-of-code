import pytest
from importlib import import_module


@pytest.mark.parametrize(
    "day, result",
    [
        ("day_1", (1292, 1262)),
        ("day_2", (1604850, 1685186100)),
        ("day_3", (2003336, 1877139))
    ],
    ids=["Day 1", "Day 2", "Day 3"]
)
def test_puzzles(day, result):
    import_path = f"src.2021.{day}.puzzle"
    module = import_module(import_path)
    main = getattr(module, "main")

    assert main() == result
