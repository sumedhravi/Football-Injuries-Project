from joblib import dump, load
from numpy.core.defchararray import islower
import pandas as pd
import numpy as np
import os

y_cols = ['foot', 'lower_leg', 'upper_leg', 'upper_body', 'arms', 'head', 'minor', 'injury']

def save_classifier(clf, filepath):
    dump(clf, filepath)
    
def load_classifier(filepath):
    clf = load(filepath)
    return clf

def load_label_classifier(filepath, label):
    full_path = os.path.join(filepath, label + ".joblib")
    return load(full_path)

# a method we can call that will use the dictionary structure above and output probabilities
def classifier_predict(clf, x_data):
    return clf.predict_proba(x_data)[:,1]

# only predicts one label, useful for tabpy
# x_data should be one row
def classifier_predict_field(clf, field, x_data):
    x_data = x_data.reshape((1,-1))
    label_classifier = clf[field]
    pred = label_classifier.predict_proba(x_data)
    print(pred)
    return pred[0,1] 

def format_data(age, height, weight, position, isArms, isFootAnkle, isHead, isLowerLeg, isUpperBody, isUpperLeg):
    data = np.zeros((22,))
    data[0] = age
    data[1] = height
    data[2] = weight
    d = {
        'Cewntre-Back': 3,
        'Right Winger': 4,
        'Left Winger': 5, 
        'Goalkeeper': 6, 
        'Central Midfield': 7, 
        'Right-Back': 8, 
        'Left-Back': 9, 
        'Defensive Midfield': 10, 
        'Centre-Forward': 11, 
        'Attacking Midfield': 12, 
        'Left Midfield': 13, 
        'Right Midfield': 14, 
        'Second Striker': 15
    }
    data[d[position]] = 1
    data[16] = isArms
    data[17] = isFootAnkle
    data[18] = isHead
    data[19] = isLowerLeg
    data[20] = isUpperBody
    data[21] = isUpperLeg
    return data

if __name__ == "__main__":
    x_data = np.array([ 28., 169.,  63.,   0.,   0.,   1.,   0.,   0.,  0.,   0.,   0.,   0.,   0.,   0.,  0.,   0.,  0.,  0.,   0.,   0.,   1.,   0.])
    print(x_data.dtype)
    clf = load_classifier("../models/numbered_history_lr.joblib")
    res = classifier_predict_field(clf, 'foot', x_data)
    print(res)
    print(classifier_predict(clf, x_data.reshape((1,-1))))