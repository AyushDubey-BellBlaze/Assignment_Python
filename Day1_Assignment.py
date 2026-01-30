list = []
n = int(input("Enter number of elements: "))
for i in range(n):
    method = input().split()
    if method[0] == "insert":
        list.insert(int(method[1]), int(method[2]))
    elif method[0] == "print":
        print(list)
    elif method[0] == "remove":
        list.remove(int(method[1]))
    elif method[0] == "append":
        list.append(int(method[1]))
    elif method[0] == "sort":
        list.sort()
    elif method[0] == "pop":
        list.pop()
    elif method[0] == "reverse":
        list.reverse()
    else:
        print("Invalid operation")

print("Final list:", list)

print("Program completed.")