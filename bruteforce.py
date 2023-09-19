alphabet="abcdefghijklmnopqrstuvwxyz"
password="test";

def check(value):
    return value == check;

table=[]
def nextLetter(pos):
    if(pos + 1 >= len(table)):
        table[pos] = 0;
        return alphabet[0];
    newIndex=(table[pos] + 1) % 26;
    table[pos] = newIndex;
    return alphabet[newIndex];


def bruteforce(max_length):
    current=""
    for i in range(0, max_length):
        
            check(current);