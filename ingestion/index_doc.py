
from pathlib import Path

from ingestion.extract import extract_pdf
from ingestion.chunk import create_chunks
from retrieval.embedding import EmbeddingModel
from database.chroma_store import collection


def index_docs():

    doc_Folder = Path("./Documents")

    embedding_model = EmbeddingModel()

    all_chunks = []

    for pdf_path in doc_Folder.glob("*.pdf"):

        print(f"Processing: {pdf_path.name}")

        pages = extract_pdf(pdf_path)

        chunks = create_chunks(pages)

        print(f"Created {len(chunks)} chunks")

        all_chunks.extend(chunks)

    if not all_chunks:
        print("No document chunks found.")
        return

    texts = [chunk["text"] for chunk in all_chunks]

    print(f"Total chunks: {len(texts)}")

    embeddings = embedding_model.generate_embeddings(texts)

    print(f"Embeddings generated: {embeddings.shape}")

    ids = [f"chunk_{i}" for i in range(len(all_chunks))]

    metadatas = [
        {
            "source": chunk["source"],
            "page": chunk["page"]
        }
        for chunk in all_chunks
    ]

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print(f"Successfully indexed {len(all_chunks)} chunks.")

    print(f"Total records in ChromaDB: {collection.count()}")


if __name__ == "__main__":
    index_docs()
