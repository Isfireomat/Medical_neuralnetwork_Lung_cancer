import tensorflow as tf
from defs import get_train, split_array

x, y = get_train("Датасет5.txt")

X_train, X_test = split_array(x, 0.8)
Y_train, Y_test = split_array(y, 0.8)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(18,)), 
    tf.keras.layers.BatchNormalization(), 
    tf.keras.layers.Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.1)), 
    tf.keras.layers.Dropout(0.2), 
    tf.keras.layers.Dense(256, activation=tf.keras.layers.LeakyReLU(alpha=0.1)), 
    tf.keras.layers.Dropout(0.2), 
    tf.keras.layers.Dense(128, activation=tf.keras.layers.LeakyReLU(alpha=0.1)), 
    tf.keras.layers.Dropout(0.2), 
    tf.keras.layers.Dense(64, activation=tf.keras.layers.LeakyReLU(alpha=0.1)),  
    tf.keras.layers.Dropout(0.2),  
    tf.keras.layers.Dense(100, activation='softmax')  
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=250, validation_data=(X_test, Y_test))

loss, accuracy = model.evaluate(X_test, Y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

model.save('MN8.h5')
