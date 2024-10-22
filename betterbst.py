from __future__ import annotations
from typing import List, Tuple, TypeVar
from data_structures.bst import BinarySearchTree
from algorithms.mergesort import mergesort

K = TypeVar('K')
I = TypeVar('I')


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: List[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements list.

        As such you can assume the length of elements to be non-zero.
        The elements list will contain tuples of key, item pairs.

        First sort the elements list and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(List[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: 
            Worst Case Complexity: 
        """
        super().__init__()
        new_elements: List[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: List[Tuple[K, I]]) -> List[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            list(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O(n * log(n))
            Worst Case Complexity: O(n * log(n))
            where n is the number of elements in the input / the final number of nodes in the tree.
        """
        
        return mergesort(elements, sort_key=lambda x: x[0])

    def __build_balanced_tree(self, elements: List[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: O(n * log(n))
            Worst Case Complexity: O(n * log(n))
            where n is the number of elements in the input / the final number of nodes in the tree.

        Justification:
            The function constructs the fully balanced binary search tree through an efficient selection of a middle item.
            used the first item of the sorted list as the root and then applies the same to the left and right sublists.
            Since in a balanced tree which insertion takes O(log(n)) we are inserting n elements then total time.
            complexity is O(n * log(n)).

        Complexity requirements for full marks:
            Best Case Complexity: O(n * log(n))
            Worst Case Complexity: O(n * log(n))
            where n is the number of elements in the list.
        """
        # reset the tree
        self.root = None
        self.length = 0

        # initialize stack for ranges
        stack = [(0, len(elements) - 1)]

        # process ranges in stack
        while stack:
            start, end = stack.pop()

            # skip invalid ranges
            if start > end:
                continue

            # find middle index
            mid = (start + end) // 2

            # insert middle element
            key, item = elements[mid]
            self[key] = item

            # add right and left ranges to stack
            stack.append((mid + 1, end))  # right side
            stack.append((start, mid - 1))  # left side
            