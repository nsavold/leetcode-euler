class Solution: '''https://leetcode.com/problems/find-the-difference-of-two-arrays/solutions/?languageTags=python3'''
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list3, list4 = [], []
        for element in nums1:
            if element not in nums2 and element not in list3:
                list3.append(element)
        for element in nums2:
            if element not in nums1 and element not in list4:
                list4.append(element)
        return [list3, list4]
    
    #in one line
        return [list(set(nums1).difference(nums2)), list(set(nums2).difference(nums1))]
    #python has set opporations
    #sets arent supposed to have duplicate elements. Since we want to return DISTINCT elements
    #putting dplicated in the set will erase them.
    #so we pass the list to a set, run set().difference(), then pass the set BACK to a list
    #neat!
    #the above is my solution. very slow.
    #you could probably use set comprehension but its not necessary (you can solve in one line lmao)