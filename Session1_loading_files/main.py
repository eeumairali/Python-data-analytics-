file = open(r'Session1_loading_files\fruits.txt', mode='r') # open the file in read mode
fruits = file.readlines()
empty_data = ''
for fruit in fruits:
    fruit = fruit.strip() # Remove any leading/trailing whitespace
    name,price,color = fruit.split(',') # Split the line into name, price, and color
    empty_data += f'{name}, {round(float(price)*1.1,2)}, {color}\n' # Format the data


file2 = open(r'Session1_loading_files\fruits2.txt', mode='w') # open the file in write mode
file2.write(empty_data) # Write the formatted data to the new file
    
file.close()
file2.close() # Close the files