import csv
import json
import sys
from imp import reload

reload(sys)
base = '../data/'
csv_file = base + 'example-data-1.csv'
jl_file = base + 'example-data-1.jl'

headers = ["sNo","x1","x2","x3","x4","x5","y"]

fp = open(jl_file, 'w')
with open(csv_file) as csvfile:
    reader = csv.reader(csvfile, delimiter=',', escapechar='\\')
    x = 0
    s = 0
    for row in reader:
        try:
            map = {}
            print(x)
            print(s)
            i = 0
            x += 1
            for element in row:
                header = headers[i]
                try:
                    e = float(element)
                    map[header] = e
                except:
                    map[header] = element
                i += 1
            fp.write(json.dumps(map) + "\n")
            s += 1
        except:
            print(row)
fp.close()
