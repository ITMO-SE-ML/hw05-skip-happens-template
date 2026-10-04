"""Реализуйте одно дерево классификации самостоятельно."""
class Model:
    def __init__(self, case, features, max_depth=6, min_samples_leaf=30,
                 threshold=0.5, smoothing=1.0):
        self.case = case
        self.features = list(features)
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.threshold = threshold
        self.smoothing = smoothing

    def fit(self, X, y):
        raise NotImplementedError

    def predict_proba(self, X):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def save(self, path):
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        raise NotImplementedError

