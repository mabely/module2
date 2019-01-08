#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############################

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

##############################
  
def big_diff(nums):
  return max(nums) - min(nums)

##############################
  
def centered_average(nums):
  nums.remove(max(nums))
  nums.remove(min(nums))
  return sum(nums)/len(nums)

##############################
  


