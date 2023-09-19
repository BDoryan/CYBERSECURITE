alphabet="abcdefghijklmnopqrstuvwxyz"

phrase_chiffrer=""

def chiffrementCesar(phrase, distance):
    final=""
    for letter in phrase:
        if letter not in alphabet: 
            final += letter;
            continue;
        position=ord(letter)
        final += chr((position + distance))
    return final;

def dechiffrementCesar(phrase, distance):
    final=""
    for letter in phrase:
        if letter not in alphabet: 
            final += letter;
            continue;
        position=ord(letter)
        final += chr(position - distance)
    return final;

def trueOrFalseValue(value, trueValue, falseValue):
    if(value):
        return trueValue
    else:
        return falseValue 

phrase = input('Qu\'est-ce que vous voulez chiffrer ?\n')
chiffrer=chiffrementCesar(phrase, 7);
print(chiffrer);
print(dechiffrementCesar(chiffrer, 7));
print("Test unitaire, est-ce que le chiffre et le déchiffrement se passe correctement")
print("  * Chiffrement : ", trueOrFalseValue(chiffrer != phrase,  "SUCCES", "ECHEC"))
print("  * Déchiffrement : ", trueOrFalseValue(phrase == dechiffrementCesar(chiffrer, 7), "SUCCES", "ECHEC"))