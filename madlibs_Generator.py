with open("paragraph.txt","r") as f :
    story=f.read()
    
words=set()
first_word=-1

target_start="["
target_end="]"

for i,char in enumerate(story):
     if char==target_start:
         first_word=i
         
     if char == target_end and first_word!=-1:
         word=story[first_word:i+1]
         words.add(word)
         first_word=-1
         
words_meaning={}

for word in words :
    meaning=input('Give the meaning for the following word '+word+" : ")
    words_meaning[word]=meaning
    
for word in words:
    story=story.replace(word,words_meaning[word])
    
print(story)
         
         