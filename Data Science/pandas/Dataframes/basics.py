import pandas as pd

# Creating Series
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
# Creating Dataframe                        
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print(df.head())

# Querying the dataframe:
print(df.loc['Store 2'])

# Selecting a column
df_copy = df.T.copy()
print(df_copy.loc['Cost'])

# Selecting from a column and a row
print(df.loc['Store 1']['Cost'])

# Dropping a row.
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print(copy_df)




