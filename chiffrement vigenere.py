alphabet="abcdefghijklmnopqrstuvwxyz"

phrase="salutation"
cle="monsupermessage"

def chiffrer(phrase, cle):
    final=""
    for i in range(0, len(phrase)):
        final+=alphabet[(alphabet.index(phrase[i]) + alphabet.index(cle[i])) % 26]
    return final;

def dechiffrer(mot, cle):
    final=""
    for i in range(0, len(mot)):
        final+= alphabet[alphabet.index(mot[i]) % 26 - alphabet.index(cle[i])]
    return final;

chiffrer=chiffrer(phrase, cle);
dechiffrer=dechiffrer(chiffrer, cle)

print(chiffrer)
print(dechiffrer)