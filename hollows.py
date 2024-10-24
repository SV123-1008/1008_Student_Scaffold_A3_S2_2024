from __future__ import annotations
"""
Ensure you have read the introduction and task 1 and understand what 
is prohibited in this task.
This includes:
The ban on inbuilt sort methods .sort() or sorted() in this task.
And ensure your treasure data structure is not banned.

"""
from abc import ABC, abstractmethod
from typing import List

from config import Tiles
from treasure import Treasure, generate_treasures
from betterbst import BetterBST
from data_structures.heap import MaxHeap

class Hollow(ABC):
    """
    DO NOT MODIFY THIS CLASS
    Mystical troves of treasure that can be found in the maze
    There are two types of hollows that can be found in the maze:
    - Spooky Hollows: Each of these hollows contains unique treasures that can be found nowhere else in the maze.
    - Mystical Hollows: These hollows contain a random assortment of treasures like the spooky hollow however all mystical hollows are connected, so if you remove a treasure from one mystical hollow, it will be removed from all other mystical hollows.
    """

    # DO NOT MODIFY THIS ABSTRACT CLASS
    """
    Initialises the treasures in this hollow
    """

    def __init__(self) -> None:
        self.treasures = self.gen_treasures()
        self.restructure_hollow()

    @staticmethod
    def gen_treasures() -> List[Treasure]:
        """
        This is done here, so we can replace it later on in the auto marker.
        This method contains the logic to generate treasures for the hollows.

        Returns:
            List[Treasure]: A list of treasures that can be found in the maze
        """
        return generate_treasures()

    @abstractmethod
    def restructure_hollow(self):
        pass

    @abstractmethod
    def get_optimal_treasure(self, backpack_capacity: int) -> Treasure | None:
        pass

    def __len__(self) -> int:
        """
        After the restructure_hollow method is called, the treasures attribute should be updated
        don't create an additional attribute to store the number of treasures in the hollow.
        """
        return len(self.treasures)


class SpookyHollow(Hollow):

    def restructure_hollow(self) -> None:
        """
        Re-arranges the treasures in the hollow from a list to a new
        data structure that is better suited for the get_optimal_treasure method.

        The new treasures data structure can't be an ArrayR or list variant (LinkedList, python list, sorted list, ...).
        No lists! Breaching this will count as a major error and lose up to 100% of the marks of the task!

        Returns:
            None - This method should update the treasures attribute of the hollow

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: TODO
            Worst Case Complexity: TODO

        Complexity requirements for full marks:
            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)
            Where n is the number of treasures in the hollow
        """
        treasure_tree_list = []
        for treasure in self.treasures:
            r = -treasure.value/treasure.weight
            treasure_tree_list.append((r,treasure))
        
        self.treasures = BetterBST(treasure_tree_list)

    def get_optimal_treasure(self, backpack_capacity: int) -> Treasure | None:
        """
        Removes the ideal treasure from the hollow 
        Takes the treasure which has the greatest value / weight ratio 
        that is less than or equal to the backpack_capacity of the player as
        we can't carry treasures that are heavier than our backpack capacity.

        Ensure there are only changes to the treasures contained in the hollow
        if there is a viable treasure to take. If there is a viable treasure
        only remove that treasure from the hollow, no other treasures should be removed.

        Returns:
            Treasure - the ideal treasure that the player should take.
            None - if all treasures are heavier than the backpack_capacity
            or the hollow is empty

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: TODO
            Worst Case Complexity: TODO

        Complexity requirements for full marks:
            Best Case Complexity: O(log(n))
            Worst Case Complexity: O(n)
            n is the number of treasures in the hollow 
        """
        
        for treasure_node in self.treasures:
            if treasure_node.item.weight <= backpack_capacity:
                del self.treasure_tree[treasure_node.key]
                return treasure_node.item

    def __str__(self) -> str:
        return Tiles.SPOOKY_HOLLOW.value

    def __repr__(self) -> str:
        return str(self)


class MysticalHollow(Hollow):

    def restructure_hollow(self):
        """
        Re-arranges the treasures in the hollow from a list to a new
        data structure that is better suited for the get_optimal_treasure method.

        The new treasures data structure can't be an ArrayR or list variant (LinkedList, python list, sorted list, ...).
        No lists! Breaching this will count as a major error and lose up to 100% of the marks of the task! 

        Returns:
            None - This method should update the treasures attribute of the hollow

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: TODO
            Worst Case Complexity: TODO

        Complexity requirements for full marks:
            Best Case Complexity: O(n)
            Worst Case Complexity: O(n)
            Where n is the number of treasures in the hollow
        """
        treasure_tree_list = []
        for treasure in self.treasures:
            r = -treasure.value/treasure.weight
            treasure_tree_list.append((r,treasure))
        
        self.treasures = MaxHeap(len(treasure_tree_list))
        self.treasures.heapify(treasure_tree_list)

    def get_optimal_treasure(self, backpack_capacity: int) -> Treasure | None:
        """
        Removes the ideal treasure from the hollow 
        Takes the treasure which has the greatest value / weight ratio 
        that is less than or equal to the backpack_capacity of the player as
        we can't carry treasures that are heavier than our backpack capacity.

        Ensure there are only changes to the treasures contained in the hollow
        if there is a viable treasure to take. If there is a viable treasure
        only remove that treasure from the hollow, no other treasures should be removed.

        Returns:
            Treasure - the ideal treasure that the player should take.
            None - if all treasures are heavier than the backpack_capacity
            or the hollow is empty

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: TODO
            Worst Case Complexity: TODO

        Complexity requirements for full marks:
            Best Case Complexity: O(log n)
            Worst Case Complexity: O(n log n)
            Where n is the number of treasures in the hollow
        """
        #check while iterating over self.treasure, check if the len of self.treasures is greater than 0, then MaxHeap function called get_max, while loop is running
        #take the treasure out using self.treasure.get_max() which will return a treasure and assign a variable and check if treasure, it is a tuple so treasure[1].weight (2nd index) make sure it is less than backpack capacity
        # if less than backpack capacity append to temp_list and return and if greater than backpack capacity append to temp_list but dont return anything
        # after while loop go through temp_list returns None in the end

        temp_list = []
        while len(self.treasures) > 0:
            best_treasure = self.treasures.get_max()
             
            if best_treasure.weight <= backpack_capacity:
                return best_treasure

            temp_list.append(best_treasure)

        for treasure in temp_list:
            self.treasures.insert(treasure)

        return None
    

    def __str__(self) -> str:
        return Tiles.MYSTICAL_HOLLOW.value

    def __repr__(self) -> str:
        return str(self)
