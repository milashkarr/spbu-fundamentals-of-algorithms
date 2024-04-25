from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import os

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:  # Конструктор, инициализирует пустое дерево
        self.root: Node = None  

    def empty(self) -> bool:  # Пустое ли дерево?
        return self.root is None

    def zigzag_level_order_traversal(self) -> List[List[Any]]:
        if self.empty():
            return []

        result = []
        current_stack = [self.root]  # Cтек для обхода текущего уровня
        next_stack = []  # Cтек для обхода следующего уровня
        left_to_right = True  # Флаг для определения направления обхода

        while current_stack:
            level_values = []

            while current_stack:
                node = current_stack.pop()
                level_values.append(node.key)

                if left_to_right:
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)
                else:
                    if node.right:
                        next_stack.append(node.right)
                    if node.left:
                        next_stack.append(node.left)

            result.append(level_values)
            current_stack, next_stack = next_stack, current_stack
            left_to_right = not left_to_right

        return result


def build_tree(list_view: List[Any]) -> BinaryTree:
    bt = BinaryTree()

    if not list_view:
        return BinaryTree()
    
    bt = BinaryTree()
    bt.root = Node(list_view[0])
    queue = [bt.root]
    i = 1

    while queue and i < len(list_view):
        current_node = queue.pop(0)

        if list_view[i] is not None:  # Если следующий элемент в списке не None, добавляем левого потомка
            current_node.left = Node(list_view[i])
            queue.append(current_node.left)
        i += 1

        if list_view[i] is not None:  # Если следующий элемент в списке не None, добавляем правого потомка
            current_node.right = Node(list_view[i])
            queue.append(current_node.right)
        i += 1

    return bt

if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        os.path.join(
            "practicum_5",
            "homework",
            "basic",
            "binary_tree_zigzag_level_order_traversal_cases.yaml",
        ),
        "r",
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
