# remove 5-index field from test.csv
# python3 di-util.py test.csv rmfield 5

def execute(args):
    # print('call rmfield ' + args)
    filename = args[1]
    index = int(args[3])

    with open(filename, "r") as file:
        lines = file.readlines()
    
    new_lines = ''
    for line in lines:
        line = line.replace('\n','')
        record = line.split(',')
        if len(record) <= index:
            break
        del record[index]
        new_line = ','.join(record)
        new_lines = ''.join([new_lines, new_line,'\n'])
        

    return new_lines





