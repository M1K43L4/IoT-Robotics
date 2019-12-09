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
        print("is not wave. try again")
        #exit() 


speecht=sr.AudioFile(user_file)
with speecht as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))

print("Enter Keyword: ")

#keyword = "disgusting"
keyword = input()

print("Keyword: " +keyword)

keycount = s.count(keyword)

print("Keycount: " +str(keycount))
