# 1. Total combinations calculation
def calculate_total_combinations(length_a, length_b):
    total_combinations = length_a * length_b
    return total_combinations

# 2. Displaying all possible combinations
def display_all_combinations(die_a, die_b):
    combinations_array = [[0 for _ in range(len(die_b))] for _ in range(len(die_a))]
    for a in range(len(die_a)):
        for b in range(len(die_b)):
            combinations_array[a][b] = (die_a[a], die_b[b])
    for i in combinations_array:
        print(i)
    return combinations_array

# 3. Calculating sum distribution
def calculate_sum_distribution(die_a, die_b):
    sum_array = [[0 for _ in range(len(die_b))] for _ in range(len(die_a))]
    for a in range(len(die_a)):
        for b in range(len(die_b)):
            sum_array[a][b] = die_a[a] + die_b[b]
    return sum_array

# 4. Calculating probabilities of all possible sums
def calculate_single_probability(die_a, die_b, sum_value):
    sum_distribution_array = calculate_sum_distribution(die_a, die_b)
    count = 0
    for rows in sum_distribution_array:
        for column in rows:
            if column == sum_value:
                count += 1
    probability = count / (len(die_a) * len(die_b))
    return round(probability, 4)

def calculate_all_probabilities(die_a, die_b):
    probability_dict = {
        "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
        "8": 0, "9": 0, "10": 0, "11": 0, "12": 0
    }
    for i in range(2, 13):
        probability_dict[str(i)] = calculate_single_probability(die_a, die_b, i)
    return probability_dict
