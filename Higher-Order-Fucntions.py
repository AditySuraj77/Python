   # map function
#print('Map Function')
"""def table(n):
	return n*n
    
l1 = [2,3,6]

print_table= list(map(table,l1))
print(print_table)"""

"""
l2 = [2,3,4,5]
print(list(map(lambda x:x*x, l2)))"""
 
 
 
 
   # Filter Function
#print('Filter Functions')
'''
def even(n):
	return n%2 == 0

   
lf = [1,2,3,4,5,6,7,8,9,10]
filter_func = list(filter(even,lf))
print(filter_func)'''

'''
lf = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2 == 0, lf))'''

             # Reduce Functions

#print('Reduce Functions')
#from functools import reduce
'''
def add(n,m):
    return n+m

lr = [1,2,3,4,5]  # reducing the number then added
add = reduce(add,lr)
print(add)'''
'''
lr = [1,2,3,4,5]
print(reduce(lambda n,m: n+m, lr))'''