def factorialize(n):
    if n <= 1:
        return 1
    else:
        return n * factorialize(n-1)

print(factorialize(4))


def reverseList(lst):
    if lst: #if list is not empty
        return reverseList(lst[1:])+[lst[0]]
    else:
        return []

test = [4,3,2,1]
# print(reverseList(test))
