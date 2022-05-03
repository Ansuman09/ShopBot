import random
import json
import pandas as pd
import torch
import re

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from nltk.stem.porter import PorterStemmer


stemmer=PorterStemmer()
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu' )

with open('intents.json','r') as data:
    intents=json.load(data)

saved_model=torch.load('data.pth')

model_state=saved_model['model_state']
input_dim=saved_model['input_size']
output_dim=saved_model['output_size']
hidden_dim=saved_model['hiddent_size']
tags=saved_model['tags']
all_words=saved_model['all_words']

model=NeuralNet(input_dim,hidden_dim,output_dim).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = 'REMY'

available=pd.read_csv('item1.csv')
available_items=list(available['items'])
print(available_items)
def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if 'available' in sentence:
        process_text = re.findall("'([^']+)", msg)[0]
        m = [stemmer.stem(k) for k in process_text.split()]
        final_word = (' ').join(m)
        print(final_word)
        if final_word in available_items:
            print('final_word')
            return 'We have this item at the store'
        else:
            return 'We do not have this item'
    elif prob.item() > 0.75:
        for intent in intents['intents']:
            if tag=='hello':
                return f"{random.choice(intent['responses'])}." \
                       f"If you would like to look for an item, pass the item name in quotation marks and use the word available?"
            elif tag == intent["tag"]:
                print(random.choice(intent['responses']))
                return random.choice(intent['responses'])

    return "I do not understand..."