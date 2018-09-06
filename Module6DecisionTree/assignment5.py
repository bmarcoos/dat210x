import pandas as pd


#https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names


# 
# TODO: Load up the mushroom dataset into dataframe 'X'
# Verify you did it properly.
# Indices shouldn't be doubled.
# Header information is on the dataset's website at the UCI ML Repo
# Check NA Encoding
#
# .. your code here ..

col_names = ['classification','cap-shape','cap-surface','cap-color','bruises?','odor','gill-attachment','gill-spacing',
             'gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring',
             'stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color',
             'population','habitat']

X = pd.read_csv('Datasets/agaricus-lepiota.data', header = None, names= col_names, na_values='?')
#print X.iloc[7410]


# INFO: An easy way to show which rows have nans in them
#print X[pd.isnull(X).any(axis=1)]

print X.shape

# 
# TODO: Go ahead and drop any row with a nan
#
# .. your code here ..
#X = X.dropna()

X = X.dropna(axis=0)
print X.shape


#
# TODO: Copy the labels out of the dset into variable 'y' then Remove
# them from X. Encode the labels, using the .map() trick we showed
# you in Module 5 -- canadian:0, kama:1, and rosa:2
#
# .. your code here ..
y = X['classification']
y = y.map({'p':1, 'e':0})
X = X.drop('classification', axis = 1)

#
# TODO: Encode the entire dataset using dummies
#
# .. your code here ..


X = pd.get_dummies(X)

# 
# TODO: Split your data into test / train sets
# Your test size can be 30% with random_state 7
# Use variable names: X_train, X_test, y_train, y_test
#
# .. your code here ..

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=7)

#
# TODO: Create an DT classifier. No need to specify any parameters
#
# .. your code here ..

from sklearn import tree
dtree = tree.DecisionTreeClassifier()
 
#
# TODO: train the classifier on the training data / labels:
# TODO: score the classifier on the testing data / labels:
#
# .. your code here ..

dtree.fit(X_train, y_train)
score= dtree.score(X_test, y_test)

print "High-Dimensionality Score: ", round((score*100), 3)

print X.columns[22]
print X.columns[31]


#
# TODO: Use the code on the courses SciKit-Learn page to output a .DOT file
# Then render the .DOT to .PNGs. Ensure you have graphviz installed.
# If not, `brew install graphviz`.
#
# .. your code here ..
import os
folder_dir = os.path.dirname(os.path.realpath(__file__))

from sklearn.externals.six import StringIO
import pydot
'''
with open(folder_dir + "/iris.dot", 'w') as f:
    f = tree.export_graphviz(dtree, out_file=f)
    os.unlink('iris.dot')
'''

from IPython.display import Image

with open(folder_dir + "/mushroom.dot", 'w') as f:
    dot_data = StringIO() 
    tree.export_graphviz(dtree, out_file=dot_data)
    graph = pydot.graph_from_dot_data(dot_data.getvalue())[0]
    #graph.write_pdf("mushroom.pdf")
    
    Image(data=graph.create_png())  

