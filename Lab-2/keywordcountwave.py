import speech_recognition as sr
r = sr.Recognizer()

#get user input for filename

fileisgood = False
while fileisgood == False:
    print("Enter filename: ")
    user_file = input()

    try:
        file_object  = open(user_file)
        print("File found")

    except Exception as e:
        print("Exception: " +str(e))

    #only open if is wav file
    print (file_object.name)
    if file_object.name.endswith('.wav'):
         print("is wav")
         fileisgood=True
    else:
        print("is not wav. try again")
        

speecht=sr.AudioFile(user_file)
with speecht as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))





#function for all instances
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

#make list of all words
wordlist = list()
for word in s.split():
    wordlist.append(word)

#print(*wordlist)


#append a newline character at the end
s = s + "\n"

endindex=s.find("\n")
#print("end is at: " + str(endindex))



keywords= list()
# for each word in word list, count the words

for i in wordlist:#iterate through word list
    l =list(find_all(s, i)) #list of indecies
    #print(*l)
    #print("word is: " + i)
    count=0
    index=0
    for j in l:
        #print(str(j))
        #print(s[j])
        if j == 0:
            index= j + len(i)# a space when it is okay
            character = s[index]
            if character == ' ':
                count+=1
                #print("count is: " + str(count))
        else:
            index= j -1
            character = s[index]
            if character == ' ':
                #count+=1
                #print("count is: " + str(count))

                index +=1#undo the minus so index=i
                index+=len(i)
                if index >= endindex:
                    count+=1
                    #print("count is: " + str(count))
                else:
                    character = s[index]
                    if character == ' ': 
                        count+=1
                        #print("count is: " + str(count))

    #print("final count is: " + str(count))
    #if count >= 4, append to keywords list
    if count >=4:
        keywords.append(i)


print("here are your keywords: ")
keywords = list(dict.fromkeys(keywords))
print(keywords)

