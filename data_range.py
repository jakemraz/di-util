# remove 5-index field from test.csv
# python3 di-util.py test.csv rmfield 5
import csv
import math

def execute(filename, params):
        
    index = params[0]
    start_num = int(params[1])
    range_num = int(params[2])
    result = []
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row[index] = str(range_num * math.floor(int(row[index]) / range_num)) + '-' + str((range_num+1) * math.floor(int(row[index]) / range_num))
            result.append(row)
            
    return result
