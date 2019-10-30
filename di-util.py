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
    
    # 13. 랜덤라운딩
    if (cmd == 'random_rounding'):
        if (len(params) == 0):
            print('random_rounding needs more params : <filename.csv> <command> <index ex:0> <round position ex:2>')
            exit()
        result = random_rounding.execute(filename, params)
        
    print(result)
        

    with open('result.csv', 'w', newline='') as csvfile:
        fieldnames = result[0]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in result:
            writer.writerow(row)
        

#     output_filename = 'newfile.csv'

#     with open(output_filename,'w') as file:
#         file.writelines(lines)

#     pass


# python3 di-util.py <data.csv> <aggregation> 
if __name__ == "__main__":
    main()