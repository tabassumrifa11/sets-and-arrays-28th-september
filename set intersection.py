print("\033c")

setx = {"green", "blue"}
sety = {"yellow", "blue"}

print("Original set elements:")
print(setx)
print(sety)

print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

print("\nUnion of two said sets:")
setz = setx.union(sety)
print(setz)

print("\nDifference of two said sets:")
setz = setx.difference(sety)
print(setz)

print("\nSymmetric Difference of two said sets:")
setz = setx.symmetric_difference(sety)
print(setz)