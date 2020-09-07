import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

"""
dataset = pd.read_csv('sales.csv')

dataset['rate'].fillna(0, inplace=True)

dataset['sales_in_first_month'].fillna(dataset['sales_in_first_month'].mean(), inplace=True)

X = dataset.iloc[:, :3]

def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

X['rate'] = X['rate'].apply(lambda x : convert_to_int(x))

y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, y)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[4, 300, 500]]))

"""

import torch
import tensorflow as tf
import tensorflow_hub as hub
from simpletransformers.question_answering import QuestionAnsweringModel

model = QuestionAnsweringModel('distilbert', 'distilbert-base-uncased-distilled-squad', args={'reprocess_input_data': True, 'overwrite_output_dir': True},use_cuda=False)
to_predict = [{'context': 'This is the context used for demonstrating predictions.', 'qas': [{'question': 'What is this context?', 'id': '0'}]}]

print(model.predict(to_predict))
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
