'''
    Combine multiple conll files into one giant file
'''

from os import listdir
from sys import argv

if len(argv) != 3:
    print("Usage: python combine_dataset.py [conll-dir] [output-path]")
    exit(1)

conll_dir = argv[1]
out_path = argv[2]

conll_files = listdir(conll_dir)

with open(out_path, 'w+') as fout:
    for _f in conll_files:
        f = conll_dir + '/' + _f
        with open(f, 'r') as fin:
            for line in fin:
                if line.rstrip():
                    parts = line.split("\t")
                    if parts[4] == "-X-":
                        continue
                fout.write(line)
            print("Processed:\t" + f)

