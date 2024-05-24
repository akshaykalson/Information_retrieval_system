# Contains all functions that deal with stop word removal.

from document import Document


def remove_symbols(text_string: str) -> str:
    """
    Removes all punctuation marks and similar symbols from a given string.
    Occurrences of "'s" are removed as well.
    :param text:
    :return:
    """

    # Handle "'s" separately
    text_string = text_string.replace("'s", "")

    # Define punctuation marks to remove
    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Remove punctuation marks
    cleaned_text = ''.join(char for char in text_string if char not in punctuation_marks)

    return cleaned_text


def is_stop_word(term: str, stop_word_list: list[str]) -> bool:
    """
    Checks if a given term is a stop word.
    :param stop_word_list: List of all considered stop words.
    :param term: The term to be checked.
    :return: True if the term is a stop word.
    """
    return term.lower() in stop_word_list

def remove_stop_words_from_term_list(term_list: list[str], stop_word_list: list[str]) -> list[str]:
    """
    Takes a list of terms and removes all terms that are stop words.
    :param term_list: List that contains the terms
    :return: List of terms without stop words
    """
    # Hint:  Implement the functions remove_symbols() and is_stop_word() first and use them here.
    return [term for term in term_list if not is_stop_word(term, stop_word_list)]


def filter_collection(collection: list[Document], stop_word_list: list[str] = None):
    """
    For each document in the given collection, this method takes the term list and filters out the stop words.
    Warning: The result is NOT saved in the documents term list, but in an extra field called filtered_terms.
    :param collection: Document collection to process
    """
    for document in collection:
        # Remove symbols from terms before checking for stop words
        cleaned_terms = [remove_symbols(term) for term in document.terms]
        if stop_word_list:
            filtered_terms = remove_stop_words_from_term_list(cleaned_terms, stop_word_list)
        else:
            filtered_terms = cleaned_terms  # If stop_word_list is not provided, use all terms
        document.filtered_terms = filtered_terms

def load_stop_word_list(raw_file_path: str) -> list[str]:
    """
    Loads a text file that contains stop words and saves it as a list. The text file is expected to be formatted so that
    each stop word is in a new line, e. g. like englishST.txt
    :param raw_file_path: Path to the text file that contains the stop words
    :return: List of stop words
    """
    with open(raw_file_path, 'r', encoding='utf-8') as file:
        stop_words = file.read().splitlines()
    return stop_words


def create_stop_word_list_by_frequency(collection: list[Document]) -> list[str]:
    """
    Uses the method of J. C. Crouch (1990) to generate a stop word list by finding high and low frequency terms in the
    provided collection.
    :param collection: Collection to process
    :return: List of stop words
    """
    term_frequency = {}
    for document in collection:
        for term in document.terms:
            term = term.lower()
            if term not in term_frequency:
                term_frequency[term] = 0
            term_frequency[term] += 1

    sorted_terms = sorted(term_frequency.items(), key=lambda item: item[1])
    stop_words = [term for term, freq in sorted_terms[:int(len(sorted_terms) * 0.05)]]
    stop_words += [term for term, freq in sorted_terms[-int(len(sorted_terms) * 0.05):]]
    return stop_words