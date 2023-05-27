class Solution:
    def climbStairs(self, num_stairs: int) -> int:
        if num_stairs == 0 or num_stairs == 1:
            return 1

        return climbStairs(num_stairs - 1) + climbStairs(num_stairs - 2)