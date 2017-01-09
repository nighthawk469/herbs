'''
open file
create current datetime
create some random values
close file
'''
from datetime import datetime
from random import randint
from time import sleep


def main():
    while True:
        f = open('data.csv', 'a')
        data = "{} , {}".format(datetime.now(), str(randint(1,10)))
        print(data, file=f)
        print(data)

        f.close()

        sleep(1)


if __name__ == "__main__":
    main()




'''
-a csv file containing only 10 entries
if there are more than 10 lines in the file
    delete the first line (will that pull the rest of the lines up?)
    append next line
'''




