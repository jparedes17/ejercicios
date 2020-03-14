def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError('Strands must have the same length')
    
    strand_a = strand_a.lower()
    strand_b = strand_b.lower()
    count = 0
    
    for i in range(len(strand_a)):	
        if strand_a[i] != strand_b[i]:	
            count = count + 1
            
    return count