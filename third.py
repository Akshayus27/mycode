i = str(input())
ii = i.upper()
k = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
if(ii in k):
    if(ii == ("A"or"E"or"I"or"O"or"U")):
       print("Vowel")
    else:
       print("Consonant")
else:
    print("Invalid")
