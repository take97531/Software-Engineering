import csv
import os
from matplotlib import pyplot as plt
import numpy as np

loop = True

while loop:
	print(
	'''
	1. Visualize tweets by keyword
	2. Exit
	'''
	)
	user_input = input('Your input: ')
	if int(user_input) == 1:
		if os.path.isfile('./ResultbyKeyword.csv'):
			result = {}
			with open('ResultByKeyword.csv', 'r') as my_csv_file:
				reader = csv.DictReader(my_csv_file)
				for each_row in reader:
					result[each_row['Keyword']] = {'Positive_Tweets': each_row['Positive_Tweets'], \
													'Negative_Tweets': each_row['Negative_Tweets'], \
													'Neutral_Tweets': each_row['Neutral_Tweets']}
			for key, value in result.items():
				labels = ('Positive Tweets', 'Negative Tweets', 'Neutral Tweets')
				y_pos = np.arange(len(labels))
				types_of_tweets = [value['Positive_Tweets'], value['Negative_Tweets'], \
									 value['Neutral_Tweets']]
				plt.bar(y_pos, types_of_tweets, align = 'center', alpha = 0.5)
				plt.xticks(y_pos, labels)
				plt.ylabel(key)
				plt.title('Tweets Plot')
				plt.show()
		else:
			print('Input file does not exist')
	elif int(user_input) == 2:
		loop = False
	else:
		print('Please enter 1 or 2')

	