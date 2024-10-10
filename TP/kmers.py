def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for _ in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)

def stream_kmers(text, k):
    """ Stream k-mers from a DNA sequence
    :param str text: The DNA sequence
    :param int k: The length of each k-mer
    :return: A generator yielding k-mer strings
    """
    if len(text) < k:
        return  # If the sequence is shorter than k, return nothing

    # Convert first k-mer into an integer representation
    val = 0
    for i in range(k):
        if text[i] == 'A':
            val = (val << 2) | 0
        elif text[i] == 'C':
            val = (val << 2) | 1
        elif text[i] == 'T':
            val = (val << 2) | 2
        elif text[i] == 'G':
            val = (val << 2) | 3
        else:
            raise ValueError(f"Invalid nucleotide '{text[i]}' found in the sequence.")
    
    # Yield the first k-mer as a string
    yield kmer2str(val, k)

    # Sliding window over the rest of the sequence
    for i in range(k, len(text)):
        val = (val << 2) & ((1 << (2 * k)) - 1)  # Shift left and keep last k-mer bits
        if text[i] == 'A':
            val |= 0
        elif text[i] == 'C':
            val |= 1
        elif text[i] == 'T':
            val |= 2
        elif text[i] == 'G':
            val |= 3
        else:
            raise ValueError(f"Invalid nucleotide '{text[i]}' found in the sequence.")

        # Yield the next k-mer as a string
        yield kmer2str(val, k)
