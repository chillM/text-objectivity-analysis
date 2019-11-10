import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pandas
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers

tf.__version__

# Import data from the file into a dataframe.
english_df = pd.read_csv('/lib/data/opinion_test_file.csv', sep='\n', header=None, names=['English'])
english_df.shape
print(english_df)

# # Final dataset dataframe.
# df = pd.concat([english_df], axis=1, join='inner')
# df.info()
# df.shape

# #Remove missing blanks and blank records from data.
# """
# df['English'].replace('', np.nan, inplace=True)
# df.dropna(subset=['English'], inplace=True)
# """
# # Lowercase english sentences as part of preprocessing
# df1=df.copy()
# df1["English"] = df1["English"].str.lower()

# # Tokenize the data and calculate vocabulary count.
# # # # # def tokenization(sentences):
#     tokenizer = Tokenizer(lower=false)
#     tokenizer.fit_on_texts(sentences)
#     return tokenizer
# txt_tokenizer = tokenization(df1["English"].astype('str'))
# txt_vocab_size = len(txt_tokenizer.word_index) + 1

# # Convert the text to integer sequences and pad the sequences.
# text_sequences = txt_tokenizer.texts_to_sequences(df1["English"].values)
# text_sequences = pad_sequences(text_sequences, padding='post')

# # Split data into test and train.
# (x_train, y_train), (x_test, y_test) = train_test_split(text_sequences,


# )

# # Define model.
# model = Sequential
# model.add(Dense(32, input_shape))
# model.add(Dense(1, activation='sigmoid'))
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy']) 

# # Train the model.
# model.fit(x_train, y_train, epochs=5)

# # Test the model.
# score=model.evaluate(x_test, y_test)
# print(score)
