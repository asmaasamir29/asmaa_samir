import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
nltk.download("punkt")
file=open("paragraphs.txt")  
my_text=file.read() 

all_stopwords=stopwords.words("english")
words=word_tokenize(my_text)
filtered_w=[word for word in words if word not in all_stopwords]
filtered_words=str(filtered_w)
def printFrequency(filtered):
    M = {}
     
    word = ""
     
    for i in range(len(filtered_words)):
        if (filtered_words[i] == ' '):
             
            if (word not in M):
                M[word] = 1
                word = ""
             
            else:
                M[word] += 1
                word = ""
         
        else:
            word += filtered_words[i]
    if (word not in M):
        M[word] = 1
     
    else:
        M[word] += 1
    for it in M:
        print(it, "-", M[it])
printFrequency(filtered_words)
