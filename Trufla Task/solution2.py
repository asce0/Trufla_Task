import pandas as pd
import numpy as np

# at first i will combine the two csv files to make the parsing easier
customers = pd.read_csv(r"input_data\csv\customers.csv") #read the customers csv
vehicles = pd.read_csv(r"input_data\csv\vehicles.csv")   #read vehicles csv
#b = b.dropna(axis=1)

merged = pd.merge(customers, vehicles, left_on="id", right_on="owner_id", how="left") #merge the files by looking at the customer ID and the owner id
merged = merged.drop(columns="owner_id")
merged.to_csv("parsing_result\Csv_result\merged.csv", index=False) #generate the merged csv

df = pd.read_csv (r'parsing_result\Csv_result\merged.csv') # reading merged csv

#now i will iterat over each row in merged csv and parse it into Json file
for idx, group in df.groupby(np.arange(len(df))): 
    group.to_json(f'parsing_result\Csv_result\customer{idx+1}.json', orient='index')

