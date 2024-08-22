from keras.layers import Dense
from keras.models import Sequential

# define the neural network model
def MLP(n_input):
 # define model
 model = Sequential()
 # define first hidden layer and visible layer
 model.add(Dense(10, input_dim=n_input, activation='relu', kernel_initializer='he_uniform'))
 # define output layer
 model.add(Dense(1, activation='sigmoid'))
 # define loss and optimizer
 model.compile(loss='binary_crossentropy', optimizer='sgd')
 return model