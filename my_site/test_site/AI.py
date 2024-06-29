import tensorflow as tf
import numpy as np
import os

tf.keras.utils.get_custom_objects().update({'LeakyReLU': tf.keras.layers.LeakyReLU})
current_directory = os.path.dirname(os.path.abspath(__file__))
model = tf.keras.models.load_model(os.path.join(current_directory, 'templates/models', 'MN8.h5'))

def predict_with_model(data):
    masiv = list(data.values())
    for i in range(len(masiv)):
        if type(masiv[i]) == str and not masiv[i]:
            masiv[i] = 0
        elif masiv[i] in [ "female","male"]:
            masiv[i] = [ "female","male"].index(masiv[i])
        else:
            masiv[i] = int(masiv[i])
        if type(masiv[i]) == bool: 
            masiv[i] = int(masiv[i])
    predictions = model.predict(np.reshape(masiv, (1, 18)))
    return list(range(101))[np.argmax(predictions[0])]