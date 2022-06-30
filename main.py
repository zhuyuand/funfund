# -*-coding:utf-8-*-
import bisect


def bisect_left(nums, target, left=0, right=None):
    if left < 0:
        raise ValueError('lo must be non-negative')
    if right is None:
        right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def right_bound(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid + 1
    return left


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(bisect_left(nums, target))
print(right_bound(nums, target))
