'''There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).'''

testcase_1 = [-1,-2,-3,-4,3,2,1]
testcase_2 = [1,5,0,2,-3]
testcase_3 = [-1,1,-1,1,-1]
              
class Solution:
    def arraySign( nums: list[int]) -> int:
        product = 1
        for num in nums.copy():
            product *= num
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        
    def noProd(nums: list[int]) -> int:
        product = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                product *= -1
        return product
      

print(Solution.arraySign(testcase_1))
print(Solution.arraySign(testcase_2))
print(Solution.arraySign(testcase_3))
print('orrrrrrrr')
print(Solution.noProd(testcase_1))
print(Solution.noProd(testcase_2))
print(Solution.noProd(testcase_3))