def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    longer = int(len(dna1)) > int(len(dna2))
    return longer
        

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    occurrences = dna.count(nucleotide)
    return occurrences


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    occurs = dna2 in dna1
    return occurs


def is_valid_sequence(sequence):
    """ (str -> bool
    
    Return True if and only if DNA sequence is valid, that is, it contains
    no characters other than 'A', 'T', 'C', and 'G'

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ABCDEF')
    False

    """

    is_valid = True
    valid_string = "ATCG"
    
    for base in sequence:
        if base not in valid_string:
            return False

    return is_valid

def insert_sequence(sequence, insertion, location):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ACGT', 'TAG', -1)
    'ACGTAGT'

    """

    sequence = sequence[0:location] + insertion + sequence[location:len(sequence)]
    return sequence

def get_complement(nucleotide):
    """(str) -> str

    >>> get_complement('ACTG')
    'TGAC'
    >>> get_complement('GGGGAAATTTCCC')
    'CCCCTTTTAAAAGGGG'
    >>> get_complement('A')
    'T'

    """

    output = ""

    for base in nucleotide:
        if base == 'A':
            output = output + 'T'
        if base == 'T':
            output = output + 'A'
        if base == 'C':
            output = output + 'G'
        if base == 'G':
            output = output + 'C'

    return output

        
def get_complementary_sequence(sequence):
    """(str) -> str

    >>> get_complement('ACTG')
    'TGAC'
    >>> get_complement('GGGGAAATTTCCC')
    'CCCCTTTTAAAAGGGG'
    >>> get_complement('A')
    'T'

    """

    output = ""
    
    for base in sequence:
        if base == 'A':
            output = output + 'T'
        if base == 'T':
            output = output + 'A'
        if base == 'C':
            output = output + 'G'
        if base == 'G':
            output = output + 'C'

    return output

    
