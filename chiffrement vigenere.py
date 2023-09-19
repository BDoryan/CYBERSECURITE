alphabet="abcdefghijklmnopqrstuvwxyz"

phrase="salutation"
cle="monsupermessage"

def chiffrer(phrase, cle):
    final=""
    for i in range(0, len(phrase)):
        index=alphabet.index(phrase[i]);
        indexCle=alphabet.index(cle[i]);
        decalage=(index + indexCle) % 26;
        final+=alphabet[(index + indexCle) % 26]
    return final;

def dechiffrer(mot, cle):
    final=""
    for i in range(0, len(mot)):
        index=alphabet.index(mot[i]);
        indexCle=alphabet.index(cle[i]);
        decalage=(index - indexCle) % 26;
        final+= alphabet[index % 26 - indexCle]
    return final;

chiffrer=chiffrer(phrase, cle);
dechiffrer=dechiffrer(chiffrer, cle)

print(chiffrer)
print(dechiffrer)