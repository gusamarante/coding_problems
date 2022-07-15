"""
LeetCode 746
You are given an integer array cost where cost[i] is the cost of i-th step
on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
"""


# Solution
def climb_costs(costs):
    memo = {}
    costs = costs + [0]

    def dp(i):
        if i == 0:
            return costs[0]

        if i == 1:
            return costs[1]

        if i not in memo:
            memo[i] = min(dp(i - 1), dp(i - 2)) + costs[i]

        return memo[i]

    return dp(len(costs) - 1)


# Testing
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # Output should be 6
print(climb_costs(cost))

cost = [1, 3, 2, 5, 6, 10, 4]  # Output should be 13
print(climb_costs(cost))

cost = [10, 15, 20]  # Output should be 15
print(climb_costs(cost))
