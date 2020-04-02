import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import csv
import os
from matplotlib import pyplot as plt
import numpy as np
 
def word_feats(words):
	return dict([(word, True) for word in words])

# Vocabulary for prediction
positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(' ]
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]
 
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
 
train_set = negative_features + positive_features + neutral_features
 
classifier = NaiveBayesClassifier.train(train_set) 


loop = True
while loop:
	print(
	'''
	1. Tweets from a csv file containing tweets by keyword
	2. Your sentence
	3. Exit
	'''
	)
	user_input = input('Your input: ')

	if int(user_input) == 2:
		# Predict
		neg = 0
		pos = 0
		neu = 0
		sentence = input('Enter a sentence: ')
		sentence = sentence.lower()
		words = sentence.split(' ')
		for word in words:
			classResult = classifier.classify(word_feats(word))
			if classResult == 'neg':
				neg = neg + 1
			if classResult == 'pos':
				pos = pos + 1
			if classResult == 'neu':
				neu = neu + 1
		print('Positive: ' + str(float(pos)/len(words)))
		print('Negative: ' + str(float(neg)/len(words)))
		print('Neutral: ' + str(float(neu)/len(words)))
	elif int(user_input) == 3:
		loop = False
	elif int(user_input) == 1:
		result = {}
		if os.path.isfile('./tweetbykeyword.csv'):
			my_csv_file =  open('tweetbykeyword.csv', 'r')
			reader = csv.DictReader(my_csv_file)
			for each_row in reader:
				words = each_row['Tweets'].split(' ')
				keyword = each_row['Keyword']
				if keyword in result:
					neg = 0
					pos = 0
					neu = 0
					for word in words:
						classResult = classifier.classify(word_feats(word))
						if classResult == 'neg':
							neg = neg + 1
						if classResult == 'pos':
							pos = pos + 1
						if classResult == 'neu':
							neu = neu + 1
					up_pos = float(pos)/len(words) + int(result[keyword]['Positive_Tweets'])
					up_neg = float(neg)/len(words) + int(result[keyword]['Negative_Tweets'])
					up_neu = float(neu)/len(words) + int(result[keyword]['Neutral_Tweets'])
					result[keyword] = {'Positive_Tweets': up_pos, \
									   'Negative_Tweets': up_neg, \
									   'Neutral_Tweets': up_neu}
				else:
					# Predict
					neg = 0
					pos = 0
					neu = 0
					for word in words:
						classResult = classifier.classify(word_feats(word))
						if classResult == 'neg':
							neg = neg + 1
						if classResult == 'pos':
							pos = pos + 1
						if classResult == 'neu':
							neu = neu + 1
					result[keyword] = {'Positive_Tweets': float(pos)/len(words), \
									   'Negative_Tweets': float(neg)/len(words), \
									   'Neutral_Tweets': float(neu)/len(words)}
			with open('ResultByKeyword.csv', 'w') as my_csv_file:
				field_names = ['Keyword', 'Positive_Tweets', 'Negative_Tweets', \
							   'Neutral_Tweets']
				writer = csv.DictWriter(my_csv_file, fieldnames = field_names)
				writer.writeheader()
				for key, value in result.items():
					writer.writerow({'Keyword': key, 'Positive_Tweets': value['Positive_Tweets'], \
									 'Negative_Tweets' : value['Negative_Tweets'], \
									 'Neutral_Tweets': value['Neutral_Tweets']})
		else:
			print('Input file does not exist')
	else:
		print('Please enter 1, 2 or 3')
