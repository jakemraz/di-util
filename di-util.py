from __future__ import print_function
import sys
import rmfield
import random_rounding
import csv

def main():

    filename = sys.argv[1]
    cmd = sys.argv[2]
    params = sys.argv[3:]

    #lines = locals()['rmfield'].execute(sys.argv)

    # python3 di-util.py test.csv rmfield 0
    if (cmd == 'rmfield'):
        lines = rmfield.execute(sys.argv)
    # add code here
    
    # 13. 랜덤라운딩 -> 반올림으로 일단
    if (cmd == 'round'):
        if (len(params) == 0):
            print('round needs more params : <filename.csv> <command> <index_field_name ex:name> <round position ex:2>')
            exit()
        result = random_rounding.execute(filename, params)
        

    with open('result.csv', 'w', newline='') as csvfile:
        fieldnames = result[0]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in result:
            writer.writerow(row)
        

# python3 di-util.py <data.csv> <aggregation> 
if __name__ == "__main__":
    main()