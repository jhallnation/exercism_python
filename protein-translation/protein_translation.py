def proteins(strand):
    codons_proteins = {
      'Methionine':     ('AUG'),
      'Phenylalanine':  ('UUU','UUC'),
      'Leucine':        ('UUA','UUG'),
      'Serine':         ('UCU','UCC','UCA','UCG'),
      'Tyrosine':       ('UAU','UAC'),
      'Cysteine':       ('UGU','UGC'),
      'Tryptophan':     ('UGG'),
      'STOP':           ('UAA','UAG','UGA'),
    }

    proteins_found = []

    codon_list = [strand[i:i+3] for i in range(0, len(strand), 3)]

    for codon in codon_list:
      for key, value in codons_proteins.items():
        if codon in value and key == 'STOP':
          return proteins_found
        elif codon in value:
          proteins_found.append(key)
          
    return proteins_found