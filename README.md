# DSA

Data Structures and Algorithms (DSA) repository containing implementations of common algorithms and solutions to classic coding problems.

## Overview

This repository serves as a learning resource and reference guide for fundamental data structures and algorithms. It includes various algorithm implementations with explanations and multiple approaches to solving problems.

## Contents

### Two Sum Problem

The repository includes implementations of the **Two Sum** problem, which is a classic array manipulation exercise.

#### Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target. You may assume that each input has exactly one solution, and you cannot use the same element twice.

#### Solutions

##### 1. Brute Force Approach
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** Uses nested loops to check every pair of numbers in the array until finding a pair that sums to the target.

```python
def twosum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

**Pros:** Simple and straightforward logic
**Cons:** Inefficient for large arrays due to quadratic time complexity

---

##### 2. Hash Map Approach
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** Uses a hash map to store previously seen numbers and their indices. For each number, we check if its complement (target - current number) exists in the hash map.

```python
def twosum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in hashmap:
            return [hashmap[num2], i]
        hashmap[num] = i
```

**Pros:** Optimal time complexity, only requires a single pass through the array
**Cons:** Requires additional space for the hash map

---

## Usage

Run the implementations:
```bash
python app.py
```

Example output:
```
[0, 1]  # Indices of elements that sum to 9 in [2, 7, 11, 15]
```

## Learning Goals

- Understand time and space complexity trade-offs
- Learn different algorithmic approaches to solve the same problem
- Practice implementing efficient solutions

# Next target BFS and DFS