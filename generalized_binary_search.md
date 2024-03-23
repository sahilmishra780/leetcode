*[Reference](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)*

Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascending order. For most tasks, we can transform the requirement into the following generalized form:
Minimize k , s.t. condition(k) is True

The following code is the most generalized binary search template:

```
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

```

What's really nice of this template is that, for most of the binary search problems, we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

-   Correctly initialize the boundary variables `left` and `right` to specify search space. Only one rule: set up the boundary to include all possible elements;
-   Decide return value. Is it `return left` or `return left - 1`? Remember this: after exiting the while loop, `left` is the minimal k​ satisfying the `condition`function;
-   Design the `condition` function. This is the most difficult and most beautiful part. Needs lots of practice.

Below I'll show you guys how to apply this powerful template to many LeetCode problems.

* * * * *
Basic Application
====================

[278\. First Bad Version [Easy]](https://leetcode.com/problems/first-bad-version/)
----------------------------------------------------------------------------------

You are a product manager and currently leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API `bool isBadVersion(version)` which will return whether `version` is bad.

Example:

```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.

```

First, we initialize `left = 1` and `right = n` to include all possible values. Then we notice that we don't even need to design the `condition` function. It's already given by the `isBadVersion` API. Finding the first bad version is equivalent to finding the minimal k satisfying `isBadVersion(k) is True`. Our template can fit in very nicely:

```
class Solution:
    def firstBadVersion(self, n) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

```

* * * * *

[69\. Sqrt(x) [Easy]](https://leetcode.com/problems/sqrtx/)
-----------------------------------------------------------

Implement `int sqrt(int x)`. Compute and return the square root of *x*, where *x* is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example:

```
Input: 4
Output: 2

```

```
Input: 8
Output: 2

```

Easy one. First we need to search for minimal k satisfying condition `k^2 > x`, then `k - 1` is the answer to the question. We can easily come up with the solution. Notice that I set `right = x + 1` instead of `right = x` to deal with special input cases like `x = 0` and `x = 1`.

```
def mySqrt(x: int) -> int:
    left, right = 0, x + 1
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1  # `left` is the minimum k value, `k - 1` is the answer

```

* * * * *

[35\. Search Insert Position [Easy]](https://leetcode.com/problems/search-insert-position/)
-------------------------------------------------------------------------------------------

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

Example:

```
Input: [1,3,5,6], 5
Output: 2

```

```
Input: [1,3,5,6], 2
Output: 1

```

Very classic application of binary search. We are looking for the minimal k value satisfying `nums[k] >= target`, and we can just copy-paste our template. Notice that our solution is correct regardless of whether the input array `nums` has duplicates. Also notice that the input  `target` might be larger than all elements in `nums` and therefore needs to placed at the end of the array. That's why we should initialize `right = len(nums)` instead of `right = len(nums) - 1`.

```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

```

* * * * *