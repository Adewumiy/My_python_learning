tpl1 = (1,2,3,4) #int tuple
print(tpl1)

tpl2 = (1.2,2.3,3.4,4.5) #float tuple
print(tpl2)

tpl3 = ('1','2','3','4') #string tuple
print(tpl3)

tpl4 = (True,False)#bool tuple
print(tpl4)

tpl5 = (1,'2',3.0,False) #Heterogenous tuple
print(tpl5)

tpl6 =() #empty tuple
print(tpl6)

print(type(tpl6))

tpl7 = 1,2,3,4 #int tuple
print(tpl7)

tpl8 = 1.2,2.3,3.4,4.5 #float tuple
print(tpl8)

tpl9 = '1','2','3','4' #string tuple
print(tpl9)

tpl10 = True, False #boolean tuple
print(tpl10)

tpl11 = 1,'2',3.0,False #heterogenous tuple
print(tpl11)

#INDEXING
print(tpl1[0])#first index using +ve indexing
print(tpl1[-4]) #first indexing using -ve indexing

print(tpl11[3]) #last index using +ve indexing
print(tpl11[1]) #second index using +ve indexing
print(tpl11[-3]) #second index using -ve indexing
#Deleting
del tpl10 #delete tpl10

#Conversion
tpl12 =tuple(["Sabi Programmers"])#convert string to tuple
print(tpl12)

tpl13 =tuple(["Sabi', 'Programmer"])#convert list to tuple
print(tpl13)

tpl14 =tuple({1,2,3,4,5,6})#convert set to tuple
print(tpl13)

tpl15 = tuple({1:"one",2:"two",3:"three"})#convert dict to tuple
print(tpl5)

#operators
print(tpl1+tpl3)#+operator
print(tpl1*4)#*operator
print(tpl2[1:3])#slicing
print(2.4 in tpl3)#in operator
print(2.4 not in tpl3)#not in operator
      

      
      



      
