def print_basic_info(data):
    print(f'type of the data is: {type(data)}')
    print(f'number of rows in the data is: {data.shape[0]}')
    
    try:
        print(f'number of all columns in the data is: {data.shape[1]}')
    except:
        print('This data has just 1 column') # data is one dimensional
