import sqlite3
import numpy as np

# ----------------------------------------
# 1. CONNECT TO SQLITE FILE (persistent)
# ----------------------------------------
conn = sqlite3.connect("books_vectors.db")

# ----------------------------------------
# 2. CREATE TABLE (only once)
# ----------------------------------------
conn.execute("""
CREATE TABLE IF NOT EXISTS books_vectors (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    embedding BLOB NOT NULL
);
""")
conn.commit()

# ----------------------------------------
# 3. HELPER TO CREATE A VECTOR
# ----------------------------------------
def make_vec(value: float) -> bytes:
    return np.array([value] * 384, dtype=np.float32).tobytes()

# ----------------------------------------
# 4. INSERT SAMPLE DATA (only once)
# ----------------------------------------
book1 = (1, "Book 1: Intro to AI", make_vec(0.10))
book2 = (2, "Book 2: Cooking with Love", make_vec(0.80))
book3 = (3, "Book 3: Machine Learning", make_vec(0.14))

conn.executemany(
    "INSERT OR REPLACE INTO books_vectors (id, title, embedding) VALUES (?, ?, ?)",
    [book1, book2, book3]
)
conn.commit()

# ----------------------------------------
# 5. FUNCTION TO CONVERT BLOB → VECTOR
# ----------------------------------------
def blob_to_vec(blob):
    return np.frombuffer(blob, dtype=np.float32)

# ----------------------------------------
# 6. FAKE EMBEDDING FOR USER QUERY
# ----------------------------------------
def fake_text_embedding(text: str):
    return np.array([0.15] * 384, dtype=np.float32)

# ----------------------------------------
# 7. USER QUERY
# ----------------------------------------
query_text = input("Enter your search text: ")
query_vec = fake_text_embedding(query_text)

# ----------------------------------------
# 8. FETCH ALL VECTORS FROM SQLITE
# ----------------------------------------
cur = conn.execute("SELECT id, title, embedding FROM books_vectors")
rows = cur.fetchall()

# ----------------------------------------
# 9. COMPUTE COSINE SIMILARITY MANUALLY
# ----------------------------------------
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

scores = []
for row in rows:
    book_id, title, emb_blob = row
    vec = blob_to_vec(emb_blob)
    score = cosine_similarity(query_vec, vec)
    scores.append((score, title))

# ----------------------------------------
# 10. SORT + SHOW TOP-2 RESULTS
# ----------------------------------------
scores.sort(reverse=True)  # highest cosine = most similar
top2 = scores[:2]

print("\nTop-2 similar books:")
for score, title in top2:
    print(f"{title}  (similarity={score:.4f})")
