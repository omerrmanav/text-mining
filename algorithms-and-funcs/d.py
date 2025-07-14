from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "I love programming in Python",
    "Python is a great programming language",
    "I love learning new things"
]

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Convert to array and displayS
print("Feature Names (Vocabulary):")
print(vectorizer.get_feature_names_out())
print("\nBag of Words Matrix:")
print(X.toarray())

