from transformers import RobertaTokenizer, RobertaModel
import torch
import numpy as np

# Load pre-trained RoBERTa tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('roberta-base')

myarray = np.load("text_roberta.npy", allow_pickle = True)
myarray = myarray.tolist()

l=[]
with open('/home/pavan/Image-Caption/sample.txt', 'r') as file:
    sentences = file.readlines()
    # Tokenize the entire text
for text in sentences:
    tokens = tokenizer(text, return_tensors='pt')

    # Forward pass through the model to get features
    outputs = model(**tokens)

    # Extract the last layer hidden states as features
    features = outputs.last_hidden_state

    # If you want to obtain a single feature vector for each line, you can use mean pooling
    line_features = torch.mean(features, dim=1)
    line_features = line_features.detach().numpy()
    l.append(line_features[0])
# print(line_features)
# Print the features for each line
# for line_feature in l:
#     print(type(line_feature))
l = np.array(l)
print("this", l)
myarray['video_1'] = l
result = myarray.items()
data = list(result)
numpyArray = np.array(data)
np.save('new.npy', numpyArray)
# 257 + 1, 274 + 1 -> kan nag
n = np.load('new.npy', allow_pickle = True)
print((n))
print(type(n))