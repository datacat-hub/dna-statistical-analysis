import matplotlib.pyplot as plt

# 1. Το DNA δείγμα (Μια αλληλουχία 100 χαρακτήρων)
dna_sequence = "ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"

# 2. Καταμέτρηση Συχνοτήτων (Στατιστική)
counts = {
    'Adenine (A)': dna_sequence.count('A'),
    'Thymine (T)': dna_sequence.count('T'),
    'Cytosine (C)': dna_sequence.count('C'),
    'Guanine (G)': dna_sequence.count('G')
}

# 3. Υπολογισμός % του GC-Content
total_length = len(dna_sequence)
gc_content = ((counts['Cytosine (C)'] + counts['Guanine (G)']) / total_length) * 100

print(f"Total Sequence Length: {total_length} bases")
print(f"GC-Content: {gc_content:.2f}%")

# 4. Δημιουργία Γραφήματος (Ραβδόγραμμα)
plt.figure(figsize=(7, 4))
plt.bar(counts.keys(), counts.values(), color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Nucleotide Frequency Distribution")
plt.ylabel("Count")
plt.show()
