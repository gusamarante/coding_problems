"""
LeetCode 70
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top of n steps?
"""


# Top-Down Solution
def climb_stairs_td(n):
    memo = {}

    def dp(i):
        if i <= 2:
            return i

        if i not in memo:
            memo[i] = dp(i - 1) + dp(i - 2)

        return memo[i]

    return dp(n)


# Bottom-Up solution
def climb_stairs_bu(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)  # creates array of zeros, each entry is the step count of that entry
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Testing - Top-Down
for j in range(1, 11):
    print(f'There are {climb_stairs_td(j)} ways to climb a {j}-step stair')

# Testing - Bottom-Up
for j in range(1, 11):
    print(f'There are {climb_stairs_bu(j)} ways to climb a {j}-step stair')
