class Solution:

    """ Constructor definition """
    def __init__(self):
        self.bound = 600

    """ Function definition """
    @staticmethod
    def triangular(index: int) -> int:
        return index * (index + 1) // 2

    def triangle_list(self, bound: int) -> list:
        return [self.triangular(k) for k in range(1, bound)]

    def solve(self):

        triangleList = self.triangle_list(self.bound)

        print()
        print(triangleList)

if __name__ == "__main__":

    solution = Solution()
    solution.solve()
