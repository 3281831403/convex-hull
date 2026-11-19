import pytest

from geometry import convex_hull as mod

CASES = [
    ('convex_hull', [[[0, 0], [2, 0], [1, 1], [2, 2], [0, 2]]], [[0, 0], [2, 0], [2, 2], [0, 2]], False),
    ('convex_hull', [[[0, 0], [1, 0], [2, 0]]], [[0, 0], [2, 0]], False),
    ('hull_area', [[[0, 0], [2, 0], [2, 2], [0, 2]]], 4.0, True),
    ('point_in_hull', [[1, 1], [[0, 0], [2, 0], [2, 2], [0, 2]]], True, False),
    ('point_in_hull', [[3, 1], [[0, 0], [2, 0], [2, 2], [0, 2]]], False, False),
    ('hull_perimeter', [[[0, 0], [3, 0], [3, 4]]], 12.0, True),
    ('remove_collinear', [[[0, 0], [1, 0], [2, 0], [2, 2]]], [[0, 0], [2, 0], [2, 2]], False),
    ('convex_hull', [[[1, 0], [0, 1], [1, 1]]], [[0, 1], [1, 0], [1, 1]], False),
    ('convex_hull', [[[0, 0], [0, 2], [2, 2], [2, 0], [1, 1]]], [[0, 0], [2, 0], [2, 2], [0, 2]], False),
    ('convex_hull', [[[0, 0], [1, 1]]], [[0, 0], [1, 1]], False),
    ('hull_area', [[[0, 0], [1, 0], [1, 1]]], 0.5, True),
    ('hull_area', [[[0, 0], [0, 3], [3, 3], [3, 0]]], 9.0, True),
    ('point_in_hull', [[0, 0], [[0, 0], [2, 0], [2, 2], [0, 2]]], True, False),
    ('hull_perimeter', [[[0, 0], [0, 2], [2, 2], [2, 0]]], 8.0, True),
    ('remove_collinear', [[[0, 0], [2, 0], [4, 0], [4, 4]]], [[0, 0], [4, 0], [4, 4]], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_convex_hull_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
