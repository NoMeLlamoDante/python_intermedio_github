import os

os.system('clear')


with open('console_games.csv', 'r') as csv_file:
    #print(csv_file.readline())
    # lista
    # print(csv_file.readlines())
    #print(type(csv_file.readlines()))
    print(len(csv_file.readlines()))
#    for line in csv_file.readline():
#        print(line)
