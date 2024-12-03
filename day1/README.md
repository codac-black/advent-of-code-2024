# Advent of Code 2024 - Day 1: Historian Hysteria

## Problem Overview

### Backstory
The Chief Historian has mysteriously disappeared while exploring historically significant locations. A group of Senior Historians needs help reconciling their lists of location IDs to track down their missing colleague.

### Challenge Objective
The challenge is split into two parts:
1. Calculate the total distance between two lists of location IDs
2. Compute a similarity score between the two lists

## Part One: List Distance Calculation

### Problem Details
- Input: Two lists of location IDs
- Task: Calculate the total distance between lists

### Pairing and Distance Calculation
1. Sort both lists in ascending order
2. Pair up corresponding elements
3. Calculate the absolute difference between paired elements
4. Sum these differences to get the total distance

#### Example Walkthrough
**Sample Input:**
- Left List: `[3, 4, 2, 1, 3, 3]`
- Right List: `[4, 3, 5, 3, 9, 3]`

**Sorting the Lists:**
- Left List (sorted): `[1, 2, 3, 3, 3, 4]`
- Right List (sorted): `[3, 3, 3, 4, 5, 9]`

**Pairing and Distance Calculation:**
1. 1 and 3: Distance = |1 - 3| = 2
2. 2 and 3: Distance = |2 - 3| = 1
3. 3 and 3: Distance = |3 - 3| = 0
4. 3 and 4: Distance = |3 - 4| = 1
5. 3 and 5: Distance = |3 - 5| = 2
6. 4 and 9: Distance = |4 - 9| = 5

**Total Distance:** 2 + 1 + 0 + 1 + 2 + 5 = 11

## Part Two: Similarity Score Calculation

### Problem Details
- Input: Two lists of location IDs
- Task: Calculate a similarity score by counting number occurrences

### Similarity Score Calculation
1. Count the frequency of each number in the right list
2. For each number in the left list:
   - Multiply the number by its frequency in the right list
3. Sum these products to get the total similarity score

#### Example Walkthrough
**Sample Input:**
- Left List: `[3, 4, 2, 1, 3, 3]`
- Right List: `[4, 3, 5, 3, 9, 3]`

**Calculation Steps:**
1. 3 appears 3 times → 3 * 3 = 9
2. 4 appears 1 time → 4 * 1 = 4
3. 2 appears 0 times → 2 * 0 = 0
4. 1 appears 0 times → 1 * 0 = 0
5. 3 appears 3 times → 3 * 3 = 9
6. 3 appears 3 times → 3 * 3 = 9

**Total Similarity Score:** 9 + 4 + 0 + 0 + 9 + 9 = 31

## Solution Approach

### Key Python Techniques
- `sorted()` for list ordering
- `zip()` for element pairing
- `abs()` for distance calculation
- `collections.Counter()` for frequency counting

### Computational Complexity
- Time Complexity: O(n log n) due to sorting
- Space Complexity: O(n) to store lists and frequencies

## Implementation Highlights
```python
def calculate_total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    return sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))

def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)
    return sum(num * right_count[num] for num in left_list)
```

## Potential Challenges
- Handling input file reading
- Ensuring lists are of equal length
- Correctly pairing and calculating distances
- Understanding frequency-based scoring

## Learning Points
- List manipulation techniques
- Sorting algorithms
- Frequency counting
- Pythonic data processing methods

## Conclusion
This challenge tests problem-solving skills, list handling, and mathematical operations while presenting a whimsical scenario of helping historians track down their missing colleague through creative list analysis.

## Puzzle Results
- Part One Total Distance: 2,031,679
- Part Two Similarity Score: *Solution Omitted*

For the full implementation visit the [github repo](https://github.com/codac-black/advent-of-code-2024)
