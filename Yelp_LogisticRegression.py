from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import os
from sklearn.metrics import accuracy_score

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

rev_train,labels_train=loadData('C:/Desktop/Academics/First Sem/Web Mining/Project/Working Code/Trial Code/Data Cleansing and Labeling/Labeled Data/Labels_Data/Testing Data')
rev_test,labels_test=loadData('C:/Desktop/Academics/First Sem/Web Mining/Project/Working Code/Trial Code/Data Cleansing and Labeling/Labeled Data/Labels_Data/Training Data')

counter = CountVectorizer()
counter.fit(rev_train)
counts_train = counter.fit_transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data
#clf= LogisticRegression() #this gives the best accuracy
#clf= MultinomialNB()
clf= DecisionTreeClassifier()
clf.fit(counts_train,labels_train)
pred=clf.predict(counts_test)
print (accuracy_score(pred,labels_test))




