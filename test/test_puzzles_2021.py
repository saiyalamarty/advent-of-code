from importlib import import_module

import pytest


@pytest.mark.parametrize(
    "day, result",
    [
        ("day_1", (1292, 1262)),
        ("day_2", (1604850, 1685186100)),
        ("day_3", (2003336, 1877139)),
        ("day_4", (89001, 7296)),
        ("day_5", (6005, 23864)),
        ("day_6", (350917, 1592918715629)),
        ("day_7", (349769, 99540554)),
        ("day_8", (344, 1048410)),
        ("day_9", (468, 1280496)),
        ("day_10", (296535, 4245130838)),
        ("day_11", (1647, 348)),
        ("day_12", (5756, 144603)),
        ("day_13", 655),
        ("day_14", (3143, 4110215602456)),
        ("day_15", (619, 2922)),
        ("day_16", (949, 1114600142730)),
    ],
    ids=[
        "Day 1",
        "Day 2",
        "Day 3",
        "Day 4",
        "Day 5",
        "Day 6",
        "Day 7",
        "Day 8",
        "Day 9",
        "Day 10",
        "Day 11",
        "Day 12",
        "Day 13",
        "Day 14",
        "Day 15",
        "Day 16",
    ],
)
def test_puzzles(day, result):
    import_path = f"src.year_2021.{day}.puzzle"
    module = import_module(import_path)
    main = getattr(module, "main")

    assert main() == result
