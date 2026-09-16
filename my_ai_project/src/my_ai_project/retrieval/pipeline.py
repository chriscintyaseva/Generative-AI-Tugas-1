from my_ai_project.retrieval.chunker import chunk_text
from my_ai_project.retrieval.embedder import embed_texts


def build_pipeline(text: str):
    """Chunk text and create embeddings."""

    chunks = list(chunk_text(text))
    vectors = embed_texts(chunks)

    return {
        "chunks": chunks,
        "vectors": vectors,
    }