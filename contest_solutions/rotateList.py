class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # If k > len(nums), we will cycle back to the original list
        # So, lets figure out how many steps we need to take AFTER all the cycling
        k = k % len(nums)
        
        if k == 0:
            # No work to be done
            return
        # if nums = [1,2,3,4,5,6,7], k = 3
        # end = [5,6,7]
        # beg = [1,2,3,4]
        end = nums[-k:]
        beg = nums[:-k]

        # In-place replacement
        nums[:k] = end
        nums[k:] = beg

        
        