import numpy as np
import random

def split_array(array, size):
    split_index = int(len(array) * size)
    array_size_percent = array[:split_index]
    remaining_array = array[split_index:]  
    return array_size_percent, remaining_array

def shuffle_arrays(array1, array2):
    indices = list(range(len(array1)))
    random.shuffle(indices)
    array1_shuffled = [array1[i] for i in indices]
    array2_shuffled = [array2[i] for i in indices]
    return array1_shuffled, array2_shuffled

def get_train(dataset):
    X_train = []
    Y_train = []
    with open(dataset, "r") as f:
        for l in f:
            masiv=eval(l)
            X_train.append(masiv[:len(masiv)-1])
            zeroes=[0]*100
            zeroes[int(masiv[len(masiv)-1])-1]=1
            Y_train.append(zeroes)
    
    X_train, Y_train = shuffle_arrays(X_train, Y_train)
    return np.array(X_train), np.array(Y_train)
