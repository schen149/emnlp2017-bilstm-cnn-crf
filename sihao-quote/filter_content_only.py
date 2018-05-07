'''
Only keep
'''
from sys import argv

if len(argv) != 3:
    print("Usage: python combine_dataset.py [conll-path] [output-path]")
    exit(1)

conll_path = argv[1]
outpath = argv[2]

with open(conll_path, 'r') as fin, open(outpath, 'w+') as fout:
    for line in fin:
        newline = line
        if line.rstrip():
            parts = line.split('\t')
            bio_label = parts[0]
            if bio_label.endswith("CUE") or bio_label.endswith("SOURCE"):
                parts[0] = "O"
                newline = "\t".join(parts)

            fout.write(newline)

