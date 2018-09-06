import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
csvTutorial = pd.read_csv('Datasets/tutorial.csv')
#print csvTutorial


# TODO: Print the results of the .describe() method
#
print csvTutorial.describe()



# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
#print csvTutorial.loc[2:4, 'col3']


