def generate_permutations(original_list, permutation = []):
    """
    Base/End case here is when
    we reach a recursive tree depth
    of three or a permuation list reaches
    a size equal to that of the original list.
    Both showcase the fact we've reached our
    desired recursion depth.

    """

    # When we reach max depth we want to return the
    # Permutation we've obtained
    if len(permutation) == len(original_list):
        return [permutation.copy()]

    # This list captures all the permutations
    # we've created in each recursion stack
    permutations = []

    for index in range(len(original_list)):

        permutation.append(original_list[index])

        permutations += generate_permutations(
            original_list,
            permutation
        )
        permutation.pop()

    return permutations


if __name__ == "__main__":

    permutations = generate_permutations(
        [0, 1]
    )
    print(
        permutations
    )