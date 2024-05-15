class Solution:
    def countPrimes(self, n: int) -> int:
        check = []
        c = 0
        for i in range(n):
            if n > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    check.append(i)
        check = set(check)
        # for i in range(len(check)):
        #     if check[i] != 0 and check[i] != 1:
        for i in check:
            if i != 1 and i != 0:
                c = c+1
        return c


a = Solution()
print(a.countPrimes(17))
