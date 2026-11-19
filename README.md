# 凸包：单调链、面积与点判定

凸包把共线点也包进去、面积偏大：单调链没有排序去重，叉积方向反了，共线点没有剔除，面积用周长近似，点在凸包内判定漏掉边界，周长按包围盒算，批量凸包只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
geometry/__init__.py
geometry/convex_hull.py
tests/test_convex_hull.py
```

## 当前状态

`geometry/convex_hull.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_convex_hull.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 单调链排序去重
2. 叉积方向正确
3. 共线点剔除
4. 面积用鞋带公式
5. 点判定含边界
6. 周长按边累加
7. 批量凸包统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `geometry/convex_hull.py`
后 15 条用例应全部通过。
