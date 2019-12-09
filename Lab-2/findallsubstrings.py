sentence="okay Jokay okays"
search="okay"

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

l =list(find_all(sentence, 'okay')) #list of indecies
print(*l)
print(len(l))

word='okay'
count=0
index=0
for i in l:
    if i == 0:
        index = len(word)
        if sentence[index] != "\n" :
            character=sentence[index]
            print(character)
        index-=1
        if sentence[index] != "\n" :
            print(character)
        
