class set(__builtins__['set']):
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
