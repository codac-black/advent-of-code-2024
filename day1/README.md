<!-- ![A creative and whimsical illustration of a cozy North Pole historian's office with stacks of parchment, ancient maps, and glowing snow globes on wooden shelves](day1/historian_hysteria.png) -->

# Advent of Code 2024 - Day 1: Historian Hysteria

## Problem Overview

### Backstory
The Chief Historian has mysteriously disappeared while exploring historically significant locations. A group of Senior Historians needs help reconciling their lists of location IDs to track down their missing colleague.

### Challenge Objective
Calculate the total distance between two lists of location IDs by pairing and comparing their values.

## Problem Details

### Input
- Two lists of location IDs
- Each list contains numeric identifiers
- Lists are of equal length

### Pairing and Distance Calculation
1. Sort both lists in ascending order
2. Pair up corresponding elements
3. Calculate the absolute difference between paired elements
4. Sum these differences to get the total distance

### Example Walkthrough

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

## Solution Approach

### Key Steps
1. Read input from file
2. Parse input into two separate lists
3. Sort both lists
4. Calculate absolute differences
5. Sum the distances

### Python Implementation Highlights
- Use `sorted()` to order lists
- Use `zip()` to pair elements
- Use `abs()` to calculate distances
- Use `sum()` to total the differences

## Complexity
- Time Complexity: O(n log n) due to sorting
- Space Complexity: O(n) to store the lists

## Potential Challenges
- Handling input file reading
- Ensuring lists are of equal length
- Correctly pairing sorted elements

## Learning Points
- List manipulation
- Sorting algorithms
- Distance calculation techniques
- File input processing

## Conclusion
This challenge tests problem-solving skills, list handling, and basic mathematical operations while presenting a whimsical scenario of helping historians track down their missing colleague.

[Check out the GitHub repository for this project](https://github.com/codac-black/advent-of-code-2024)