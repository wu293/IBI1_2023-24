seq = "ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
import re
pattern1 = r'GTGTGT'
pattern2 = r'GTCTGT'
matches1 = re.finditer(pattern1, seq)
matches2 = re.finditer(pattern2, seq)
total = sum(1 for _ in matches1)+sum(1 for _ in matches2)
print("the total number of repeat elements is",total)
