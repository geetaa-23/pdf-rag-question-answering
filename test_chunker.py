from parser import extract_text
from chunker import chunk_text

text = extract_text("sample.pdf")

chunks = chunk_text(text)

print("=" * 50)
print("NUMBER OF CHUNKS:", len(chunks))
print("=" * 50)

for i, chunk in enumerate(chunks[:3]):
    print(f"\nCHUNK {i+1}")
    print("-" * 30)
    print(chunk[:200])