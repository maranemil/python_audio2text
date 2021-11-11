# OK

# sudo pip3 install sumy

import sumy

# sumy.summarizers

original_text = 'Junk foods taste good that’s why it is mostly liked by everyone of any age group especially kids and ' \
                'school going children. They generally ask for the junk food daily because they have been trend so by ' \
                'their parents from the childhood. They never have been discussed by their parents about the harmful ' \
                'effects of junk foods over health. According to the research by scientists, it has been found that ' \
                'junk foods have negative effects on the health in many ways. They are generally fried food found in ' \
                'the market in the packets. They become high in calories, high in cholesterol, low in healthy ' \
                'nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of ' \
                'dietary fibers. Processed and junk foods are the means of rapid and unhealthy weight gain and ' \
                'negatively impact the whole body throughout the life. It makes able a person to gain excessive weight ' \
                'which is called as obesity. Junk foods tastes good and looks good however do not fulfil the healthy ' \
                'calorie requirement of the body. Some of the foods like french fries, fried foods, pizza, burgers, ' \
                'candy, soft drinks, baked goods, ice cream, cookies, etc are the example of high-sugar and high-fat ' \
                'containing foods. It is found according to the Centres for Disease Control and Prevention that Kids ' \
                'and children eating junk food are more prone to the type-2 diabetes. In type-2 diabetes our body ' \
                'become unable to regulate blood sugar level. Risk of getting this disease is increasing as one become ' \
                'more obese or overweight. It increases the risk of kidney failure. Eating junk food daily lead us to ' \
                'the nutritional deficiencies in the body because it is lack of essential nutrients, vitamins, iron, ' \
                'minerals and dietary fibers. It increases risk of cardiovascular diseases because it is rich in ' \
                'saturated fat, sodium and bad cholesterol. High sodium and bad cholesterol diet increases blood ' \
                'pressure and overloads the heart functioning. One who like junk food develop more risk to put on extra ' \
                'weight and become fatter and unhealthier. Junk foods contain high level carbohydrate which spike blood ' \
                'sugar level and make person more lethargic, sleepy and less active and alert. Reflexes and senses of ' \
                'the people eating this food become dull day by day thus they live more sedentary life. Junk foods are ' \
                'the source of constipation and other disease like diabetes, heart ailments, clogged arteries, ' \
                'heart attack, strokes, etc because of being poor in nutrition. Junk food is the easiest way to gain ' \
                'unhealthy weight. The amount of fats and sugar in the food makes you gain weight rapidly. However, ' \
                'this is not a healthy weight. It is more of fats and cholesterol which will have a harmful impact on ' \
                'your health. Junk food is also one of the main reasons for the increase in obesity nowadays.This food ' \
                'only looks and tastes good, other than that, it has no positive points. The amount of calorie your ' \
                'body requires to stay fit is not fulfilled by this food. For instance, foods like French fries, ' \
                'burgers, candy, and cookies, all have high amounts of sugar and fats. Therefore, this can result in ' \
                'long-term illnesses like diabetes and high blood pressure. This may also result in kidney failure. ' \
                'Above all, you can get various nutritional deficiencies when you don’t consume the essential ' \
                'nutrients, vitamins, minerals and more. You become prone to cardiovascular diseases due to the ' \
                'consumption of bad cholesterol and fat plus sodium. In other words, all this interferes with the ' \
                'functioning of your heart. Furthermore, junk food contains a higher level of carbohydrates. It will ' \
                'instantly spike your blood sugar levels. This will result in lethargy, inactivates, and sleepiness. A ' \
                'person reflex becomes dull overtime and they lead an inactive life. To make things worse, ' \
                'junk food also clogs your arteries and increases the risk of a heart attack. Therefore, it must be ' \
                'avoided at the first instance to save your life from becoming ruined.The main problem with junk food ' \
                'is that people don’t realize its ill effects now. When the time comes, it is too late. Most ' \
                'importantly, the issue is that it does not impact you instantly. It works on your overtime; you will ' \
                'face the consequences sooner or later. Thus, it is better to stop now.You can avoid junk food by ' \
                'encouraging your children from an early age to eat green vegetables. Their taste buds must be ' \
                'developed as such that they find healthy food tasty. Moreover, try to mix things up. Do not serve the ' \
                'same green vegetable daily in the same style. Incorporate different types of healthy food in their ' \
                'diet following different recipes. This will help them to try foods at home rather than being attracted ' \
                'to junk food.In short, do not deprive them completely of it as that will not help. Children will find ' \
                'one way or the other to have it. Make sure you give them junk food in limited quantities and at ' \
                'healthy periods of time. '

# Importing the parser and tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Import the LexRank summarizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Initializing the parser
my_parser = PlaintextParser.from_string(original_text, Tokenizer('english'))

# Creating a summary of 3 sentences.
ranksummarizer = LexRankSummarizer()
lexrank_summary = ranksummarizer(my_parser.document, sentences_count=3)

# Printing the summary
for sentence in lexrank_summary:
    print(sentence)
    print('-----------')

    #
    # Import the summarizer
from sumy.summarizers.lsa import LsaSummarizer

# Text to summarize
original_text = 'Junk foods taste good that’s why it is mostly liked by everyone of any age group especially kids and ' \
                'school going children. They generally ask for the junk food daily because they have been trend so by ' \
                'their parents from the childhood. They never have been discussed by their parents about the harmful ' \
                'effects of junk foods over health. According to the research by scientists, it has been found that ' \
                'junk foods have negative effects on the health in many ways. They are generally fried food found in ' \
                'the market in the packets. They become high in calories, high in cholesterol, low in healthy ' \
                'nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of ' \
                'dietary fibers. Processed and junk foods are the means of rapid and unhealthy weight gain and ' \
                'negatively impact the whole body throughout the life. It makes able a person to gain excessive ' \
                'weight which is called as obesity. Junk foods tastes good and looks good however do not fulfil the ' \
                'healthy calorie requirement of the body. Some of the foods like french fries, fried foods, pizza, ' \
                'burgers, candy, soft drinks, baked goods, ice cream, cookies, etc are the example of high-sugar and ' \
                'high-fat containing foods. It is found according to the Centres for Disease Control and Prevention ' \
                'that Kids and children eating junk food are more prone to the type-2 diabetes. In type-2 diabetes ' \
                'our body become unable to regulate blood sugar level. Risk of getting this disease is increasing as ' \
                'one become more obese or overweight. It increases the risk of kidney failure. Eating junk food daily ' \
                'lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, ' \
                'vitamins, iron, minerals and dietary fibers. It increases risk of cardiovascular diseases because it ' \
                'is rich in saturated fat, sodium and bad cholesterol. High sodium and bad cholesterol diet increases ' \
                'blood pressure and overloads the heart functioning. One who like junk food develop more risk to put ' \
                'on extra weight and become fatter and unhealthier. Junk foods contain high level carbohydrate which ' \
                'spike blood sugar level and make person more lethargic, sleepy and less active and alert. Reflexes ' \
                'and senses of the people eating this food become dull day by day thus they live more sedentary life. ' \
                'Junk foods are the source of constipation and other disease like diabetes, heart ailments, ' \
                'clogged arteries, heart attack, strokes, etc because of being poor in nutrition. Junk food is the ' \
                'easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight ' \
                'rapidly. However, this is not a healthy weight. It is more of fats and cholesterol which will have a ' \
                'harmful impact on your health. Junk food is also one of the main reasons for the increase in obesity ' \
                'nowadays.This food only looks and tastes good, other than that, it has no positive points. The ' \
                'amount of calorie your body requires to stay fit is not fulfilled by this food. For instance, ' \
                'foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats. ' \
                'Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may ' \
                'also result in kidney failure. Above all, you can get various nutritional deficiencies when you ' \
                'don’t consume the essential nutrients, vitamins, minerals and more. You become prone to ' \
                'cardiovascular diseases due to the consumption of bad cholesterol and fat plus sodium. In other ' \
                'words, all this interferes with the functioning of your heart. Furthermore, junk food contains a ' \
                'higher level of carbohydrates. It will instantly spike your blood sugar levels. This will result in ' \
                'lethargy, inactivates, and sleepiness. A person reflex becomes dull overtime and they lead an ' \
                'inactive life. To make things worse, junk food also clogs your arteries and increases the risk of a ' \
                'heart attack. Therefore, it must be avoided at the first instance to save your life from becoming ' \
                'ruined.The main problem with junk food is that people don’t realize its ill effects now. When the ' \
                'time comes, it is too late. Most importantly, the issue is that it does not impact you instantly. It ' \
                'works on your overtime; you will face the consequences sooner or later. Thus, it is better to stop ' \
                'now.You can avoid junk food by encouraging your children from an early age to eat green vegetables. ' \
                'Their taste buds must be developed as such that they find healthy food tasty. Moreover, try to mix ' \
                'things up. Do not serve the same green vegetable daily in the same style. Incorporate different ' \
                'types of healthy food in their diet following different recipes. This will help them to try foods at ' \
                'home rather than being attracted to junk food.In short, do not deprive them completely of it as that ' \
                'will not help. Children will find one way or the other to have it. Make sure you give them junk food ' \
                'in limited quantities and at healthy periods of time. '

# Parsing the text string using PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser

parser = PlaintextParser.from_string(original_text, Tokenizer('english'))

# creating the summarizer
lsa_summarizer = LsaSummarizer()
lsa_summary = lsa_summarizer(parser.document, 3)

# Printing the summary
for sentence in lsa_summary:
    print(sentence)
    print('-----------')

# Import the summarizer
from sumy.summarizers.luhn import LuhnSummarizer

# text to summarize
original_text = 'Junk foods taste good that’s why it is mostly liked by everyone of any age group especially kids and ' \
                'school going children. They generally ask for the junk food daily because they have been trend so by ' \
                'their parents from the childhood. They never have been discussed by their parents about the harmful ' \
                'effects of junk foods over health. According to the research by scientists, it has been found that ' \
                'junk foods have negative effects on the health in many ways. They are generally fried food found in ' \
                'the market in the packets. They become high in calories, high in cholesterol, low in healthy ' \
                'nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of ' \
                'dietary fibers. Processed and junk foods are the means of rapid and unhealthy weight gain and ' \
                'negatively impact the whole body throughout the life. It makes able a person to gain excessive ' \
                'weight which is called as obesity. Junk foods tastes good and looks good however do not fulfil the ' \
                'healthy calorie requirement of the body. Some of the foods like french fries, fried foods, pizza, ' \
                'burgers, candy, soft drinks, baked goods, ice cream, cookies, etc are the example of high-sugar and ' \
                'high-fat containing foods. It is found according to the Centres for Disease Control and Prevention ' \
                'that Kids and children eating junk food are more prone to the type-2 diabetes. In type-2 diabetes ' \
                'our body become unable to regulate blood sugar level. Risk of getting this disease is increasing as ' \
                'one become more obese or overweight. It increases the risk of kidney failure. Eating junk food daily ' \
                'lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, ' \
                'vitamins, iron, minerals and dietary fibers. It increases risk of cardiovascular diseases because it ' \
                'is rich in saturated fat, sodium and bad cholesterol. High sodium and bad cholesterol diet increases ' \
                'blood pressure and overloads the heart functioning. One who like junk food develop more risk to put ' \
                'on extra weight and become fatter and unhealthier. Junk foods contain high level carbohydrate which ' \
                'spike blood sugar level and make person more lethargic, sleepy and less active and alert. Reflexes ' \
                'and senses of the people eating this food become dull day by day thus they live more sedentary life. ' \
                'Junk foods are the source of constipation and other disease like diabetes, heart ailments, ' \
                'clogged arteries, heart attack, strokes, etc because of being poor in nutrition. Junk food is the ' \
                'easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight ' \
                'rapidly. However, this is not a healthy weight. It is more of fats and cholesterol which will have a ' \
                'harmful impact on your health. Junk food is also one of the main reasons for the increase in obesity ' \
                'nowadays.This food only looks and tastes good, other than that, it has no positive points. The ' \
                'amount of calorie your body requires to stay fit is not fulfilled by this food. For instance, ' \
                'foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats. ' \
                'Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may ' \
                'also result in kidney failure. Above all, you can get various nutritional deficiencies when you ' \
                'don’t consume the essential nutrients, vitamins, minerals and more. You become prone to ' \
                'cardiovascular diseases due to the consumption of bad cholesterol and fat plus sodium. In other ' \
                'words, all this interferes with the functioning of your heart. Furthermore, junk food contains a ' \
                'higher level of carbohydrates. It will instantly spike your blood sugar levels. This will result in ' \
                'lethargy, inactivates, and sleepiness. A person reflex becomes dull overtime and they lead an ' \
                'inactive life. To make things worse, junk food also clogs your arteries and increases the risk of a ' \
                'heart attack. Therefore, it must be avoided at the first instance to save your life from becoming ' \
                'ruined.The main problem with junk food is that people don’t realize its ill effects now. When the ' \
                'time comes, it is too late. Most importantly, the issue is that it does not impact you instantly. It ' \
                'works on your overtime; you will face the consequences sooner or later. Thus, it is better to stop ' \
                'now.You can avoid junk food by encouraging your children from an early age to eat green vegetables. ' \
                'Their taste buds must be developed as such that they find healthy food tasty. Moreover, try to mix ' \
                'things up. Do not serve the same green vegetable daily in the same style. Incorporate different ' \
                'types of healthy food in their diet following different recipes. This will help them to try foods at ' \
                'home rather than being attracted to junk food.In short, do not deprive them completely of it as that ' \
                'will not help. Children will find one way or the other to have it. Make sure you give them junk food ' \
                'in limited quantities and at healthy periods of time. '

# Creating the parser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser

parser = PlaintextParser.from_string(original_text, Tokenizer('english'))

#  Creating the summarizer
luhn_summarizer = LuhnSummarizer()
luhn_summary = luhn_summarizer(parser.document, sentences_count=3)

# Printing the summary
for sentence in luhn_summary:
    print(sentence)
    print('-----------')

# KLSummarizer

from sumy.summarizers.kl import KLSummarizer

# Our text to perform summarization
original_text = 'Junk foods taste good that’s why it is mostly liked by everyone of any age group especially kids and ' \
                'school going children. They generally ask for the junk food daily because they have been trend so by ' \
                'their parents from the childhood. They never have been discussed by their parents about the harmful ' \
                'effects of junk foods over health. According to the research by scientists, it has been found that ' \
                'junk foods have negative effects on the health in many ways. They are generally fried food found in ' \
                'the market in the packets. They become high in calories, high in cholesterol, low in healthy ' \
                'nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of ' \
                'dietary fibers. Processed and junk foods are the means of rapid and unhealthy weight gain and ' \
                'negatively impact the whole body throughout the life. It makes able a person to gain excessive ' \
                'weight which is called as obesity. Junk foods tastes good and looks good however do not fulfil the ' \
                'healthy calorie requirement of the body. Some of the foods like french fries, fried foods, pizza, ' \
                'burgers, candy, soft drinks, baked goods, ice cream, cookies, etc are the example of high-sugar and ' \
                'high-fat containing foods. It is found according to the Centres for Disease Control and Prevention ' \
                'that Kids and children eating junk food are more prone to the type-2 diabetes. In type-2 diabetes ' \
                'our body become unable to regulate blood sugar level. Risk of getting this disease is increasing as ' \
                'one become more obese or overweight. It increases the risk of kidney failure. Eating junk food daily ' \
                'lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, ' \
                'vitamins, iron, minerals and dietary fibers. It increases risk of cardiovascular diseases because it ' \
                'is rich in saturated fat, sodium and bad cholesterol. High sodium and bad cholesterol diet increases ' \
                'blood pressure and overloads the heart functioning. One who like junk food develop more risk to put ' \
                'on extra weight and become fatter and unhealthier. Junk foods contain high level carbohydrate which ' \
                'spike blood sugar level and make person more lethargic, sleepy and less active and alert. Reflexes ' \
                'and senses of the people eating this food become dull day by day thus they live more sedentary life. ' \
                'Junk foods are the source of constipation and other disease like diabetes, heart ailments, ' \
                'clogged arteries, heart attack, strokes, etc because of being poor in nutrition. Junk food is the ' \
                'easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight ' \
                'rapidly. However, this is not a healthy weight. It is more of fats and cholesterol which will have a ' \
                'harmful impact on your health. Junk food is also one of the main reasons for the increase in obesity ' \
                'nowadays.This food only looks and tastes good, other than that, it has no positive points. The ' \
                'amount of calorie your body requires to stay fit is not fulfilled by this food. For instance, ' \
                'foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats. ' \
                'Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may ' \
                'also result in kidney failure. Above all, you can get various nutritional deficiencies when you ' \
                'don’t consume the essential nutrients, vitamins, minerals and more. You become prone to ' \
                'cardiovascular diseases due to the consumption of bad cholesterol and fat plus sodium. In other ' \
                'words, all this interferes with the functioning of your heart. Furthermore, junk food contains a ' \
                'higher level of carbohydrates. It will instantly spike your blood sugar levels. This will result in ' \
                'lethargy, inactivates, and sleepiness. A person reflex becomes dull overtime and they lead an ' \
                'inactive life. To make things worse, junk food also clogs your arteries and increases the risk of a ' \
                'heart attack. Therefore, it must be avoided at the first instance to save your life from becoming ' \
                'ruined.The main problem with junk food is that people don’t realize its ill effects now. When the ' \
                'time comes, it is too late. Most importantly, the issue is that it does not impact you instantly. It ' \
                'works on your overtime; you will face the consequences sooner or later. Thus, it is better to stop ' \
                'now.You can avoid junk food by encouraging your children from an early age to eat green vegetables. ' \
                'Their taste buds must be developed as such that they find healthy food tasty. Moreover, try to mix ' \
                'things up. Do not serve the same green vegetable daily in the same style. Incorporate different ' \
                'types of healthy food in their diet following different recipes. This will help them to try foods at ' \
                'home rather than being attracted to junk food.In short, do not deprive them completely of it as that ' \
                'will not help. Children will find one way or the other to have it. Make sure you give them junk food ' \
                'in limited quantities and at healthy periods of time. '

# Creating the parser
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser

parser = PlaintextParser.from_string(original_text, Tokenizer('english'))

# Instantiating the  KLSummarizer
kl_summarizer = KLSummarizer()
kl_summary = kl_summarizer(parser.document, sentences_count=3)

# Printing the summary
for sentence in kl_summary:
    print(sentence)
    print('-----------')

"""
# Abstractive Text Summarization
# pip install transformers

# Importing requirements
from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration

# text to summarize original_text='Junk foods taste good that’s why it is mostly liked by everyone of any age group 
especially kids and school going children. They generally ask for the junk food daily because they have been trend so 
by their parents from the childhood. They never have been discussed by their parents about the harmful effects of 
junk foods over health. According to the research by scientists, it has been found that junk foods have negative 
effects on the health in many ways. They are generally fried food found in the market in the packets. They become 
high in calories, high in cholesterol, low in healthy nutrients, high in sodium mineral, high in sugar, starch, 
unhealthy fat, lack of protein and lack of dietary fibers. Processed and junk foods are the means of rapid and 
unhealthy weight gain and negatively impact the whole body throughout the life. It makes able a person to gain 
excessive weight which is called as obesity. Junk foods tastes good and looks good however do not fulfil the healthy 
calorie requirement of the body. Some of the foods like french fries, fried foods, pizza, burgers, candy, 
soft drinks, baked goods, ice cream, cookies, etc are the example of high-sugar and high-fat containing foods. It is 
found according to the Centres for Disease Control and Prevention that Kids and children eating junk food are more 
prone to the type-2 diabetes. In type-2 diabetes our body become unable to regulate blood sugar level. Risk of 
getting this disease is increasing as one become more obese or overweight. It increases the risk of kidney failure. 
Eating junk food daily lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, 
vitamins, iron, minerals and dietary fibers. It increases risk of cardiovascular diseases because it is rich in 
saturated fat, sodium and bad cholesterol. High sodium and bad cholesterol diet increases blood pressure and 
overloads the heart functioning. One who like junk food develop more risk to put on extra weight and become fatter 
and unhealthier. Junk foods contain high level carbohydrate which spike blood sugar level and make person more 
lethargic, sleepy and less active and alert. Reflexes and senses of the people eating this food become dull day by 
day thus they live more sedentary life. Junk foods are the source of constipation and other disease like diabetes, 
heart ailments, clogged arteries, heart attack, strokes, etc because of being poor in nutrition. Junk food is the 
easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight rapidly. 
However, this is not a healthy weight. It is more of fats and cholesterol which will have a harmful impact on your 
health. Junk food is also one of the main reasons for the increase in obesity nowadays.This food only looks and 
tastes good, other than that, it has no positive points. The amount of calorie your body requires to stay fit is not 
fulfilled by this food. For instance, foods like French fries, burgers, candy, and cookies, all have high amounts of 
sugar and fats. Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may 
also result in kidney failure. Above all, you can get various nutritional deficiencies when you don’t consume the 
essential nutrients, vitamins, minerals and more. You become prone to cardiovascular diseases due to the consumption 
of bad cholesterol and fat plus sodium. In other words, all this interferes with the functioning of your heart. 
Furthermore, junk food contains a higher level of carbohydrates. It will instantly spike your blood sugar levels. 
This will result in lethargy, inactivates, and sleepiness. A person reflex becomes dull overtime and they lead an 
inactive life. To make things worse, junk food also clogs your arteries and increases the risk of a heart attack. 
Therefore, it must be avoided at the first instance to save your life from becoming ruined.The main problem with junk 
food is that people don’t realize its ill effects now. When the time comes, it is too late. Most importantly, 
the issue is that it does not impact you instantly. It works on your overtime; you will face the consequences sooner 
or later. Thus, it is better to stop now.You can avoid junk food by encouraging your children from an early age to 
eat green vegetables. Their taste buds must be developed as such that they find healthy food tasty. Moreover, 
try to mix things up. Do not serve the same green vegetable daily in the same style. Incorporate different types of 
healthy food in their diet following different recipes. This will help them to try foods at home rather than being 
attracted to junk food.In short, do not deprive them completely of it as that will not help. Children will find one 
way or the other to have it. Make sure you give them junk food in limited quantities and at healthy periods of time. ' 


# Instantiating the model and tokenizer 
my_model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
# Concatenating the word "summarize:" to raw text
text = "summarize:" + original_text
text

'summarize:Junk foods taste good that’s why it is mostly liked by everyone of any age group especially kids and school going children. They generally ask for the junk food daily because they have been trend so by their parents from the childhood. They never have been discussed by their parents about the harmful effects of junk foods over health. According to the research by scientists, it has been found that junk foods have negative effects on the health in many ways. They are generally fried food found in the market in the packets. They become high in calories, high in cholesterol, low in healthy nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of dietary fibers. Processed and junk foods are the means of rapid and unhealthy weight gain and negatively impact the whole body throughout the life. It makes able a person to gain excessive weight which is called as obesity. Junk foods tastes good and looks good however do not fulfil the healthy calorie requirement of the body. Some of the foods like french fries, fried foods, pizza, burgers, candy, soft drinks, baked goods, ice cream, cookies, etc are the example of high-sugar and high-fat containing foods. It is found according to the Centres for Disease Control and Prevention that Kids and children eating junk food are more prone to the type-2 diabetes. In type-2 diabetes our body become unable to regulate blood sugar level. Risk of getting this disease is increasing as one become more obese or overweight. It increases the risk of kidney failure. Eating junk food daily lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, vitamins, iron, minerals and dietary fibers. It increases risk of cardiovascular diseases because it is rich in saturated fat, sodium and bad cholesterol. High sodium and bad cholesterol diet increases blood pressure and overloads the heart functioning. One who like junk food develop more risk to put on extra weight and become fatter and unhealthier. Junk foods contain high level carbohydrate which spike blood sugar level and make person more lethargic, sleepy and less active and alert. Reflexes and senses of the people eating this food become dull day by day thus they live more sedentary life. Junk foods are the source of constipation and other disease like diabetes, heart ailments, clogged arteries, heart attack, strokes, etc because of being poor in nutrition. Junk food is the easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight rapidly. However, this is not a healthy weight. It is more of fats and cholesterol which will have a harmful impact on your health. Junk food is also one of the main reasons for the increase in obesity nowadays.This food only looks and tastes good, other than that, it has no positive points. The amount of calorie your body requires to stay fit is not fulfilled by this food. For instance, foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats. Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may also result in kidney failure. Above all, you can get various nutritional deficiencies when you don’t consume the essential nutrients, vitamins, minerals and more. You become prone to cardiovascular diseases due to the consumption of bad cholesterol and fat plus sodium. In other words, all this interferes with the functioning of your heart. Furthermore, junk food contains a higher level of carbohydrates. It will instantly spike your blood sugar levels. This will result in lethargy, inactiveness, and sleepiness. A person reflex becomes dull overtime and they lead an inactive life. To make things worse, junk food also clogs your arteries and increases the risk of a heart attack. Therefore, it must be avoided at the first instance to save your life from becoming ruined.The main problem with junk food is that people don’t realize its ill effects now. When the time comes, it is too late. Most importantly, the issue is that it does not impact you instantly. It works on your overtime; you will face the consequences sooner or later. Thus, it is better to stop now.You can avoid junk food by encouraging your children from an early age to eat green vegetables. Their taste buds must be developed as such that they find healthy food tasty. Moreover, try to mix things up. Do not serve the same green vegetable daily in the same style. Incorporate different types of healthy food in their diet following different recipes. This will help them to try foods at home rather than being attracted to junk food.In short, do not deprive them completely of it as that will not help. Children will find one way or the other to have it. Make sure you give them junk food in limited quantities and at healthy periods of time. '


# encoding the input text
input_ids=tokenizer.encode(text, return_tensors='pt', max_length=512)
# Generating summary ids
summary_ids = my_model.generate(input_ids)
summary_ids
# Decoding the tensor and printing the summary.
t5_summary = tokenizer.decode(summary_ids[0])
print(t5_summary)




# Summarization with BART Transformers
# Importing the model
from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig
# Loading the model and tokenizer for bart-large-cnn
tokenizer=BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model=BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

original_text = 'Junk foods taste good that’s why it is mostly liked by everyone of any age group especially kids and school going children. They generally ask for the junk food daily because they have been trend so by their parents from the childhood. They never have been discussed by their parents about the harmful effects of junk foods over health. According to the research by scientists, it has been found that junk foods have negative effects on the health in many ways. They are generally fried food found in the market in the packets. They become high in calories, high in cholesterol, low in healthy nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of dietary fibers. Processed and junk foods are the means of rapid and unhealthy weight gain and negatively impact the whole body throughout the life. It makes able a person to gain excessive weight which is called as obesity. Junk foods tastes good and looks good however do not fulfil the healthy calorie requirement of the body. Some of the foods like french fries, fried foods, pizza, burgers, candy, soft drinks, baked goods, ice cream, cookies, etc are the example of high-sugar and high-fat containing foods. It is found according to the Centres for Disease Control and Prevention that Kids and children eating junk food are more prone to the type-2 diabetes. In type-2 diabetes our body become unable to regulate blood sugar level. Risk of getting this disease is increasing as one become more obese or overweight. It increases the risk of kidney failure. Eating junk food daily lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, vitamins, iron, minerals and dietary fibers. It increases risk of cardiovascular diseases because it is rich in saturated fat, sodium and bad cholesterol. High sodium and bad cholesterol diet increases blood pressure and overloads the heart functioning. One who like junk food develop more risk to put on extra weight and become fatter and unhealthier. Junk foods contain high level carbohydrate which spike blood sugar level and make person more lethargic, sleepy and less active and alert. Reflexes and senses of the people eating this food become dull day by day thus they live more sedentary life. Junk foods are the source of constipation and other disease like diabetes, heart ailments, clogged arteries, heart attack, strokes, etc because of being poor in nutrition. Junk food is the easiest way to gain unhealthy weight. The amount of fats and sugar in the food makes you gain weight rapidly. However, this is not a healthy weight. It is more of fats and cholesterol which will have a harmful impact on your health. Junk food is also one of the main reasons for the increase in obesity nowadays.This food only looks and tastes good, other than that, it has no positive points. The amount of calorie your body requires to stay fit is not fulfilled by this food. For instance, foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats. Therefore, this can result in long-term illnesses like diabetes and high blood pressure. This may also result in kidney failure. Above all, you can get various nutritional deficiencies when you don’t consume the essential nutrients, vitamins, minerals and more. You become prone to cardiovascular diseases due to the consumption of bad cholesterol and fat plus sodium. In other words, all this interferes with the functioning of your heart. Furthermore, junk food contains a higher level of carbohydrates. It will instantly spike your blood sugar levels. This will result in lethargy, inactiveness, and sleepiness. A person reflex becomes dull overtime and they lead an inactive life. To make things worse, junk food also clogs your arteries and increases the risk of a heart attack. Therefore, it must be avoided at the first instance to save your life from becoming ruined.The main problem with junk food is that people don’t realize its ill effects now. When the time comes, it is too late. Most importantly, the issue is that it does not impact you instantly. It works on your overtime; you will face the consequences sooner or later. Thus, it is better to stop now.You can avoid junk food by encouraging your children from an early age to eat green vegetables. Their taste buds must be developed as such that they find healthy food tasty. Moreover, try to mix things up. Do not serve the same green vegetable daily in the same style. Incorporate different types of healthy food in their diet following different recipes. This will help them to try foods at home rather than being attracted to junk food.In short, do not deprive them completely of it as that will not help. Children will find one way or the other to have it. Make sure you give them junk food in limited quantities and at healthy periods of time. '

# Encoding the inputs and passing them to model.generate()
inputs = tokenizer.batch_encode_plus([original_text],return_tensors='pt')
summary_ids = model.generate(inputs['input_ids'], early_stopping=True)
# Decoding and printing the summary
bart_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(bart_summary)






# Summarization with GPT-2 Transformers
# Importing model and tokenizer
from transformers import GPT2Tokenizer,GPT2LMHeadModel
# Instantiating the model and tokenizer with gpt-2
tokenizer=GPT2Tokenizer.from_pretrained('gpt2')
model=GPT2LMHeadModel.from_pretrained('gpt2')
# Encoding text to get input ids & pass them to model.generate()
inputs=tokenizer.batch_encode_plus([original_text],return_tensors='pt',max_length=512)
summary_ids=model.generate(inputs['input_ids'],early_stopping=True)
# Decoding and printing summary
GPT_summary=tokenizer.decode(summary_ids[0],skip_special_tokens=True)
print(GPT_summary)







# Summarization with XLM Transformers
# Importing model and tokenizer
from transformers import XLMWithLMHeadModel, XLMTokenizer
# Instantiating the model and tokenizer 
tokenizer=XLMTokenizer.from_pretrained('xlm-mlm-en-2048')
model=XLMWithLMHeadModel.from_pretrained('xlm-mlm-en-2048')
# Encoding text to get input ids & pass them to model.generate()
inputs=tokenizer.batch_encode_plus([original_text],return_tensors='pt',max_length=512)
summary_ids=model.generate(inputs['input_ids'],early_stopping=True)
# Decode and print the summary
XLM_summary=tokenizer.decode(summary_ids[0],skip_special_tokens=True)
print(XLM_summary)



ImportError: 
T5ForConditionalGeneration requires the PyTorch library but it was not found in your environment. Checkout the instructions on the
installation page: https://pytorch.org/get-started/locally/ and follow the ones that match your environment.

"""
