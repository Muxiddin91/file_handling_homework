f = open('txt_file/data01.txt').read().split(',')
def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(f)
# Read data from file
print(main(f))