def translate_mRNA_to_polypeptide(mRNA_sequence):
    
    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

    polypeptide_sequence = ''
   
    for i in range(0, len(mRNA_sequence), 3):
        codon = mRNA_sequence[i:i+3]
        
        
        if codon_table[codon] == 'STOP':
            break  
        else:
            polypeptide_sequence += codon_table[codon]

    return polypeptide_sequence


mRNA_sequence = "AAGGCGCUAUGUUUCAGCCGAGAAGCUUGCGUGAAGAAGGAGGAGCGCUAA"
polypeptide_sequence = translate_mRNA_to_polypeptide(mRNA_sequence)
print("mRNA Sequence:", mRNA_sequence)
print("")
print("Polypeptide Sequence:", polypeptide_sequence)
print("")
print("The abrreviation and the names of the amino acids are: A= Alanine, R= Arginine, N= Asparagine, D= Aspartic Acid, C= Cysteine, E= Glutamic Acid, Q= Glutamine, G= Glycine, H= Histidine, I= Isoleucine, L= Leucine, K= Lysine, M= Methionine, F= Phenylalanine, P= Proline, S= Serine, T= Threonine, W= Tryptophan, Y= Tyrosine, V= Valine.")
print("")

Negative_Charged_AA= polypeptide_sequence.count("D"and"E")
Positive_Charged_AA= polypeptide_sequence.count("K" and "H" and "R")
Aromatic_AA= polypeptide_sequence.count("F" and "W" and "Y")
Polar_AA = polypeptide_sequence.count("S" and "T" and "Y" and "N" and "Q" and "C")
NonPolar_AA = polypeptide_sequence.count("A" and "G" and "I" and "L" and "M" and "F" and "W" and "P" and "V")


print("Total number of positively charged amino acids are present in this polypeptide chain is: ", Positive_Charged_AA)
print("Total number of negatively charged amino acids are present in this polypeptide chain is: ", Negative_Charged_AA)
print("Total number of aromatic amino acids are present in this polypeptide chain is: ", Aromatic_AA)
print("Total number of polar amino acids are present in this polypeptide chain is: ", Polar_AA)
print("Total number of non polar amino acids are present in this polypeptide chain is: ", NonPolar_AA)
print("Lengeth of polypeptide is:", len(polypeptide_sequence))
print("Total approximate average molecular weight of the polypeptide: ", (110*len(polypeptide_sequence)))

if Negative_Charged_AA==Positive_Charged_AA:
    print("Net charge of the protein is 0, it is in isoelectric point at physiological pH")
elif Negative_Charged_AA>Positive_Charged_AA:
    print("Net charge of the protein is: ", (Positive_Charged_AA-Negative_Charged_AA))
elif Positive_Charged_AA-Negative_Charged_AA:
        print("Net charge of the protein is: ", (Positive_Charged_AA-Negative_Charged_AA)) 





def calculate_molecular_weight(sequence, mol_weight):
    mol_weight_sum = sum(mol_weight[aa] for aa in sequence)
    
    return mol_weight_sum

mol_weight = {
    'A': 71.08, 'R': 156.19, 'N': 114.11, 'D': 115.09, 'C': 103.15,
    'E': 129.12, 'Q': 128.13, 'G': 57.05, 'H': 137.14, 'I': 113.16,
    'L': 113.16, 'K': 128.17, 'M': 131.20, 'F': 147.18, 'P': 97.12,
    'S': 87.08, 'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13
}

calculated_molweight = calculate_molecular_weight(polypeptide_sequence,mol_weight )
print("Calculated molecular weight in Dalton:",calculated_molweight )

