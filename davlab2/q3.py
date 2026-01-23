def dictintro():
    n=int(input("How many inputs:"))
    cup={}
    for i in range(n):
        year=int(input("Enter the year: "))
        country=input("Enter the name of the country which won in that year: ")
        cup[year]=country
    print("\n Our dictionary=> ",cup)
    freq={}
    for i in cup.values():
        freq[i]=freq.get(i,0)+1
    best=max(freq, key=freq.get)
    print("Frequency:", freq)
    print("Best Performing Country:", best)
    print("Unique Countries:", set(cup.values()))

dictintro()
    
    