# remove 5-index field from test.csv
# python3 di-util.py test.csv rmfield 5
import csv
import collections

def execute(filename, params):
        
    result = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
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





