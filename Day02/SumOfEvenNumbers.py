nums = [2, 5, 6, 9 , 8 , 14, 3]
evenSum = 0

for i in range(0, len(nums)):
    if(nums[i] % 2 == 0):
        evenSum += nums[i]

print(evenSum)