def tupleintro():
    t=tuple(map(int, input("Enter 5 elements separated by a space: ").split()))
    print()
    try:
        t[2]=67
    except Exception as e:
        print("Error!!!! - ",e)
        print()
        print("This error occurred due to the fact that tuple is immutable!!!!")
tupleintro()