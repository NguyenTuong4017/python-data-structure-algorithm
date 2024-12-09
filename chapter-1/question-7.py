
# Write a function called "custom_encoder" that accepts a string text as parameter 
# and for each char of the text it calculates its 0-based position in the following reference string:



    


def custom_encoder(n):
    n=n.lower()
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positionList = []


    for char in n :
        positionList.append(reference_string.find(char))
    
    return positionList

print(custom_encoder("hello"))