import csv

def read_csv_file(filename):
    f = open(filename, encoding = 'utf-8')
    for row in csv.reader(f):
        print(row)
    f.close


def read_csv_file_tabs(filename):
    f = open(filename, encoding = 'utf-8')
    for row in csv.reader(f):
        column = ''
        for col in range(0,len(row)):
            column = column + row[col] + '\t'
        print (column)
    f.close 


def write_list_to_csv(filename, list):
    f = open(filename, encoding = 'utf-8')
    for item in list:
        csv.writer(f).writerow(item)
    f.close


def write_one_row_to_csv(filename, content):
    f = open(filename, encoding = 'utf-8')
    csv.writer(f).writerow(content)
    f.close