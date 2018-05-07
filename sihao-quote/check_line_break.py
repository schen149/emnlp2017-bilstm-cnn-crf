from sys import argv

if len(argv) != 2:
    print("Usage: python check_line_break.py [text-file]")
    exit(1)

with open(argv[1], 'r') as fin:
    for line in fin:
        sline = line.strip()
        if len(sline) == 0:
            print(repr(line) + "\t" + str(len(sline)))