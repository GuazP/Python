# /usr/bin/python3

from collections import defaultdict
 
def main():
    print(count_grouped_by_genre("game_stat.txt"))
    print(count_grouped_by_genre2("game_stat.txt"))

def count_grouped_by_genre(file_name):
    result_dict = defaultdict(list)
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            game, number, date, genre, company = line.split('\t')
            result_dict[genre].append(game) 
    return dict(result_dict)

def count_grouped_by_genre2(file_name):
    resultDict = {} 
    with open(file_name, 'rt') as file:
        for line in file.readlines():
            line = line.split("\t")
            key = line[3]
            resultDict[key] = resultDict.get(key, 0) + 1
    return resultDict

if __name__ == "__main__":
    main()
