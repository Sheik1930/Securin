import part_a
import arraysum
from array import array

def print_orderly(array):
    for i in array:
        print(i)

def calculate_possibilities(curr, free_space, input_values, possibilities, fixed_values, repetition=True):
    if free_space == 0:
        curr = sorted(curr)
        possibilities.add(tuple(curr))
        return possibilities
    
    if repetition:
        for input_value in input_values:
            calculate_possibilities(curr+[input_value], free_space-1, input_values, possibilities, fixed_values, True)
    else:
        for i in range(len(input_values)):
            remaining_input_values = input_values[:i] + input_values[i + 1:]
            calculate_possibilities(curr + [input_values[i]], free_space - 1, remaining_input_values, possibilities, fixed_values, False)
    return possibilities

def transform_dice(die_a, die_b):
    original_probabilities = part_a.calculate_all_probabilities(die_a, die_b)
    
    fixed_values_a = [1, 4]
    input_values_a = [1, 2, 3, 4]
    free_space_a = 4
    possibilities_a = set()
    new_die_a_possibilities = calculate_possibilities(fixed_values_a.copy(), free_space_a, input_values_a, possibilities_a, fixed_values_a, True)
    
    fixed_values_b = [1, 8]
    input_values_b = [2, 3, 4, 5, 6, 7]
    free_space_b = 4
    possibilities_b = set()
    new_die_b_possibilities = calculate_possibilities(fixed_values_b.copy(), free_space_b, input_values_b, possibilities_b, fixed_values_b, False)
    
    for a in new_die_a_possibilities:
        for b in new_die_b_possibilities:
            if (arraysum.sum_of_array(a) + arraysum.sum_of_array(b)) == 42:
                new_sum_possibility = part_a.calculate_all_probabilities(array('i', a), array('i', b))
                if original_probabilities == new_sum_possibility:
                    new_die_a = a
                    new_die_b = b
                    return new_die_a, new_die_b
