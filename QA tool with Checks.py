import pandas as pd
import csv
import numpy as np
import os
import datetime



'''
GOAL:
COMPARES METRICS BETWEEN TWO FILES [BASE AND COMP] 



Notes:
basefilemixed and compfilemixed are same as the OG but the palcements are moved around

step by step:
1 - PART 1 - user passes two files base and comp [e.g sql and ui file]
2 - PART 2 - user creates a mapping list to match which columns to compare
3 - PART 3 - creates a csv file and shows the campaign and the 

'''
# ## algos to keep in mind
# print(base_df.iloc[:,0]) ## first column where 0 indicats index




## user to pass two file paths
base_filename = r'basefile.xlsx'
comp_filename = r'compfile.xlsx'
base_mixed_file = r'basefile mixed.xlsx'
comp_mixed_file = r'compfilemixed.xlsx'

# have user pass csv files
base_csv = r'basefile mixed.csv'
comp_csv = r'compfilemixed.csv'


basefile_user_input = input('base filepath pls')
compfile_user_input = input('comp file path pls')

if compfile_user_input.endswith('.csv') and basefile_user_input.endswith('.csv') != True:
    print('please submit csv files')


## create data frame files
base_df = pd.read_csv(basefile_user_input)
comp_df = pd.read_csv(compfile_user_input)


## variables
base_df.shape[0],base_df.shape[1] ## row count, column count for fileA
comp_df.shape[0],comp_df.shape[1] ## row count, column count for fileB
base_columnList = list(base_df.columns.values) ## list of column headers in file A
comp_columnList = list(comp_df.columns.values) ## list of column headers in file B



## START PART 1; GET MAPPING LIST OF COLUMNS

print(f"base columns:\n"
      f"{base_columnList}")
print(f"comp columns:\n"
      f"{comp_columnList}")



## mapping columns between two files so we know which columns to compare
adding_columns = True
c_list = []
while adding_columns == True:
    print(f"select a column from the following: {base_columnList}\n")
    #user_select_base = input('select a column for base file from the above\n')
    user_select_base = input()
    if  user_select_base.lower() == 'q' and user_select_base not in base_columnList:
        adding_columns = False
        break
    print(f"select a column from the following: {comp_columnList}\n")
    #user_select_comp = input('select a column for comp file from above\n')
    user_select_comp = input()
    if user_select_comp.lower() == 'q' and user_select_comp not in comp_columnList:
        adding_columns = False
        break
    else:
        column_pair = user_select_base,user_select_comp
        column_pair = list(column_pair)
        c_list.append(column_pair)

## END PART 1; GET MAPPING LIST OF COLUMNS



## START PART 2; MATCH THE CAMPAIGN NAME AND PLAEMENTS NAMES BETWEEN TWO FILES,
## GET METRICS, MATH, THEN ADD DIFFS TO NEW MERGEDFILE

# # create csv file with two paramters to store combined dataframe
merged_df = pd.DataFrame(columns=["Campaign","Placement"])
# df['test'] = '' ## add column




## loop to pull decending index from c_list [aka c_list]


while len(c_list) != 0 :
    for index in range(0,base_df.shape[0]): ## loop through all rows of the base file
    # variables for each row for campaign and placement


        # base file variables
        base_campaign = base_df['Campaign'][index]
        base_placement = base_df['Placement'][index]


        # comp file variables
        comp_campaign = comp_df['Campaign'][index]
        comp_placement = comp_df['Placement'][index]


        # add campaign and placement name to the new DF
        merged_df.loc[base_df.index[index],'Campaign'] = base_campaign
        merged_df.loc[base_df.index[index],'Placement'] = base_placement

        ## values 0 and 1 from the column mapping list aka c_list
        base_column = c_list[0][0] # first value in first list pair in c_list
        comp_column = c_list[0][1] # second value in first list pair in c_list

        # get value for column [base_column] from comp_file
        value_to_compareTo = comp_df.loc[(comp_df['Campaign'] == base_campaign) & (comp_df['Placement'] == base_placement)][str(base_column)].values

        # get value for column [comp_column] from base_file
        base_column_value = base_df[base_column][index]

        # subtract to get the diff
        equals = int(base_column_value - value_to_compareTo)

        # add the column if it doesnt already exist in the file; and append the value from above [equals]
        merged_df.loc[index,base_column] = equals
    # remove the value at index[0] so script can move onto the next headers user wants to compare
    c_list.pop(0)

# create time stamp to append to filename
now = datetime.datetime.now()
timestamp = now.year, now.month, now.day, now.hour, now.minute, now.second
filename = os.path.dirname(basefile_user_input) + '\\' + 'MergedFile.csv' + timestamp
## save df to a csv file so use can open
merged_df.to_csv(filename,index=False)

