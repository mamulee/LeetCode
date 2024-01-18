class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        rs = [1, 2, 3]
        answer = 0
        for i in range(3, n+1):
            rs.append(rs[i-1] + rs[i-2])
        for i in range(n-1, n):
            if n == 1:
                return 1
            answer += rs[i]
        return answer