#Justin Mitchell
#2/23/2021

#Problem 4 unique list

def unique(l):

    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x

print(unique([1 , 3, 3, 3, 6, 2, 3, 5]))


#Program prints only the unique numbers out of the given list
