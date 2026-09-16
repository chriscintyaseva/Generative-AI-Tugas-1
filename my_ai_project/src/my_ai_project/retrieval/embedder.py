def embed_texts(texts: list[str]):
    return [f"embedding({text})" for text in texts]