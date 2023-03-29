class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        selected_indx = []
        for i in range(len(nums)):
            exemple = nums.copy()
            for n in range(len(exemple)):
                if n == i:
                    exemple[n] = 0
                elif nums[i]+exemple[n] == target:
                    selected_indx.append(i)
                    selected_indx.append(n)
                else:
                    pass

        mylist = list(dict.fromkeys(selected_indx))
        return mylist