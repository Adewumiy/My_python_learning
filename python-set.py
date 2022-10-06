set1 ={1,2,3,4} #int set
print(set1)

set2 ={1.2,2.0,3.0} #float set
print(set2)

set3 = {'1','2','3','4'} #string set
print(set3)

set4 ={True,False,True,False} #bool set
print(set4)

set5={1,2.1,'3',True} #heterogenous set
print(set5)

set6 =set() #emptyset
print(set6)

print(type(set6))

set7 = {12,57,43,1,2.4,"greet"} #set of hashbol
print(set7)

#Conversion
set8=set('Sabi Programmers') #convert string to
print(set8)

set9 =set(['Sabi','Programmers']) #convert list
print(set9)

set10 = set(('Sabi','Programmers')) #convert tuple
print(set10)

set11 =set({1:'Sabi',2 : 'Programmers'}) #convert
print(set11)

#modifying a set
set12 =set()
set12.add(20)
set12.add('christiana')
set12.add(True)
set12.add(40.123)
#Update function
set13={'Vera','Alex',"Sola",'Wumi'}
set12.update(set13)
print('set13:',set13)
print('set 12 after updating:',set12)
#or operator
set14 ={1,2,3,4,5}
set15 ={4,5,6,7,8}
#print(set14  set15, "Using ")
print(set14 or set15, "Using or")

#and operator
print(set14 & set15, "Using &")
print(set14 and set15, "Using and")

#-operator
print(set14 - set15, "Using set14- set15")
print(set15 -set14, "Using set15 -set14")

# operator
#print(set13 set15,"Using ")

#union method
print(set14.union(set15), "Using union")

#intersection
print(set14.intersection(set15), "Using intersection")

#difference
print(set14.difference(set15), "Using set14.difference")
print(set15.difference (set14),"using set15.difference")

#symmetric difference
print(set14.symmetric_difference(set15), "Using systemic difference")

#copy method
set16 = set3.copy()
print


#difference update
set14 ={1,2,3,4,5}
set15 ={4,5,6,7,8}
print('set14 before difference update: ',set14)
print('set15 before difference update: ',set15)
set14.difference_update(set15)
print('set14 after difference update: ',set14)
print('set15 after difference update: ',set15)


#intersection update
set14 ={1,2,3,4,5}
set15 ={4,5,6,7,8}
print('set14 before intersection update: ',set14)
print('set15 before intersection update: ',set15)
set15.intersection_update(set15)
print('set14 after intersection update: ',set14)
print('set15 after intersection update: ',set15)


#symmetric_difference update
set14 ={1,2,3,4,5}
set15 ={4,5,6,7,8}
print('set14 before symmetric_difference update: ',set14)
print('set15 beforesymmetric_difference update: ',set15)
set15.intersection_update(set15)
print('set14 after symmetric_difference update: ',set14)
print('set15 after symmetric_difference update: ',set15)

#discard method
print(set14.discard(4))

#remove method
print(set15.remove(6))

#issubset method
set17 ={1,2}
print(set17.issubset(set14))

#isdisjoint method
set18 ={20,30}
print(set18.isdisjoint(set14))

#pop method
print('popped value: ',set16.pop())
print('new set16: ', set16)



print(set17.issubset(set14))













      
      


               
                     
                     
               
