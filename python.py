# Import Libraries: 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("folder/filename.csv")
pd.read_csv('file_name.csv', usecols= ['column_name1','column_name2']) # subset of columns

"""VIEW DATA"""
display(data)
head(data)
data.info() # display number rows, columns
len(df) # get number of rows
len(df.columns) # get number of columns
df.shape # get number rows and columns
df.size # get number of elements



"""INSPECT DATA"""
# 1. Check data types of each column
data.dtypes 
# 2. Check the length of each column
len(data) # rows
# (b) Get column names
list_names = results.columns.names
# get unique values
len(pd.unique(data["column"])) # data 
# (b) Count non-missing observations
n_nonmiss = results["points"].count()

# summary statistics
data.describe()
print(data["column"].describe())
data["column"].dtype

"""Create new dataframe"""
# Filter subset of rows
lower_value          = 20
subset_row_text      = races.query('name == "Australian Grand Prix"')
subset_row_ineq      = results.query('(points >= 20) & (points <= 30)')
subset_row_global    = results.query('(points >= @lower_value)')
subset_row_colspaces = results.query('(`points col` >= @lower_value)')

# Extract specific columns for new dataframe
data[["columnOne", "columntwo"]]

# Rename columns
dictionary_rename = {'oldName': "newName"}
data = data.rename(columns = dictionary_rename)
# rename in one line
data = data.rename({'oldName': "newName"})
# 2. Problem: String intead of Numerical column
subset = data.query("columnName.str.isnumeric()==False") #.str (not a )
list_unique = pd.unique(subset["column"]) # list of unique values from list
data["column"] = data["column"].replace([list_oldValues], [list_newValues])
data["column"] = pd.to_numeric(data["column"]) # converts to numeric
# Replace values
results   = results.replace(to_replace = ["UK","USA"],
                            value = ["United Kingdom","United States"])

# Groupby and Aggregate ('column name', 'function name')
teamrace_agg = (results.query("raceId >= 200")
                        .groupby(["raceId","constructorId"])
                       .agg(mean_points = ('points','mean'),
                            sd_points =   ('points','std'),
                            min_points =  ('points','min'),
                            max_points =  ('points','max'),
                            count_obs   = ('points',len))
                        .sort_values(by="mean_points", ascending = False))


# Store cleaned dataset
data.to_csv("folder/fileName.csv")

"""GENERATE NEW COLUMN"""
# 1. Based on interval: 
bins_grades = [0, 54, 59, 64, 69, 74, 79, 82, 86, 92, 100]
labels_grades = ["F", "D", "C-", "C", "C+", "B-", "B", "B+", "A-", "A"]
students["lettergrade"] = pd.cut(students["numericgrade"],
                                bins = bins_grades,
                                right = True,
                                labels = labels_grades)

# 2. Merge - only merge needed columns
results_merge = pd.merge(results_primarydataset,
                         teamrace_agg_secondarydataset,
                         on = ["raceId", "constructorId"], # common variables
                         how = "left") # left dataset is primary one
dict_rename_races = {"name_x": "race_name", 
                    "name_y" : "circuit_name"} # must rename common names (python automatically add _x and _y)

# 3. Query than cocatenate data back together:
circuits_usa   = circuits.query('country == "United States" | country == "USA"')
circuits_malaysia = circuits.query('country == "Malaysia"')
circuits_concat = pd.concat([circuits_malaysia,circuits_usa])


# NaN (not a number)
# operations (+-*/) will return NaN
# summary statistics np.mean() does not work, np.nanmean() ignores NaN