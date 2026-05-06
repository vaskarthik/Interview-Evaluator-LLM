from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data"


def load_knowledge_base(file_name="interview_knowledge.txt"):
    """
    Load knowledge base text file.
    """

    file_path = DATA_PATH / file_name

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return text


def chunk_text(text: str):
    """
    Very simple chunking:
    split by lines.
    """

    chunks = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    return chunks