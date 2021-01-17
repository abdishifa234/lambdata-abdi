from pandas import DataFrame
# write a function that tells the number of null values 
def null_count(df):     
   return df.isnull().sum().sum()

#Split addresses into three columns (df['city'], df['state'], and df['zip']) 
# def addy_split(add_series):     
#     df[len_str] = df['owner city state zip'].str.split(',').apply(len)    
#     df['num_commas'] = df['Owner City State Zip'].str.count(',')   
#     return df



#Return a new column with the full name from 
# a State abbreviation column -> An input of FL would return Florida



def add_state_names_column(my_df):
   '''
   add a column of corrsponding state names to a dataframe'

   Pramas (my_df) a DataFrame with a column called "abbrev" that has state abbrevations

   Return a copy of the original dataframe,but with an extra column.
   '''
   new_df=my_df.copy()

   names_map={"CA":"California","CO":"Cplorado","CT":"Conn"}

   new_df["name"]=new_df["abbrev"].map(names_map)

   breakpoint()

   return my_df

if __name__=="__main__":
   
   df=DataFrame({"abrev":["CA","CO","CT","DC","TX"]})

   print(df.head())
   
   add_state_names_column(my_df)
   print(df.head())