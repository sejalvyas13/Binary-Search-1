// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
  
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 1
        if reader.get(0) == target :
            return 0
        while reader.get(right) != (2**31 - 1 ) and reader.get(right) <= target:
            #find the upperbound first
            left = right
            right = right * 2
        #perform binary search
        print(left, right)
        while left <= right :
            mid = (left + right) // 2
            element = reader.get(mid)
            if element == target :
                return mid
            elif element > target :
                right = mid - 1
            else :
                left = mid + 1
        return -1
        
        
        
