import string
def list_from_file(filename):
    myfile = open(filename, 'r')
    data = myfile.read().split()
    col = []
    for word in data:
        col.append(word)
    return col

def myhist(col):
    hist = {}
    for word in col:
        word = word.lower()
        word = word.strip(string.punctuation + string.whitespace)
        hist[word] = hist.get(word, 0)+1
    return hist

col = list_from_file('dataforfit1.txt')
colf = myhist(col)
print(colf)
