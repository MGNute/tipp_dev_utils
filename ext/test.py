import numpy as np
import nwops

top=np.zeros(30,dtype=np.int32)
lens=np.ones(30,dtype=np.float64)

nseq_prot='ATGGCTATTGTTAAATGTAAGCCGACTTCGGCTGGTCGCCGTCACGTCGTTAAAATTGTGAACAATGACCTGCATAAAGGTAAGCCTTATGCGCC' \
         'GCTTTTAGAAAAAAATTCTAAAAACGGTGGTCGTAACAACAACGGTCGTATCACAGTACGTCACATCGGTGGTGGGCATAAGCAACACTATCGTT' \
         'TGATCGATTTTAAACGTACTAAAGATGGCATTCCGGCAAAAGTTGAGCGTCTGGAATATGATCCAAACCGTAGTGCAAACATCGCTTTGGTTCTT' \
         'TATGCAGACGGTGAACGTCGTTACATCATTGCACCGAAAGGTCTGCAAGCTGGTGATGTAATCCAGTCTGGCGTTGACGCACCGATTAAAGCAGG' \
         'TAATACACTGCCGATGCGCAATATCCCAGTGGGTTCAACAGTTCACTGTGTTGAATTGAAACCTGGCAAAGGTGCACAACTTGCACGTTCTGCTG' \
         'GTGCTTATGCACAAATCGTTGCTCGTGACGGTGCATACGCAACAATTCGTCTGCGTTCTGGTGAGATGCGTCGAGTTCCTTCTGAAGGTCGTGCA' \
         'ACGATTGGTGAAGTTGGTAACTCTGAGCACATGCTTCGTGAACTTGGTAAAGCAGGTGCTACACGTTGGCGTGGTGTTCGTCCTACTGTTCGCGG' \
         'TGTTGTGATGAACCCAGTTGACCACCCACACGGTGGTGGTGAAGGTCGCACATCCGGTGGTCGTCACCCTGTATCTCCTTGGGGTATGCCTACTA' \
         'AGGGCTTCAAAACCCGTAAAAACAAACGCACCGACAAGTACATTGTACGTCGTCGTAATAAGTAA';
len(nseq_prot)
#825

nseq_fu='TGGGGCCTTATTGTTTAAATATGTGTAAAGCCCCGCGGACACTCTTTTCTCGCGGGGCTGGTCCGCGCCCCCGTCACCGTCTCGTTAAAATTTGTG' \
        'AACAAAAATGACACCCCTCTGTGCGCACATAAAAAGGTAAGCCTCTTATATTGCGCCGCTCTTTTTTTTTTATAGAGAGAAAAAAATTCTAAAAAA' \
        'AAACACGCGGGGTGTGTGGGGTTCGTATAAACACAACAACGGTCGTATATCACAGTACCGTCTCAACATCGGGTGGTGTGGGGGGGCATAAGCAAC' \
        'ACACTATATCGTTTTTGATCGCGATTTTTTTTAAACGTACTAAAAAAGATGGCGCACATTCTCCGCGGGGCAAAAAAGAGTGTTTTGTGAGAGCGC' \
        'GTGTCTCTGGGGAGAAAATATATGTGAGATCCCAAACCCGTGTATAGTGTGTGCGCACAAAAACACATATCTCGCGGCT';
len(nseq_fu)

p_pos=np.zeros(len(nseq_raw) + len(nseq_fu) + 4, dtype=np.int32)
n_pos=np.zeros(len(nseq_raw) + len(nseq_fu) + 4, dtype=np.int32)

nwops.get_pairwise_alignment(nseq_prot, nseq_fu, p_pos, n_pos)

# print(p_pos)
# print(n_pos)
