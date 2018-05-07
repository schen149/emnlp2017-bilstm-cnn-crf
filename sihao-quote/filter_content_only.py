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
        if line.rstrip():
            _parts = line.split('\t')
            parts = [_parts[0], _parts[5].lstrip()]
            bio_label = parts[0]
            if bio_label.endswith("CUE") or bio_label.endswith("SOURCE"):
                parts[0] = "O"

            newline = "\t".join(parts) + '\n'
        else:
            newline = line

        fout.write(newline)


