def deep_equal(a_element, b_element):
    """Computes whether two different elements are deep equal.

    Two elements are considered deep equal if:
     1. Their tag names are equal
     2. Their attributes are equal
     3. Their text contents (including the tail contents) are equal.
        Note that text contents are stripped of starting and ending
        whitespace.
     3. Their children are pairwise deep equal
    """
    if a_element.tag != b_element.tag:
        return False

    if len(a_element.items()) != len(b_element.items()):
        return False

    for key in a_element.keys():
        if a_element.get(key) != b_element.get(key):
            return False

    if a_element.tail.strip() != b_element.tail.strip():
        return False

    if a_element.text.strip() != b_element.text.strip():
        return False

    if len(a_element) != len(b_element):
        return False

    for pair in zip(a_element, b_element):
        if not deep_equal(*pair):
            return False

    return True
