def subsets(elements):
    if not elements:
        # returning 2D list because the function requires to return 2D list data type
        return [ [] ]

    first = elements[0]
    without = subsets(elements[1:])

    with_first = []
    for sub in without:
        with_first.append([*sub, first])

    # with_first = [sub + [first] for sub in without]

    return without + with_first

