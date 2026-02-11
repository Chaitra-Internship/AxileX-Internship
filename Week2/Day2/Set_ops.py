# Program to perform set operations

# Taking input for first set
set1 = set(map(int, input("Enter elements of first set (space separated): ").split()))

# Taking input for second set
set2 = set(map(int, input("Enter elements of second set (space separated): ").split()))

print("\nSet 1:", set1)
print("Set 2:", set2)

# Union
print("\nUnion:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (Set1 - Set2):", set1.difference(set2))
print("Difference (Set2 - Set1):", set2.difference(set1))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))