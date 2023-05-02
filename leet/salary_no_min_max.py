class Solution:  #https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
    def average(self, salary: List[int]) -> float:
        min = 1000001 #our biggest will be 1m
        max = 999  #smallest 1000
        sum = 0
        for pay in salary:
            if pay < min:
                min = pay
            if pay > max:   #why did this fail as an elif?
                max = pay
            sum += pay
        return float((sum-min-max) / (len(salary)-2))