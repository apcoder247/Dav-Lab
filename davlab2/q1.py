def listintro():
    l=list(map(int, input("Enter elements separated by a space: ").split()))
    print("The largest element in the list is:",max(l))
    print("The smallest element in the list is:",min(l))
    print("The sum of all the elements in the list is:",sum(l))
    print("The average of all the elements in the list is:",sum(l)/len(l))
    x=int(input("Enter the element whose count has to be calculated: "))
    print(f"The count of the number {x} in the list is {l.count(x)}")

listintro()