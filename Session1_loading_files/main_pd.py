import pandas as pd 
data = pd.read_csv('Session1_loading_files/fruits.txt',header=None)
data.columns = ['name', 'price', 'color']  # Assign column names
data['price_p10'] = data['price'] * 1.1  # Increase price by 10%
data['price_p20'] = data['price'] * 1.2  # Increase price by 20%



data.to_excel('Session1_loading_files/fruits3.xlsx',index=False)  # Save to Excel without index
