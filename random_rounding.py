# remove 5-index field from test.csv
# python3 di-util.py test.csv rmfield 5
import csv
import math

def execute(filename, params):
        
    index = params[0]
    round_position = params[1]
    result = []
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row[index], -1 * int(round_position))
            row[index] = round(int(row[index]), -1 * int(round_position))
            result.append(row)
            
    return result

    
    # new_lines = ''
    # for line in lines:
    #     line = line.replace('\n','')
    #     record = line.split(',')
    #     if len(record) <= index:
    #         break
    #     del record[index]
    #     new_line = ','.join(record)
    #     new_lines = ''.join([new_lines, new_line,'\n'])
        

#     return new_lines





