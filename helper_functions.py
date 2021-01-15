# write a function that tells the number of null values 
def null_count(df):     
   return df.isnull().sum().sum()

#Split addresses into three columns (df['city'], df['state'], and df['zip']) 
def addy_split(add_series):     
    df[len_str] = df['owner city state zip'].str.split(',').apply(len)    
    df['num_commas'] = df['Owner City State Zip'].str.count(',')   
    return df