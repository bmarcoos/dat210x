import pandas as pd
import numpy as np


# TODO:
# Load up the dataset, setting correct header labels
# Use basic pandas commands to look through the dataset...
# get a feel for it before proceeding!
# Find out what value the dataset creators used to
# represent "nan" and ensure it's properly encoded as np.nan
#
myCols = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']
df = pd.read_csv('Datasets/census.data', header= None, names=myCols)

df = df.replace('NAN',np.nan).replace('NaN',np.nan).replace('Nan',np.nan).replace('nan',np.nan)


# TODO:
# Figure out which features should be continuous + numeric
# Conert these to the appropriate data type as needed,
# that is, float64 or int64
#
print df.dtypes


# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal types using
# the method discussed in the chapter.
#
# .. your code here ..

#print df.education.unique()
list_education = ['1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th',
                  'Preschool', 'HS-grad', 'Some-college', 'Bachelors', 'Masters', 'Doctorate']

df.education = df.education.astype("category",
  ordered=True,
  categories=list_education
).cat.codes


# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any nominal types by
# exploding them out to new, separate, boolean fatures.
#
df = pd.get_dummies(df,columns=['sex','race','classification'])

print df.columns
# TODO:
# Print out your dataframe
