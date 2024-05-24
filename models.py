# Contains all retrieval models.

from abc import ABC, abstractmethod

from document import Document


class RetrievalModel(ABC):
    @abstractmethod
    def document_to_representation(self, document: Document, stopword_filtering=False, stemming=False):
        """
        Converts a document into its model-specific representation.
        This is an abstract method and not meant to be edited. Implement it in the subclasses!
        :param document: Document object to be represented
        :param stopword_filtering: Controls, whether the document should first be freed of stopwords
        :param stemming: Controls, whether stemming is used on the document's terms
        :return: A representation of the document. Data type and content depend on the implemented model.
        """
        raise NotImplementedError()

    @abstractmethod
    def query_to_representation(self, query: str):
        """
        Determines the representation of a query according to the model's concept.
        :param query: Search query of the user
        :return: Query representation in whatever data type or format is required by the model.
        """
        raise NotImplementedError()

    @abstractmethod
    def match(self, document_representation, query_representation) -> float:
        """
        Matches the query and document presentation according to the model's concept.
        :param document_representation: Data that describes one document
        :param query_representation:  Data that describes a query
        :return: Numerical approximation of the similarity between the query and document representation. Higher is
        "more relevant", lower is "less relevant".
        """
        raise NotImplementedError()


class LinearBooleanModel(RetrievalModel):
    # TODO: Implement all abstract methods and __init__() in this class. (PR02)

    def __init__(self):
        pass  # No initialization needed for this model

    def document_to_representation(self, document: Document, stopword_filtering=False, stemming=False):
        """
        Converts a document to a boolean representation.

        Args:
            document: The document to convert.
            stopword_filtering: Whether to remove stop words from the representation.
            stemming: Whether to stem the words in the representation.

        Returns:
            A set of terms representing the document.
        """

        teras = document.terms  # Get the document's terms

        if stopword_filtering:
            if stemming:
                terms = document.filtered_stemmed_terms  # Use filtered and stemmed terms
            else:
                terms = document.filtered_terms  # Use only filtered terms
        else:
            terms = teras  # Use all terms if no filtering or stemming is applied

        return set(terms)  # Return the terms as a set

    def query_to_representation(self, query: str) -> set:
        """
        Converts a query to a boolean representation.

        Args:
            query: The query string.

        Returns:
            A set of terms representing the query.
        """

        return set(query.split())  # Return the query terms as a set

    def match(self, document_representation: set, query_representation: set) -> float:
        """
        Calculates the match score between a document and a query using the boolean retrieval model.

        Args:
            document_representation: The document's boolean representation.
            query_representation: The query's boolean representation.

        Returns:
            A score indicating the match between the document and the query.
        """

        return 1.0 if query_representation.issubset(document_representation) else 0.0  # Exact match

    def __str__(self):
        return 'Boolean Model (Linear)'

class InvertedListBooleanModel(RetrievalModel):
    # TODO: Implement all abstract methods and __init__() in this class. (PR03)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function. (PR3, Task 2)

    def __str__(self):
        return 'Boolean Model (Inverted List)'


class SignatureBasedBooleanModel(RetrievalModel):
    # TODO: Implement all abstract methods. (PR04)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function.

    def __str__(self):
        return 'Boolean Model (Signatures)'


class VectorSpaceModel(RetrievalModel):
    # TODO: Implement all abstract methods. (PR04)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function.

    def __str__(self):
        return 'Vector Space Model'


class FuzzySetModel(RetrievalModel):
    # TODO: Implement all abstract methods. (PR04)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function.

    def __str__(self):
        return 'Fuzzy Set Model'
