f = open('txt_file/data01.txt')
a=f.read()
b=a.split(',')
def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return b
print(main(a))
# Read data from file