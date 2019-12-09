sentence="okay okay okays"
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


sentence+="\n"
word='okay'
count=0
index=0
endindex=sentence.find("\n")
print("end is at: " + str(endindex))

for i in l:
    print(str(i))
    print(sentence[i])
    if i == 0:
        index= i + len(word)# a space when it is okay
        character = sentence[index]
        if character == ' ':
            count+=1
            print("count is: " + str(count))
    else:
        index= i -1
        character = sentence[index]
        if character == ' ':
            #count+=1
            #print("count is: " + str(count))

            index +=1#undo the minus so index=i
            index+=len(word)
            if index >= endindex:
                count+=1
                print("count is: " + str(count))
            else:
                character = sentence[index]
                if character == ' ': 
                    count+=1
                    print("count is: " + str(count))

print("final count is: " + str(count))
