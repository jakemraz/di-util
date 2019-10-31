# remove 5-index field from test.csv
# python3 di-util.py test.csv rmfield 5
import csv
import math


def execute(filename, params):
    index = params[0]
    start_num = int(params[1])
    range_num = int(params[2])
    result = []
    print(index, start_num, range_num)

    statistics = {}

    # i = 0
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
        #     if row[index] == "0":
        #         row[index] = "0"
        #         result.append(row)
        #         if str("0") in statistics:
        #             statistics["0"] += 1
        #         else:
        #             statistics["0"] = 1
        #         continue

            from_num = str(range_num * int(math.floor(int(row[index]) / range_num)))
            # if range_num * int(math.floor(int(row[index]) / range_num)) == 0:
            #     from_num = str("1")
            to_num = str(range_num * int(math.floor(int(row[index]) / range_num)) + range_num)

            # print(row[index], from_num)

            max_num = "250000000"
            if int(from_num) >= int(max_num):
                row[index] = ">="+max_num
                result.append(row)
                if str(max_num) in statistics:
                    statistics[max_num] += 1
                else:
                    statistics[max_num] = 1
                continue

            row[index] = '[' + from_num + ', ' + to_num + '['
            result.append(row)

            if str(from_num) in statistics:
                statistics[from_num] += 1
            else:
                statistics[from_num] = 1
            # i += 1
            # if i == 100:
            #     break

    print(statistics)

    return result
