nums = [1, 3, 2, 3]
def min_max(nums):
    nums_tup = []
    if len(nums) > 0:
        mini = nums_tup.append(min(nums))
        maxi = nums_tup.append(max(nums))
        print(tuple(nums_tup))
    else:
        raise ValueError
min_max(nums)