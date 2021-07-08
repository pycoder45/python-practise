#nums = input("Enter The Numbers for Average : ")

def averageof(nums):
  
  nums_ls = nums.split(",")
  make_int = []
  
  for i in nums_ls:
    make_int.append(int(i))
  
  total_sum = 0
  
  for j in make_int: 
    total_sum += j
    
  average = total_sum/len(make_int)
  print(average)

averageof(nums)