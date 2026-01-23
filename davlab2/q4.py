def word_frequency():
    sentence = input("Enter a sentence: ")
    words = sentence.split()     
    freq = {}                    
    for w in words:
        if w in freq:
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1
    
    print("Word Frequency Dictionary:", freq)

word_frequency()
