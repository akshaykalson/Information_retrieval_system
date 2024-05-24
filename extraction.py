# Contains functions that deal with the extraction of documents from a text file (see PR01)

import json

from document import Document

def extract_collection(source_file_path: str) -> list[Document]:
    """
    Loads a text file (aesopa10.txt) and extracts each of the listed fables/stories from the file.
    :param source_file_name: File name of the file that contains the fables
    :return: List of Document objects
    """
    catalog = []  # This dictionary will store the document raw_data.

    catalog = []  # This will store the Document objects

    with open(source_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    fable_start = False
    title = ""
    raw_text = []
    document_id = 0

    for i in range(len(lines) - 3):  # Ensuring we don't go out of range
        line = lines[i]
        if fable_start:
            if line.strip() == "" and lines[i + 1].strip() == "" and lines[i + 2].strip() == "":
                # We have found the end of the fable
                raw_text_str = " ".join(raw_text).replace('\n', ' ')
                terms = raw_text_str.split()

                document = Document()
                document.document_id = document_id
                document.title = title
                document.raw_text = raw_text_str
                document.terms = terms
                document.filtered_terms = []  # These can be processed later
                document.stemmed_terms = []  # These can be processed later

                catalog.append(document)
                document_id += 1
                raw_text = []
                fable_start = False
            else:
                raw_text.append(line.strip())
        elif line.strip() == "" and lines[i + 1].strip() == "" and lines[i + 2].strip() == "" and lines[i + 3].strip():
            # We have found the start of a fable
            title = lines[i + 3].strip()
            fable_start = True

    # Check for the last fable in case the loop ends without hitting the exact conditions
    if fable_start and raw_text:
        raw_text_str = " ".join(raw_text).replace('\n', ' ')
        terms = raw_text_str.split()

        document = Document()
        document.document_id = document_id
        document.title = title
        document.raw_text = raw_text_str
        document.terms = terms
        document.filtered_terms = []
        document.stemmed_terms = []

        catalog.append(document)

    return catalog


def save_collection_as_json(collection: list[Document], file_path: str) -> None:
    """
    Saves the collection to a JSON file.
    :param collection: The collection to store (= a list of Document objects)
    :param file_path: Path of the JSON file
    """

    serializable_collection = []
    for document in collection:
        serializable_collection += [{
            'document_id': document.document_id,
            'title': document.title,
            'raw_text': document.raw_text,
            'terms': document.terms,
            'filtered_terms': document.filtered_terms,
            'stemmed_terms': document.stemmed_terms
        }]

    with open(file_path, "w") as json_file:
        json.dump(serializable_collection, json_file)


def load_collection_from_json(file_path: str) -> list[Document]:
    """
    Loads the collection from a JSON file.
    :param file_path: Path of the JSON file
    :return: list of Document objects
    """
    try:
        with open(file_path, "r") as json_file:
            json_collection = json.load(json_file)

        collection = []
        for doc_dict in json_collection:
            document = Document()
            document.document_id = doc_dict.get('document_id')
            document.title = doc_dict.get('title')
            document.raw_text = doc_dict.get('raw_text')
            document.terms = doc_dict.get('terms')
            document.filtered_terms = doc_dict.get('filtered_terms')
            document.stemmed_terms = doc_dict.get('stemmed_terms')
            collection += [document]

        return collection
    except FileNotFoundError:
        print('No collection was found. Creating empty one.')
        return []
