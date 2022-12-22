def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   s = data.split('\n')
   d = s[1].split(',')
   return d
# Read the csv file
f = open("data.csv", 'r')
a = f.read()
print(get_first_row(a))