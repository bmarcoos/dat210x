import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import random, math

# Look pretty...
matplotlib.style.use('ggplot')

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples= []
colors= []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
import os
folder_dir = os.path.dirname(os.path.realpath(__file__)) + r'/Datasets/ALOI/32/'

for png_name in os.listdir(folder_dir):        
    im = misc.imread(folder_dir + png_name)
    samples.append(im.ravel()) ## to flatten out the image array 
    colors.append('b')

##########################second part################################
folder_dir = os.path.dirname(os.path.realpath(__file__)) + r'/Datasets/ALOI/32_i/'

for png_name in os.listdir(folder_dir):
    if png_name[-3:] == 'png':
        im = misc.imread(folder_dir + png_name)
        samples.append(im.ravel()) ## to flatten out the image array 
        colors.append('r')
####################################################################


df = pd.DataFrame(samples)

from sklearn import manifold
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
T = iso.transform(df)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('ISOMAP 2D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.scatter(T[:,0], T[:,1], c= colors, marker='.', alpha=0.75)

'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('ISOMAP 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(T[:,0], T[:,1], T[:,2], c=colors, marker='.', alpha=0.7)
'''
#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 

##DONE IN SECOND PART


#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 

##DONE IN SECOND PART



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 



#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 




#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

