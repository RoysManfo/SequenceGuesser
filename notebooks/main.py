import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn import model_selection

# Read the CSV file
DATA_PATH = 'data/BTC_Sequence.csv'
column_names = ['Close']
df = pd.read_csv(DATA_PATH, names=column_names, na_values='?',
                 comment='\t', sep=', ', skipinitialspace=True, skiprows=1, engine='python')

# Scale the data using MinMaxScaler
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)

# Create a dataset of 5-element sequences
window_size = 5
batch_size = 1


def create_sequences(values: np.ndarray, window_size: int):
    """
    #### Slice the dataframa in individual 5 number sequences
    """
    sequences = []
    for i in range(len(values) - window_size):
        sequences.append(values[i:i+window_size])
    return sequences


dataset = tf.data.Dataset.from_tensor_slices(
    create_sequences(normalized_data, window_size))
dataset = dataset.batch(batch_size)

model = tf.keras.Sequential(name="SeGu AI")
model.add(tf.keras.layers.SimpleRNN(16, input_shape=(5, 1)))
model.add(tf.keras.layers.Dense(5))

# Choose an optimizer and add a loss function
model.compile(optimizer='adam', loss='mse')


def reshape(target: np.ndarray) -> np.ndarray:
    passed = False
    while not passed:
        s = target
        try:
            s.reshape(-1, 5, 1)
            passed = True
        except ValueError:
            target = target[0:len(target)-1]

    return target

normalized_data = reshape(normalized_data)

# Split data between training and validation
X = normalized_data[:-5]
y = normalized_data[5:]

X_train, X_val, y_train, y_val = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, "\t->", reshape(X_train).shape)
print(X_val.shape, "\t->", reshape(X_val).shape)

X_train = reshape(X_train)
X_val = reshape(X_val)

# train the model
history = model.fit(
    X_train.reshape(-1, 5, 1),
    y_train,
    epochs=100,
    validation_data=(
        X_val.reshape(-1, 5, 1),
        y_val
    )
)