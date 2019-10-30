from __future__ import print_function
import sys
import rmfield
import random_rounding
import data_range
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
    
    # 13. 랜덤 라운딩 -> 정수형 숫자를 내림 ex)1964 -> 1960 or 1900
    if (cmd == 'random_rounding'):
        if (len(params) == 0):
            print('random_rounding needs more params : <index_field_name ex:name> <round position ex:2>')
            exit()
        result = random_rounding.execute(filename, params)
        
    # 14. 범위 방법 -> 수치 데이터를 범위로 설정 ex)3,300만원 ->3,000만원~4,000만원
    if (cmd == 'data_range'):
        if (len(params) == 0):
            print('data_range needs more params : <index_field_name ex:name> <start_num> <range_num>')
            exit()
        result = data_range.execute(filename, params)
        

    with open('result.csv', 'w', newline='') as csvfile:
        fieldnames = result[0]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in result:
            writer.writerow(row)
        

# python3 di-util.py <data.csv> <aggregation> 
if __name__ == "__main__":
    main()