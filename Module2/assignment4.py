import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
#dsNHL= pd.read_html("http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2")[0]
dsNHL = pd.read_html("Datasets/2014-15 NHL Hockey Stats and League Leaders - Points - National Hockey League - ESPN.htm")[0]
print len(dsNHL)
# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
cols = ['RK','PLAYER','TEAM','GP','G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','G','A','G','A']
dsNHL.columns = cols

# TODO: Get rid of any row that has at least 4 NANs in it
#
dsNHL['countNull'] = dsNHL.isnull().sum(axis=1)
dsNHL = dsNHL[dsNHL.countNull < 4]

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#

dsNHL = dsNHL[dsNHL.notnull().any(axis=1)]

print len(dsNHL)



# TODO: Get rid of the 'RK' column
#
dsNHL = dsNHL.drop('countNull', axis=1)
dsNHL = dsNHL.drop('RK', axis=1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#

dsNHL = dsNHL[dsNHL.PLAYER != 'PLAYER']
dsNHL = dsNHL.reset_index(drop=True)



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print len(dsNHL['PCT'].unique())

dsNHL.GP = pd.to_numeric(dsNHL.GP, errors='coerce')
print dsNHL.dtypes
print dsNHL['GP'].loc[15:16].sum()