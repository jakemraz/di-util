from __future__ import print_function
import sys
import module1
import rmfield

def main():

    filename = sys.argv[1]
    cmd = sys.argv[2]

    #lines = locals()['rmfield'].execute(sys.argv)

    # python3 di-util.py test.csv rmfield 0
    if (cmd == 'rmfield'):
        lines = rmfield.execute(sys.argv)
    # add code here



    output_filename = 'newfile.csv'

    with open(output_filename,'w') as file:
        file.writelines(lines)

    pass


# python3 di-util.py <data.csv> <aggregation> 
if __name__ == "__main__":
    main()