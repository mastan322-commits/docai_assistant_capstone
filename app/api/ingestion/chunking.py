def chunk_text(text: str, chunk_size: int = 40, overlap: int = 10) -> list[str]:
    """
    Split text into fixed-size chunks with overlap.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks
