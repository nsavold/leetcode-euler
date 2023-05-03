setmessing = {1,2,3,3,5}
listtosettolist = [x for x in range(1,11)]
listtosettolist.append(5)
# a list with a dupe
print('as list:')
print(listtosettolist)
#pass the list to a set, then print set
print('as set')
setversion = set(listtosettolist)
print(setversion)
listof = list(setversion)
print('as list:')
print(listof)
#we pas a list with a dupe to a set, whihc removes the dupe, 
#then passes it back, which preserves the dupe removal