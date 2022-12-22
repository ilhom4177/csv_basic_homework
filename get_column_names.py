#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    l=data.split('\n') 
    return l[0].split(',')
f=open('data.csv','r')
s=f.read()
print(get_column_names(s))
    
# Read the csv file