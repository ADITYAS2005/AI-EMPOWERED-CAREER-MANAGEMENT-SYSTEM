#Importing Libraries
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree, svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

import pickle


#Loading Dataset
df = pd.read_csv(r"C:\Users\adity\Downloads\CareerPredictionModel-main\CareerPredictionModel-main\Career-Prediction-System-main\Career-Prediction-System-main2\data\\\mldata.csv")


# Number Encoding
cols = df[["self-learning capability?", "Extra-courses did","Taken inputs from seniors or elders", "worked in teams ever?", "Introvert"]]
for i in cols:
    cleanup_nums = {i: {"yes": 1, "no": 0}}
    df = df.replace(cleanup_nums)
   

mycol = df[["reading and writing skills", "memory capability score"]]
for i in mycol:
    cleanup_nums = {i: {"poor": 0, "medium": 1, "excellent": 2}}
    df = df.replace(cleanup_nums)


# Label Encoding
category_cols = df[['certifications', 'workshops', 'Interested subjects', 'interested career area ', 'Type of company want to settle in?', 
                    'Interested Type of Books']]
for i in category_cols:
    df[i] = df[i].astype('category')
    df[i + "_code"] = df[i].cat.codes


# Dummy Variable Encoding
df = pd.get_dummies(df, columns=["Management or Technical", "hard/smart worker"], prefix=["A", "B"])


# Building Model
feed = df[['Logical quotient rating', 'coding skills rating', 'hackathons', 'public speaking points', 'self-learning capability?','Extra-courses did', 
           'Taken inputs from seniors or elders', 'worked in teams ever?', 'Introvert', 'reading and writing skills', 'memory capability score',  
           'B_hard worker', 'B_smart worker', 'A_Management', 'A_Technical', 'Interested subjects_code', 'Interested Type of Books_code', 'certifications_code', 
           'workshops_code', 'Type of company want to settle in?_code',  'interested career area _code',
             'Suggested Job Role']]


# Taking all independent variable columns
df_train_x = feed.drop('Suggested Job Role',axis = 1)

# Target variable column
df_train_y = feed['Suggested Job Role']

# Train-Test Splitting
x_train, x_test, y_train, y_test = train_test_split(df_train_x, df_train_y, test_size=0.20, random_state=42)


# Decision Tree Classifier
clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(x_train, y_train)

# SVM Classifier
clf2 = svm.SVC()
clf2 = clf2.fit(x_train, y_train)


#Random Forest Classifier
clf3 = RandomForestClassifier(n_estimators=100) 
clf3 = clf3.fit(x_train, y_train)

#XGBoost Classifier



# feed = df[['Logical quotient rating', 'coding skills rating', 'hackathons', 'public speaking points', 'self-learning capability?','Extra-courses did', 
#            'Taken inputs from seniors or elders', 'worked in teams ever?', 'Introvert', 'reading and writing skills', 'memory capability score',  
#            'B_hard worker', 'B_smart worker', 'A_Management', 'A_Technical', 'Interested subjects_code', 'Interested Type of Books_code', 'certifications_code', 
#            'workshops_code', 'Type of company want to settle in?_code',  'interested career area _code',
#              'Suggested Job Role']]


# Decision Tree Model
file1 = open('weights.pkl', 'wb') 
pickle.dump(clf1, file1)
file1.close()

# # # SVM Model
# # file2 = open('pkl/model2.pkl', 'wb') 
# # pickle.dump(clf2, file2)
# # file2.close()

# # Random Forest Model
# file3 = open('weights.pkl', 'wb') 
# pickle.dump(clf3, file3)
# file3.close()




print("All Model Building Done!")


