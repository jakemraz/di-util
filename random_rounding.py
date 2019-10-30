# remove 5-index field from test.csv
# python3 di-util.py test.csv rmfield 5
import csv
import math

def execute(filename, params):
        
    index = params[0]
    round_position = int(params[1])
    before_round = math.pow(0.1, round_position)
    after_round = math.pow(10, round_position)
    result = []
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row[index] = int(math.floor(int(row[index]) * before_round) * after_round)
            result.append(row)
            
    return result
