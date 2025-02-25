class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lid = 0
        rid = len(numbers) - 1

        while lid < rid:
            if numbers[lid] + numbers[rid] == target:
                return [lid+1, rid+1]
            elif numbers[lid] + numbers[rid] > target:
                rid -= 1
            else:
                lid += 1
        
        return 0
        