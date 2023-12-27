def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])

print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
print(DNA_strand("GTATCGATCGATCGATCGATTATATTTTCGACGAGATTTAAATATATATATATACGAGAGAATACAGATAGACAGATTA"))
