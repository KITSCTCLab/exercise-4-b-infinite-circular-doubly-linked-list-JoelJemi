from collections import Counter
# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
Unique=Counter(circular_linked_list)
print(len(Unique))
print(*Unique)
Footer
© 2022 GitHub, Inc.
