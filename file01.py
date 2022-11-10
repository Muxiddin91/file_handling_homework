f = open('txt_file/data01.txt').read().split(',')
l1 = []
for i in f:
    a=int(i)
    l1+=[a]
def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    return l1
print(main(f))
# Read data from file