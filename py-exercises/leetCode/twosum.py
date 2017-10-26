class Solution():
    def __init__(self):
        """set your shit here"""
        pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        this = True
        while this:
            for i in range(nums):
                for j in range(nums):
                    if nums[i] + nums[j] == target and i != j:
                        print(i, j)
                        this = False
    def main(self):
        print("Hello World")

if __name__ == "__main__":
    main = Solution()
    main.twoSum([1,3,7,5], 10)
