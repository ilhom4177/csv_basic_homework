def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
    d = data.split('\n')
    d1 = d[1].split(',')
   return d1
# Read the csv file