import os

os.system('clear')

with open('console_games.csv', 'r') as csv_file:
    print(csv_file.readline())

    for line in csv_file.readline():
        print(line)