def binary_search(nums, left, right, target):

    #base case search space exhausted
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if target == nums[mid]:
        return mid
    
    #target less than mid - discard right
    if target < nums[mid]:
        return binary_search(nums, left, mid-1, target)
    
    #target greater than mid - discard left
    if target > nums[mid]:
        return binary_search(nums, mid+1, right, target)

if __name__ == "__main__":

    nums = [2,3,4,5,6,7,8,9]
    target = 5

    (left, right) = (0, len(nums)-1)
    index = binary_search(nums, left, right, target)

    if index != -1:
        print("Target found at index ", index )
    else:
        print("Target not found in list")

# O(log2n) time complexity & O(1) space complexity