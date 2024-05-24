Information Retrieval System
This project is an implementation of various information retrieval models in Python. The primary focus of this project is the LinearBooleanModel, which is used to perform boolean searches on a collection of documents. The system also supports stop word removal and stemming.

Table of Contents
Installation
Usage
Project Structure
Retrieval Models
Stop Word Removal
Contributing
License
Installation
To get started with this project, clone the repository and install the necessary dependencies.

Clone the Repository

git clone https://github.com/yourusername/information-retrieval-system.git
cd information-retrieval-system
Install Dependencies
Make sure you have Python 3.x installed. Then, install the required Python packages:


pip install -r requirements.txt
Usage
To use the information retrieval system, you need to have a collection of documents. The system will allow you to build a collection, set a retrieval model, and perform searches.

Running the Program

python main.py
Follow the on-screen prompts to interact with the system. You can list documents, search for terms, and change retrieval models.

Project Structure

information-retrieval-system/
│
├── data/                      # Directory containing the document collection
├── document.py                # Document class for handling document operations
├── retrieval_models.py        # Contains all retrieval model classes
├── main.py                    # Main script to run the information retrieval system
├── requirements.txt           # Python package dependencies
└── README.md                  # This file
Retrieval Models
LinearBooleanModel
The LinearBooleanModel is a simple implementation of a boolean retrieval model using linear search. It supports the following features:

Converting documents to boolean representations
Converting queries to boolean representations
Matching documents against queries based on boolean logic

from document import Document
from retrieval_models import LinearBooleanModel

# Example document
doc = Document("doc1", "This is a sample document with sample text.")

# Initialize the model
model = LinearBooleanModel()

# Convert document and query to representations
doc_representation = model.document_to_representation(doc)
query_representation = model.query_to_representation("sample text")

# Perform a match
score = model.match(doc_representation, query_representation)
print(score)  # Output: 1.0 (exact match)
Stop Word Removal
The system includes functionality for removing stop words from documents and queries. This can improve the relevance of search results by ignoring common words that are not useful for matching.

Example Usage with Stop Word Removal

from document import Document
from retrieval_models import LinearBooleanModel

# Example document
doc = Document("doc1", "This is a sample document with sample text.")

# Initialize the model
model = LinearBooleanModel()

# Convert document and query to representations with stop word removal
doc_representation = model.document_to_representation(doc, stopword_filtering=True)
query_representation = model.query_to_representation("sample text")

# Perform a match
score = model.match(doc_representation, query_representation)
print(score)  # Output depends on the presence of stop words
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bugs or feature requests.
