# Predicting Toxicity of Agrochemicals to Honey Bees 🧪🐝
# che1147-bees 

## Data Preparation

*Data Cleaning*
The ApisTox dataset does not include any missing or redundant values in the rows or columns.

*Featurization*
Hashed fingerprints are used as the sole features for the model. These are generated using the RDKit Morgan Fingerprint generator with radius = 2 and fingerprint size = 2048 bits, and then added to the dataframe as columns. 

*Feature Selection:* 
The columns of containing Morgan bits with zero variance in the training set are removed from both the training and test sets respective to their split. Consequently, the datasets corresponding to the random, maxmin, and time splits will have differing numbers of features. The random split datasets have 1948 features, the maxmin split datasets have 1914, and the timesplit datasets have 1907. This quirk leads to needing to use a separate variable representing the features for each dataset. To call the features, the random split, maxmin split, and time split datasets use 'random_features', 'maxmin_features', and 'time_features', respectively. 

The rationale behind removing zero variance columns from the splits (as opposed to removing them from the initial dataset and then splitting) is that it is more important to reduce dimensionality in the training datasets than it is for all the split types to have the exact same features. A particular column may have a bit 'on' in the overall model (ie. having non-zero variance), but this particular bit may not be 'on' in a given training split (ie. having zero variance) by pure chance. This problematic scenario is plausible, as fingerprint representations are relatively sparse: the number of bits 'on' per column is generally quite low.
