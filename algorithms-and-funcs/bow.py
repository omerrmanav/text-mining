def create_bow_vector(documents):
    vocabulary = set()
    for doc in documents:
        words = doc.lower().replace(',', '').replace('.', '').split()
        vocabulary.update(words)

    vocab_list = sorted(list(vocabulary))
    vocab_index = {word: i for i, word in enumerate(vocab_list)}

    bow_vectors = []
    for  doc in documents:
        vector = [0]*len(vocab_list)
        words = doc.lower().replace(',', '').replace('.', '').split()
        for word in words:
            vector[vocab_index[word]] += 1
        bow_vectors.append(vector)

    return vocab_list, bow_vectors

documents = [
    "I love coding",
    "Coding is fun, I love it",
    "Python coding is great"
]

vocabulary, vectors = create_bow_vector(documents)

print("Vocabulary: ", vocabulary)
print("\nBoW Vectors for documents: ")
for i, vec in enumerate(vectors):
    print(f"Document {i+1}:{vec}")