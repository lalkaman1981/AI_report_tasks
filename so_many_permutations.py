from itertools import permutations

def permutations_no_duplicates(string):
    """
    This function generates all permutations of a string, removing duplicates and converting to strings.

    Args:
        string: The input string.

    Returns:
        A list containing all unique permutations of the input string.
    """
    if len(string) == 0:
        return [""]
    permutations_set = set()
    for perm in permutations(string):
        # Join characters in the permutation to form a string
        permutations_set.add(''.join(perm))
    return list(permutations_set)

# Example usage
string = "abc"
permutations_of_string = permutations_no_duplicates(string)
print(permutations_of_string)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

string = "ab"
permutations_of_string = permutations_no_duplicates(string)
print(permutations_of_string)  # Output: ['ab', 'ba']

string = "aabb"
permutations_of_string = permutations_no_duplicates(string)
print(permutations_of_string)  # Output: ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']