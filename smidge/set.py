class set(__builtins__['set']):
    '''
    set() -> new empty set
    set(*iterable) -> new set of many items
    set(item) -> new set of 1 item
    set(item1, item2, item3) -> new set of 3 items

    Build a collection of unique elements.
    '''
    def __init__(set, *params):
        super().__init__(params)
    def one(set):
        '''Converts a set of one item into its item.

        Returns:
            Unwrapped item

        Raises:
            KeyError if the set is not of size 1
        '''
        for item in set:
            if len(set) != 1:
                raise KeyError('multiple items')
            return item
        raise KeyError('not found')
    def first(set):
        '''Retrieves the first item from iterating a set.

        Returns:
            First item found

        Raises:
            KeyError if the set is empty
        '''
        for item in set:
            return item
        raise KeyError('not found')
