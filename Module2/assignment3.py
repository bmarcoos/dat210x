import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
dsServo = pd.read_csv('Datasets/servo.data', header= None, names=['motor', 'screw', 'pgain', 'vgain', 'class'])
#print dsServo


# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#

dfFiltered = dsServo.vgain[dsServo.vgain == 5]

print len(dfFiltered)


# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..

dfFiltered2 = dsServo[(dsServo.motor == 'E') & (dsServo.screw == 'E')]

print len(dfFiltered2)

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
dfFiltered3 = dsServo[dsServo.pgain == 4]

print dfFiltered3.vgain.mean()


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!

print dsServo.dtypes

