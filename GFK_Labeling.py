"""
Reads a list of reviews and decide if each review is positive or negative,
based on the occurences of positive and negative words.
"""
import operator
import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import load
import os

def processGfk(terms,gfkLex):
    #Determines whether a restaurant is good for kids or not based on certain age related text using text mining
    result=[]
    gfk_count=0
    fourGrams = ngrams(terms,3) #compute 3-grams    
   	 #for each 3gram
    for tg in fourGrams:
        for i in range(0,1):
            if (tg[i] in gfkLex) or (tg[i] in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14'] and tg[i+1] == 'year' and tg[i+2] == 'old'):
                gfk_count=gfk_count+1
    return gfk_count 

def processSentence(terms,ngfkLex,ctr):
    #Determines whether a restaurant is good for kids or not based on certain text eg - nightlife, descrpition, availability of hard drinks etc using text mining
    result=[]
    gfk=1
    #gfk_count=0
    fourGrams = ngrams(terms,3) #compute 2-grams    
   	 #for each 2gram
    for tg in fourGrams:
        for i in range(0,3):
            if tg[i] in  ngfkLex:
                if ctr==1:
                    continue
                elif ctr==2:                
                    print('i am here')
                    gfk=0
                    break
        for i in range(0,2):
            if tg[i] == 'hookah' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'adult' and tg[i+1] == 'entertainment':
                gfk=0
                break
            elif tg[i] == 'bar' and tg[i+1] == 'crawl':
                gfk=0
                break
            elif tg[i] == 'beer' and tg[i+1] == 'bar':
                gfk=0
                break
            elif tg[i] == 'champagne' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'cigar' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'club' and tg[i+1] == 'crawl':
                gfk=0
                break
            elif tg[i] == 'irish' and tg[i+1] == 'pub':
                gfk=0
                break
            elif tg[i] == 'cocktail' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'comedy' and tg[i+1] == 'clubs':
                gfk=0
                break
            elif tg[i] == 'dive' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'gay' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'hookah' and tg[i+1] == 'lounge':
                gfk=0
                break
            elif tg[i] == 'irish' and tg[i+1] == 'pub':
                gfk=0
                break
            elif tg[i] == 'night' and tg[i+1] == 'clubs':
                gfk=0
                break
            elif tg[i] == 'piano' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'sports' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'strip' and tg[i+1] == 'clubs':
                gfk=0
                break
            elif tg[i] == 'striptease' and tg[i+1] == 'dancers':
                gfk=0
                break
            elif tg[i] == 'tiki' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'vermouth' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'whiskey' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'wine' and tg[i+1] == 'bars':
                gfk=0
                break
            elif tg[i] == 'country' and tg[i+1] == 'dance' :
                gfk=0
                break
            elif tg[i] == 'full' and tg[i+1] == 'bar':
                gfk=0
                break
            elif tg[i] == 'thru' and tg[i+1] == 'bars':
                gfk=0
                break
            elif (i<1) and (tg[i] in ['1','2','3','4','5']) and (tg[i+2] == 'am'):
                gfk=0
                break
        if gfk==0:
            break
        result.append(tg)
    return result,gfk

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
        #print(line.strip())
    lex_conn.close()

    return newLex

#function that reads restaurant data and determines whether it's good for kids or not
#The function returns a list of the input reviews and a list of the respective decisions
def run(path,i,c,d):
    decision=0
    ctr=0
    gfk_c=0
    gfk_hold=1
    details=''
    #load the positive and negative lexicons
    ngfkLex=loadLexicon('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/ngfk_words.txt')
    gfkLex=loadLexicon('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/goodforkids.txt')
    
    fin=open(path,encoding = "ISO-8859-1")
    for line in fin: # for every line in the file (1 review per line)
        if not line.strip():
            continue
        else:
            
            ngfkList=[] #list of positive words in the review
            gfkList=[]
            #negList=[] #list of negative words in the review
            
            line=line.lower().strip()  
            line=re.sub('[^a-zA-Z\d]',' ',line)
            line=re.sub(' +',' ',line).strip()
            details=details+line+' '
                    #tokenize the sentence
            terms = nltk.word_tokenize(line) 
            
            gfk_count = processGfk(terms,gfkLex)
            gfk_c=gfk_c+gfk_count
            #print(gfk_c)
            
            #print(terms)
            ctr=ctr+1
            result,gfk= processSentence(terms,ngfkLex,ctr)
            #print(result)
            
            if gfk==0 :
                gfk_hold=0
                #break
            else:
                words=line.split() # slit on the space to get list of words
                #print(words)
                for word in words: #for every word in the review
                    #print(word)    #print(element)
                    if word in ngfkLex: # if the word is in the positive lexicon
                        ngfkList.append(word) #update the positive list for this review
                        #print('i am here')
                        #break
                    else:
                        if word in gfkLex:                           
                            gfkList.append(word)
        
                #decision=0  # 0 for neutral    
                if len(gfkList)>len(ngfkList): # more pos words than neg
                    decision=decision+1 # 1 for positiv
                else:# more neg than pos
                    decision=decision-1 # -1 for negative

    if ((decision > 0) or (gfk_hold==1)):
        decision=1
    else:
        if ( gfk_hold==0 and gfk_c > 3):
            decision=1
        else:
            decision=-1
    
    if decision == 1:            
        f1=open('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/GK_'+str(c)+'/goodforkids_test_'+str(i)+'.txt','w')
        f1.write(details+'\t'+str(decision))
        f1.close()
    elif decision == -1:
        f2=open('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/NGK_'+str(d)+'/notgoodforkids_test_'+str(i)+'.txt','w')
        f2.write(details+'\t'+str(decision))
        f2.close()
    fin.close()
    return decision

if __name__ == "__main__":
    i=0
    a=1
    b=1
    c=0
    d=0
    folders = os.listdir('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/Page Data')
    os.makedirs('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/GK_'+str(c))
    os.makedirs('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/NGK_'+str(d))
    for folder in folders:
        files = os.listdir('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/Page Data'+'/'+folder)  
        for myfile in files:
            i=i+1
            decision=run('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/Page Data'+'/'+folder+'/'+myfile,i,c,d)
            if decision == 1:
                a=a+1
            elif decision == -1:
                b=b+1
                
            if a%30==1 and decision == 1:
                c=c+1
                if not os.path.exists('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/GK_'+str(c)):
                    os.makedirs('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/GK_'+str(c))
            if b%30==1 and decision == -1:
                d=d+1
                if not os.path.exists('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/NGK_'+str(d)):
                    os.makedirs('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/NGK_'+str(d))
   
        
       


        


