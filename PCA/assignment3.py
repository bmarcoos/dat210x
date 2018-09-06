import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper

# Look pretty...
matplotlib.style.use('ggplot')

# Do * NOT * alter this line, until instructed!
scaleFeatures = True # False

df = pd.read_csv('Datasets/kidney_disease.csv')
df = df.dropna()

labels = ['red' if i=='ckd' else 'green' for i in df.classification]

#df = df.drop(['id', 'classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'], axis=1)

df['wc'] = pd.to_numeric(df['wc'], errors='coerce')
df['rc'] = pd.to_numeric(df['rc'], errors='coerce')
df['pcv'] = pd.to_numeric(df['pcv'], errors='coerce')


################
df = df.drop(['id', 'classification'], axis=1)
df = pd.get_dummies(df, prefix=['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'])
print df
#################

df['wc'] = pd.to_numeric(df['wc'], errors='coerce')
df['rc'] = pd.to_numeric(df['rc'], errors='coerce')
df['pcv'] = pd.to_numeric(df['pcv'], errors='coerce')

print df.dtypes


if scaleFeatures: df = helper.scaleFeatures(df)

print df['bgr'].var()
print df['wc'].var()
print df['rc'].var()


from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(df)
T = pca.transform(df)

ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()
