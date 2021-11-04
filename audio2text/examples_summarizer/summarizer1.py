

# https://www.youtube.com/watch?v=TsfLm5iiYb4
# https://github.com/nicknochnack/Hugging-Face-Transformers-Summarization/blob/main/Summarization.ipynb

# pip3 install transformers
# pip3 install tensorflow
# pip3 install nltk

#from transformers import pipeline
#summarizer = pipeline("summarization")

ARTICLE = """
find the conversation Sam Harris what are the most influential and pioneering thinkers of our time he's a host of The Making Sense podcast and the author of many similar books and human nature and the human mind including the end of Faith the moral landscape lying free will and waking up he also has a meditation app called waking up and I've been using to guide my own meditation could mention of our sponsors national instruments belcampo athlet. 
"""

#summarizer(ARTICLE, max_length=100, min_length=30, do_sample=False)

"""
untimeError: At least one of TensorFlow 2.0 or PyTorch should be installed. 
To install TensorFlow 2.0, read the instructions at https://www.tensorflow.org/install/ 
To install PyTorch, read the instructions at https://pytorch.org/.

https://beta.openai.com/examples
https://beta.openai.com/examples/default-summarize
https://www.mygreatlearning.com/blog/text-summarization-in-python/
"""

"""
import openai

openai.api_key 'KEY'

response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt="Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals, which involves consciousness and emotionality. The distinction between the former and the latter categories is often revealed by the acronym chosen. 'Strong' AI is usually labelled as AGI (Artificial General Intelligence) while attempts to emulate 'natural' intelligence have been called ABI (Artificial Biological Intelligence). Leading AI textbooks define the field as the study of \"intelligent agents\": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[3] Colloquially, the term \"artificial intelligence\" is often used to describe machines (or computers) that mimic \"cognitive\" functions that humans associate with the human mind, such as \"learning\" and \"problem solving\".[4]\n\nAs machines become increasingly capable, tasks considered to require \"intelligence\" are often removed from the definition of AI, a phenomenon known as the AI effect.[5] A quip in Tesler's Theorem says \"AI is whatever hasn't been done yet.\"[6] For instance, optical character recognition is frequently excluded from things considered to be AI,[7] having become a routine technology.[8] Modern machine capabilities generally classified as AI include successfully understanding human speech,[9] competing at the highest level in strategic game systems (such as chess and Go),[10] autonomously operating cars, intelligent routing in content delivery networks, and military simulations.[11]\n\ntl;dr:",
  temperature=0.25,
  max_tokens=100,
  top_p=1
)
"""




import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = """
Junk foods taste good that’s why it is mostly liked by everyone of any age group especially kids and school going children. They generally ask for the junk food daily because they have been trend so by their parents from the childhood. They never have been discussed by their parents about the harmful effects of junk foods over health. According to the research by scientists, it has been found that junk foods have negative effects on the health in many ways. They are generally fried food found in the market in the packets. They become high in calories, high in cholesterol, low in healthy nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of dietary fibers. Processed and junk foods are the means of rapid and unhealthy weight gain and negatively impact the whole body throughout the life. It makes able a person to gain excessive weight which is called as obesity. Junk foods tastes good and looks good however do not fulfil the healthy calorie requirement of the body.  
"""

stopwords = set (stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopwords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1


# create dict
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

average = int(sumValues / len(sentenceValue))

sumary = ''
for sentence in sentenceValue:
    if(sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        sumary+= " " + sentence
print(sumary)