from abc import ABCMeta, abstractmethod

"""
    This module defines an interface for classifiers.
Todo:
    * Implement more relevant classifiers.
    * Implement simple rules
    * Shuffle data before k-fold cutting in predict_training.
"""

class Classifier(object):
    """Define classifier interface for FlexMatcher."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, data):
        """Initialize the class"""
        pass

    @abstractmethod
    def fit(self, data):
        """Train based on the input training data."""
        pass

    @abstractmethod
    def predict_training(self, data):
        """Predict the training data (using k-fold cross validation)."""
        pass

    @abstractmethod
    def predict(self, data):
        """Predict for unseen data."""
        pass


    
