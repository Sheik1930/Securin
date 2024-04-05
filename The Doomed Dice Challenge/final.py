import part_a
import part_b

# You are given two six-sided dice, Die A and Die B, each with faces numbered from 1 to 6.
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

length_a = len(die_a)
length_b = len(die_b)

# Part-A
print("Part-A")

# By Formula
print("Total Combinations: ")
combination_count = part_a.calculate_total_combinations(length_a, length_b)
print(combination_count)

# Distribution Display
print("All Possible Distributions: ")
part_a.display_all_combinations(die_a, die_b)

print("Sum Distributions")
part_b.print_orderly(part_a.calculate_sum_distribution(die_a, die_b))

print("Sum Probabilities")
print(part_a.calculate_all_probabilities(die_a, die_b))

# Part-B
print("Part-B")
print("New Dice are")
part_b.print_orderly(part_b.transform_dice(die_a, die_b))
