from TP.loading import load_directory
from TP.kmers import stream_kmers, kmer2str

def jaccard(fileA, fileB, k):
    # Concatenate the sequences from the list into a single string for each sample
    seqA = "".join(fileA)
    seqB = "".join(fileB)

    # Convert the generator into a set to evaluate all the k-mers
    setA = set(stream_kmers(seqA, k))
    setB = set(stream_kmers(seqB, k))

    # Calculate the intersection and union
    intersection = len(setA & setB)
    union = len(setA | setB)

    # Avoid division by zero
    if union == 0:
        j = 0
    else:
        j = intersection / union

    return j

if __name__ == "__main__":
    print("Computation of Jaccard similarity between files")

    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    print("Computing Jaccard similarity for all pairs of samples")
    filenames = list(files.keys())

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            # Call the jaccard function for each pair of samples
            j_sim = jaccard(files[filenames[i]], files[filenames[j]], k)
            print(f"{filenames[i]} vs {filenames[j]}: {j_sim}")
