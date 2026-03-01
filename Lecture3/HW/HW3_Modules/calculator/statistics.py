def mean(nums):
  return sum(nums)/len(nums)


def median(nums):
  nums.sort()
  n = len(nums)
  mid = n // 2
  if (n % 2 == 0):
    return (nums[mid - 1] + nums[mid]) / 2
  else:
    return nums[(n+1)//2]