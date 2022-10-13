'''nums = {'abi', 'bola', 'ebe', 'ola'}
nums.add('oba')
print(nums)

nums = {1,5,20,60,200,2}
nums.remove(20)
print(nums)
nums1 = {'abi', 'bola', 'ebe', 'ola'}
nums2 = {'abi', 'ade', 'sade', 'ola'}

z = nums1.intersection(nums2)
print(z)

y= nums1.issubset(nums2)
print(y)



#dictoionary function

nums1 = {'abi', 'bola', 'ebe', 'ola'}
nums2 = {'abi', 'ade', 'sade', 'ola'}


students = ['abi', 'bola', 'ebe', 'ola']
marks = [28,39,50,60]
students_dics=dict(zip(students,marks))
print(students_dics)


d = {0:10,1:20}
print(d)
d.update({2:30})
print(d)'''
dic1 ={1:10,2:20}
dic2 ={3:30,4:40}
dic3 ={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)


