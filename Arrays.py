print("\033c")

import array as arr 

array_num = arr.array('i' , [1, 3, 5, 3, 7, 9, 3, 3, 3])

print("Original array:" , array_num)

print("Number of occurrences of the number 3 is the said array", array_num.count(3))

array_num.reverse()
print(array_num)