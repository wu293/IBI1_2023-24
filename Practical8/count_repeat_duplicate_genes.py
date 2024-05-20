import re

def count_repeat_duplicate_genes(inputfile, outputfile):
    with open(inputfile, 'r') as input_fasta, open(outputfile, 'w') as output_fasta:
        sequence = []
        repeat_pattern = re.compile(r'(GTGTGT|GTCTGT)')  
        flag=1

        for line in input_fasta:
            line = line.strip()
            if line.startswith('>'):
                if sequence and flag:
                        output_fasta.write(''.join(sequence) + '\n')
                        sequence = []
                        flag=1
               
                if re.search('duplication', line):
                    genename_match = re.search(r'gene:(\w+)', line)
                    if genename_match:
                        gene_name = genename_match.group(1)                        
                        repeat_count = len(repeat_pattern.findall(''.join(sequence)))                    
                        new_gene_name = f"{gene_name}_{repeat_count}"
                        output_fasta.write(f">{new_gene_name}\n")
                        flag=0
            else:
                sequence.append(line)

        if sequence and flag:
            output_fasta.write(''.join(sequence) + '\n')

# Prompts the user enter a repeat sequence
repeat_sequence = input("Please enter one of the repetitive sequences ('GTGTGT' or 'GTCTGT'): ")
if repeat_sequence not in ['GTGTGT', 'GTCTGT']:
    print("Invalid sequence entered.")
else:
    output_filename = f"{repeat_sequence}_duplicate_genes.fa"
    count_repeat_duplicate_genes('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', output_filename)
