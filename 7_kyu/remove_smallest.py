def remove_smallest(numbers):
    nums = numbers[:]
    if nums:
        nums.remove(min(nums))
    return nums
