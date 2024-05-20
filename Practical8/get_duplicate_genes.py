import os
import re
os.chdir("/Users/yun/Desktop/IBInotes")
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('duplicate_genes.fa', 'w')
sequence=[]
flag=1
for line in input_file:
    line = line.strip()
    if line.startswith('>'):
        if sequence and flag:
                output_file.write(''.join(sequence)+'\n')
                sequence=[]
        flag=1
        if re.search('duplication', line):
                genename_match=re.search(r'gene:(\w+)',line)
                if genename_match:
                    output_file.write(f'>{genename_match.group(1)}\n')
                    flag=0
        else:
                    sequence.append(line)

        if sequence and flag:
            output_file.write(''.join(sequence)+'\n')
