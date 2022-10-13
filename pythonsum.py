'''nums = [1,5,20,60,200,2]
sumTotal =0
for num in nums:
    sumTotal += num
print(sumTotal)

nums = [1,5,20,60,200,2]
mulTotal =1
for num in nums:
    mulTotal *= num
print(mulTotal)


nums = [1,5,20,60,200,2]
largest =0
for num in nums:
    if num > largest:
        largest = num
print(largest)

nums = [1,5,20,60,200,2]
smallest = max(nums)
for num in nums:
    if num < smallest:
        smallest = num
print(smallest)
'''

str_list = ['abc', 'xyz', 'aba', '1221']
count=0
for i in str_list:
    if len(i)>=2:
        if i[0]==i[-1]:
            count +=1

print(count)

            
            
