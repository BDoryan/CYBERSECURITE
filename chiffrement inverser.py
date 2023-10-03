def encode(value):
    return value[::-1]

def decode(value):
    return value[::-1]

word=input("Chiffrement par renversement : ")
chiffrer=encode(word);
print("Chiffrement :", chiffrer);
print("Déchiffrement :", decode(chiffrer));
