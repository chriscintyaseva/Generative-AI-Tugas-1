from my_ai_project.retrieval.chunker import chunk_text


def test_chunk_text():
    text = "one two three four five"

    chunks = list(chunk_text(text, chunk_size=2))

    assert chunks == [
        "one two",
        "three four",
        "five",
    ]