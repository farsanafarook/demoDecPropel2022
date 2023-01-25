#Tuple is unlike  list,its not mutable
#starting with(and ends with)
months=("jan","feb","mar",4)
print(months)
print(months[0])
print(months[-1])

#tuples are immutable eg
#months[0]="text" #result will error,
# no append or replace in tuple
print(len(months))#gives the length of the tuple as integer
print("feb"in months)#check an element---- boolean result
print(months+("apr","may"))#will give result as ('jan', 'feb', 'mar', 4, 'apr', 'may')
print(months)#but still the tuple contain ("jan","feb","mar",4)
day=("sun",)#comma must in in tuples otherwise considred as string
days=("sun","mon","thu","wed")
print(months+day)
print(months+days)
print(months*3)
#del months #deleting the entire tuples
print(months)
# result error,NameError: name 'months' is not defined
