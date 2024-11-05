from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
import numpy as np

data= np.array([
    ['Red','Sports','Domestic','Yes'],
    ['Red','Sports','Domestic','No'],
    ['Red','Sports','Domestic','Yes'],
    ['Yellow','Sports','Domestic','No'],
    ['Yellow','Sports','Imported','Yes'],
    ['Yellow','SUV','Imported','No'],
    ['Yellow','SUV','Imported','Yes'],
    ['Yellow','SUV','Domestic','No'],
    ['Red','SUV','Imported','No'],
    ['Red','Sports','Imported','Yes']
    ])

X= data[:, :-1]
y= data[:, -1]

label_encoders=[]
for i in range(X.shape[1]):
    le=LabelEncoder()
    X[:, i]=le.fit_transform(X[:, i])
    label_encoders.append(le)

label_encoder_y=LabelEncoder()
y=label_encoder_y.fit_transform(y)

model= CategoricalNB()
model.fit(X,y)

new_tuple= np.array([['Red','SUV','Domestic']])

encoded_tuple= new_tuple.copy()
for i in range(new_tuple.shape[1]):
    encoded_tuple[:, i]=label_encoders[i].transform(new_tuple[:, i])

prediction=model.predict(encoded_tuple)
prediction_label=label_encoder_y.inverse_transform(prediction)

print(f"Input Tuple: Color={new_tuple[0][0]}, Type={new_tuple[0][1]}, Origin={new_tuple[0][2]}")
print(f"Prediction: The Car is Stolen:{prediction_label[0]}")
    
