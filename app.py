import os
import pickle
import numpy as np
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from flask import Flask, request

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5', compile=False)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def predict(inputs):
    sequence = tokenizer.texts_to_sequences(inputs)
    sequence = pad_sequences(sequence, padding='post', maxlen=5)
    predictions = model.predict(sequence)
    predictions = np.where(predictions > 0.5, 1, 0)
    return predictions


# http://127.0.0.1:5000/?name= عمر محمد احمد => Real Name
# http://127.0.0.1:5000/?name= اان$رلاا //رر => Fake Name

@app.route('/', methods=['GET'])
def home():
    name = str(request.args.get('name'))
    print(name)
    result = predict([name])
    if result[0][0] == 0:
        return "Fake Name"
    elif result[0][0] == 1:
        return "Real Name"
    return "great"


if __name__ == '__main__':
    # app.run(debug=True)
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')

