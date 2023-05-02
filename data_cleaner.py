import pandas as pd
import numpy as np

df = pd.read_csv('city_bor_rough.csv')

print(df)

clean_df = pd.DataFrame(columns=['City', 'Borough'])

counter = 0
for index, row in df.iterrows():
    if counter == 0 and isinstance(row['Cities'], str):
        if row['Cities'] == 'East New York':
            clean_df.loc[len(clean_df)] = ['New York', 'Manhattan']
        else:
            clean_df.loc[len(clean_df)] = [row['Cities'], 'Brooklyn']
    elif counter == 1 and isinstance(row['Cities'], str):
        clean_df.loc[len(clean_df)] = [row['Cities'], 'Bronx']
    elif counter == 2 and isinstance(row['Cities'], str):
        clean_df.loc[len(clean_df)] = [row['Cities'], 'Manhattan']
    elif counter == 3 and isinstance(row['Cities'], str):
        if row['Cities'] == 'North Corona' or row['Cities'] == 'South Corona':
            clean_df.loc[len(clean_df)] = ['Corona', 'Queens']
        clean_df.loc[len(clean_df)] = [row['Cities'], 'Queens']
    elif counter == 4 and isinstance(row['Cities'], str):
        clean_df.loc[len(clean_df)] = [row['Cities'], 'Staten Island']
    counter += 1

    if counter > 4:
        counter = 0
clean_df.loc[len(clean_df)] = ['Bronx', 'Bronx']
clean_df.loc[len(clean_df)] = ['Brooklyn', 'Brooklyn']
clean_df.loc[len(clean_df)] = ['Staten Island', 'Staten Island']
clean_df.loc[len(clean_df)] = ['South Richmond Hill', 'Queens']
clean_df.loc[len(clean_df)] = ['Rockaway Beach', 'Queens']
clean_df.loc[len(clean_df)] = ['Saint Albans', 'Queens']
clean_df.to_csv('city_bor.csv', index=False)
