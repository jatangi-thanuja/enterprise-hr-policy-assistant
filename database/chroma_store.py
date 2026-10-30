import chromadb

client = chromadb.PersistentClient(
    path="./database/chroma_data"
)

collection = client.get_or_create_collection(
    name="hr_policies"
)