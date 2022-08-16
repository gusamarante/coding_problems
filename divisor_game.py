"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.
"""


def divisor_game(n):
    # base cases
    memo = {1: False,
            2: True}

    # recurssive solution
    def dp(k):
        if k not in memo:
            memo[k] = False
            for i in range(1, k):
                if k % i == 0:
                    memo[k] = memo[k] or not dp(k - i)

        return memo[k]

    return dp(n)


for jj in range(1, 1000):
    print(jj, divisor_game(jj))
