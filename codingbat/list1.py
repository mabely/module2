##############################

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True

  else:
    return False

##############################
    
def common_end(a, b):
  if a[0] == b[0]:
    return True
  
  elif a[-1] == b[-1]:
    return True
    
  else:
    return False

##############################

def sum3(nums):
  if len(nums) == 3:
    return sum(nums)
  else:
    return False

##############################





