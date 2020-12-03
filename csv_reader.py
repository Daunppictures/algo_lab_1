from pool import Pool
import csv


def read_csv_file(file_name):
    pools = []
    with open(file_name, 'r')  as file:
        reader = csv.reader(file)

        for row in reader:
            pools.append(Pool(row[0], int(row[1]), int(row[2])))

    return pools
