"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os


#read the reviews and their polarities from a given file
def loadData(folders):
    reviews=[]
    labels=[]
    for folder in os.listdir(folders):
        files=os.listdir(folders+'/'+folder)
        for myfile in files:
            f=open(folders+'/'+folder+'/'+myfile)
            review,rating=f.read().split('\t')  
            reviews.append(review.lower())    
            labels.append(int(rating))
            f.close()
    return reviews,labels

rev_train,labels_train=loadData('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/Testing Data')
rev_test,labels_test=loadData('C:/Desktop/Academics/First Sem/Web Mining/Project/Final Project/Training Data')


#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#train classifier
clf = MultinomialNB()

#train all classifier on the same datasets
clf.fit(counts_train,labels_train)

#use hard voting to predict (majority voting)
pred=clf.predict(counts_test)

#print accuracy
print (accuracy_score(pred,labels_test))


