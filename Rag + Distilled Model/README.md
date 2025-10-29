# Apollo 11 RAG & Distilled Model Evaluation

This notebook demonstrates a **Retrieval-Augmented Generation (RAG)** system
using data from the **Apollo 11 mission**.  
It uses **LangChain**, **HuggingFace**, and **ChromaDB** to load, embed, and
query textual data, then evaluates responses using a set of pre-defined prompts
from a JSON file.

---

## Project Description

The notebook `Apollo11_rag&distilled.ipynb` contains a structured RAG pipeline
with four main parts:

1. **Data Loading** – Reads Apollo 11 mission text data from a JSON file.
2. **Database Creation** – Builds a local ChromaDB vector store for semantic
search.  
   > This step should be run **only once**, as it creates and saves the
database locally.
3. **Query & Generation** – Retrieves relevant context for a given question and
uses a model to generate an answer.
4. **Evaluation** – Tests the model’s responses using predefined data from the
JSON file.

---

## Folder Structure

```text
 Rag + Distilled Model/
├── Apollo11_rag&distilled.ipynb   ← Main Jupyter Notebook
├── README.md                      ← Project documentation
└── data/
    ├── apollo11_docs.json     ← Apollo 11 text dataset and evaluation prompts
    └── chroma_db/             ← Auto-created vector database folder
                                  (It will appear after you run it)
```

---

## Models Used

* **LaMini-Flan-T5-248M**: It is a Local LLM and it is a distilled version of
Google's Flan-T5, optimized for lightweight text generation tasks.
Used here for reasoning, summarization, and RAG response generation.
* **all-MiniLM-L6-v2**: It as an Embedding model and it is a compact sentence-transformer
model used to convert text chunks into numerical vector embeddings for
semantic search and retrieval.

These two models make the project lightweight, fully local, and suitable for GPU
or CPU execution.

---

## Notes

* The ChromaDB folder (data/chroma_db/) is automatically generated when you first
run the document loader.
* You can safely delete it to rebuild embeddings later.
* The notebook does not require an external .txt file — all content is inside
the JSON.
* The model automatically detects whether to use GPU (torch.cuda.is_available()).
