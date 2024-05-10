nums=[1,2,3,4,5,6,7,8,9,10]

# filter(function, list)
# def even(num):
#     return (num%2) ==0
    
# evenNum = list(filter( even,nums))
# print(evenNum)

# nums =[num for num in nums if(num%2) ==0]

# print(nums)

# evenNum = []

# for num in nums:
#     if (num % 2) == 0:
#         evenNum.append(num)

# print(evenNum)

evenNums = list(filter(lambda num: (num%2)==0,nums))
print(evenNums)