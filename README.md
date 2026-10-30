# Enterprise HR Policy Assistant using RAG

An AI-powered HR Policy Assistant designed to help employees retrieve information from HR policy documents using Retrieval-Augmented Generation (RAG).

**Project Status: In Progress**

## Overview

This project explores how RAG can be used to build a document-based question-answering system. It processes HR policy PDFs, generates semantic embeddings and stores document chunks in a persistent vector database.

## Current Features

- PDF text extraction using PyPDF.
- Document chunking using Python.
- Semantic embedding generation using Sentence Transformers.
- 384-dimensional embeddings using `all-MiniLM-L6-v2`.
- Persistent vector storage using ChromaDB.
- Document metadata storage, including source filename and page number.

## Current Implementation

Successfully processed two PDF documents and indexed 25 document chunks in ChromaDB.

## Technology Stack

- Python
- PyPDF
- Sentence Transformers
- all-MiniLM-L6-v2
- NumPy
- ChromaDB

## Project Structure

```text
Assistant/
├── Documents/
├── database/
│   ├── __init__.py
│   └── chroma_store.py
├── ingestion/
│   ├── __init__.py
│   ├── extract.py
│   ├── chunk.py
│   └── index_doc.py
├── retrieval/
│   ├── __init__.py
│   └── embeddings.py
├── generation/
├── evaluation/
├── knowledge_graph/
├── tests/
├── .gitignore
└── README.md
```

## Current Progress

The document ingestion and indexing pipeline is implemented and tested.

## Planned Features

- Semantic retrieval using ChromaDB.
- LLM-based answer generation using Gemini.
- Context-grounded answers with source references.
- FastAPI integration.
- RAG evaluation using a golden question-answer dataset.
- Hallucination and retrieval quality evaluation.
- Dockerization and deployment.

## Running the Current Indexing Pipeline

Install the required dependencies, then run from the project root:

```bash
python -m ingestion.index_doc
```

## Project Goal

Build a reliable, evaluation-driven RAG application that answers employee questions using organizational HR policy documents.