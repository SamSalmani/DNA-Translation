"""
Created on Wed Oct  4 12:53:45 2021
@author: hsalmanitehrani
"""


#read the DNA file
input = "/kaggle/dna_data/DNA.txt"
f= open(input, "r")
seq = f.read()


# remove the problematic string exist due to copy pase
seq = seq.replace("\n","")
seq = seq.replace("\r","")



# %% [code]
def translate(seq):
    """Translate a string containing a nucleotise sequence into a string 
    containing the corresponding sequence of amino acides. Nucleotides are translated 
    in trip;ets using the table dictionary; each amino acid is encoded with a 
    string of length 1"""
    #Table related to DNA translations. A dictionary including DNA names and associated amino acid
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}
    
    protein = ""
    if len(seq)%3 ==0:
        for i in range(0,len(seq),3):
            codon = seq[i:i+3]
            protein += table[codon]
    return protein

# %% [code]
#better method to read a file using with function 
def read_seq(inputfile):
    """Reads and returns the input sequence with special characters removed """
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n","")
    seq = seq.replace("\r","")
    return seq

# %% [code]
prt = read_seq("protein.txt")
dna = read_seq("DNA.txt")

#based on NCBA website, the sequence start from 21 to 938 (in python, as it starts from 0, we will get 20 to 938 that 938 not included)
#also as the last one gives "-", we will ignore the last seq and will go up to 935

prt == translate(dna[20:935])

#instead of going up to 935, we will go up to 938 and exclude last character
prt == translate(dna[20:938])[:-1]
