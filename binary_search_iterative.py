def binary_search(nums, target):

    # define start and end index
    (left, right) = (0, len(nums) - 1)

    # loop until search space exhausted
    while left < right:

        # get mid index
        mid = (left + right) // 2

        # target found
        if target == nums[mid]:
            return mid
        
        #target is less than mid so remove right side of array
        # including mid element
        elif target < nums[mid]:
            right = mid - 1
        
        #target is greater than mis so remove left and mid element
        else:
            left = mid + 1
    
    #There is no match for target
    return -1

if __name__ == "__main__":

    nums = [2,3,4,6,8,9,10]
    target = 5

    index = binary_search(nums, target)

    if index != -1:
        print("Target found at index", index)
    else:
        print("Target not found in the list")