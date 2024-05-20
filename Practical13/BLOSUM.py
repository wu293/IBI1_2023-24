import blosum as bl
import os

# Load the BLOSUM62 matrix
matrix = bl.BLOSUM(62)

os.chdir("/Users/yun/Desktop/IBInotes")

# Read sequences from the file
def get_sequence(filename):
    with open(filename, 'r') as file:
        sequence = ""
        for line in file:
            if line.startswith(">"):
                continue
            sequence += line.strip().replace("\n", "")
    return list(sequence)

seq_human = get_sequence('SLC6A4_HUMAN.fa')
seq_mouse = get_sequence('SLC6A4_MOUSE.fa')
seq_rat = get_sequence('SLC6A4_RAT.fa')

# Calculate score and percentage identity
def compare_sequences(seq1, seq2):
    score = 0
    identical = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += matrix[aa1][aa2]
        if aa1 == aa2:
            identical += 1
    percentage_identity = (identical / len(seq1)) * 100
    return score, percentage_identity

# Compare sequences and print results
def print_comparison(seq1, seq2, name1, name2):
    score, percentage = compare_sequences(seq1, seq2)
    print(f"{name1} vs {name2} BLOSUM score: {score}, identity percentage: {percentage:.2f}%")

print_comparison(seq_human, seq_mouse, "Human", "Mouse")
print_comparison(seq_human, seq_rat, "Human", "Rat")
print_comparison(seq_mouse, seq_rat, "Mouse", "Rat")
