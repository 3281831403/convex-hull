"""凸包：单调链、面积与点判定：待实现的核心模块。"""


def convex_hull(points):
    """单调链凸包。"""
    raise NotImplementedError

def hull_area(hull):
    """凸包面积。"""
    raise NotImplementedError

def point_in_hull(point, hull):
    """点是否在凸包内（含边界）。"""
    raise NotImplementedError

def hull_perimeter(hull):
    """凸包周长。"""
    raise NotImplementedError

def remove_collinear(hull):
    """剔除共线中间点。"""
    raise NotImplementedError
