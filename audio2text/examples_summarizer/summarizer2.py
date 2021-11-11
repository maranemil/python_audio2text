# OK

import os
import tensorflow as tf
from transformers import pipeline

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# import tensorflow as tf
# gpus = tf.config.experimental.list_physical_devices("GPU")
# tf.config.experimental.set_memory_growth(gpus[0], True)


# gpus = tf.config.experimental.list_physical_devices(‘GPU’)
# print(gpus)
# tf.config.experimental.set_memory_growth(gpus[0], True)


# Open and read the article
f = open("recognized.txt", "r", encoding="utf8")
to_tokenize = f.read()

# Initialize the HuggingFace summarization pipeline
summarizer = pipeline("summarization")
summarized = summarizer(to_tokenize, min_length=50, max_length=100)

# Print summarized text
print(summarized)

# https://www.machinecurve.com/index.php/2020/12/21/easy-text-summarization-with-huggingface-transformers-and-machine-learning/
