print("\033c")

def symDif(s1,s2):
    return s1.symmetric_difference(s2)


set1 = {'blue', 'green'}
set2 = {'blue', 'yellow'}

set3 = {1, 2, 3, 4, 5}
set4 = {1, 5, 6, 7, 8, 9}


result1 = (symDif(set1,set2))
print(result1)

result2 = (symDif(set3,set4))
print(result2)

