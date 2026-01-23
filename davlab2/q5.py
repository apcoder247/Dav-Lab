def setintro():
    set1=set(map(int, input("Enter set 1 elements: ").split()))
    set2=set(map(int, input("Enter set 2 elements: ").split()))
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Union:", set1.union(set2))                      
    print("Intersection:", set1.intersection(set2))         
    print("Difference (Set1 - Set2):", set1.difference(set2))  
    print("Difference (Set2 - Set1):", set2.difference(set1))  

setintro()
