class MultinomialBayes:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.class_priors = {}
        self.word_probs = {}
        self.classes = None
        self.vocabulary = None

        