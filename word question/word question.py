from random import randint
import sys , re
# #open and read the file after the appending:

def append_without_repeated(words):
    f=open("saved.txt","r")
    file_words=f.read()
    list_new=[]
    if "," in words:
        words=words.split(",")
        for i in words:
            if i in file_words:
                words.replace(i,"")
    else:
        if words in file_words:
            return file_words
    f1=open("saved.txt","a")
    f1.write(","+words)
    f1=open("saved.txt","r")
    a=f1.read()
    f.close()
    f1.close()
    return a

# print(f.read())

words=input("Enter your words to form (word:answare) and put a comma between this word and another word:")


a=re.search("^([a-zA-Z]* *[a-zA-Z]*)*:([a-zA-Z]* *[a-zA-Z]*)*",words)
if not a and words!="":
    print("False")
    sys.exit()

words=append_without_repeated(words)

List_word=words.split(",")
Quiz=[]
Answare=[]
for i in List_word:
    q,a=i.split(":")
    Quiz.append(q)
    Answare.append(a)

number_random=randint(0,len(List_word)-1)
true=0
rep=0
count_quiz=0
t=True
while t:
    user_ans=input(f"What does {Quiz[number_random]} mean ?")
    if user_ans=="exit":
        rabete=count_quiz/true
        score=20/rabete
        print(f"Number of questions : {count_quiz}\nNumber of True : {true}\nScore : {score}")
        sys.exit()
    elif user_ans == Answare[number_random]:
        if rep==0:
            true+=1
        print("True")
        number_random=randint(0,len(List_word)-1)
        count_quiz+=1
        rep=0
    else:
        print("False")
        rep+=1

