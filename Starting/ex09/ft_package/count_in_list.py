

def count_in_list(lst: list, item):
        """Count the number of items in a list.
        
        The function receives two parameters the items list and the item to count.
        Uses the method count from the List class

        Args:
                arg1(list): list of items
                arg2(item): item to be searched
        """
        val = lst.count(item)
        return val