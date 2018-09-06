import pandas as pd
import numpy as np
from sklearn import preprocessing

c_range = np.arange(start=0.5, stop=2.05, step=0.05)
gamma_range = np.arange(start=0.001, stop=0.1001, step=0.001)

X = pd.read_csv('Datasets/parkinsons.data', index_col = 'name')
y = X['status']
X = X.drop('status', axis=1) # best_score = 0.915254237288

X = preprocessing.StandardScaler().fit_transform(X) # 0.932203389831
#X = preprocessing.MaxAbsScaler().fit_transform() # 0.881355932203
#X = preprocessing.MinMaxScaler().fit_transform(X) #0.881355932203
#X = preprocessing.Normalizer().fit_transform(X) # 0.796610169492
#X = preprocessing.scale(X) # 0.932203389831

#from sklearn.decomposition import PCA
#pca = PCA(n_components=10)
#pca.fit(X)
#X = pca.transform(X)

from sklearn import manifold
iso = manifold.Isomap(n_neighbors=4, n_components=5)
iso.fit(X)
X = iso.transform(X)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

from sklearn.svm import SVC

best_score = 0
for c_value in c_range:
    for gamma_value in gamma_range:
        model = SVC(kernel= 'rbf', C=c_value, gamma= gamma_value) #linear, poly, rbf
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        
        if score > best_score:
            best_score = score
        
print best_score