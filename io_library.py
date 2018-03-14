import csv

def read_data(filename):
    with open(filename, "rb") as csvfile:
        return list(csv.reader(csvfile))
