import sqlite3
import numpy as np

# ------------------------------------------
# 1. CONNECT + LOAD VECTOR EXTENSION
# ------------------------------------------
conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)

# path to your sqlite-vec DLL
conn.load_extension(r"C:\sqlite_project\vector0.dll")

# ------------------------------------------
# 2. CREATE VECTOR TABLE
# ------------------------------------------
conn.execute("""
CREATE TABLE books_vectors (
    id        INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    embedding BLOB NOT NULL
);
""")

# Helper: create fake 384-dim vectors
def make_vec(value: float) -> bytes:
    return np.array([value] * 384, dtype=np.float32).tobytes()

# Sample book vectors
book1_emb = make_vec(0.10)
book2_emb = make_vec(0.80)
book3_emb = make_vec(0.14)

conn.executemany(
    "INSERT INTO books_vectors (id, title, embedding) VALUES (?, ?, ?)",
    [
        (1, "Book 1: Intro to AI",       book1_emb),
        (2, "Book 2: Cooking with Love", book2_emb),
        (3, "Book 3: Machine Learning",  book3_emb),
    ],
)
conn.commit()

# ------------------------------------------
# 3. Create a fake embedding for the query
# ------------------------------------------
def fake_text_embedding(text: str) -> bytes:
    return np.array([0.15] * 384, dtype=np.float32).tobytes()

query_text = input("Enter your search text: ")
query_emb = fake_text_embedding(query_text)

# ------------------------------------------
# 4. CORRECT VECTOR SEARCH
# ------------------------------------------
cur = conn.execute(
    """
    SELECT id, title, distance
    FROM vec_search(
        'books_vectors',   -- table name
        'embedding',       -- vector column
        ?,                 -- query vector
        2,                 -- top-k
        'cosine'           -- distance metric
    );
    """,
    (query_emb,),
)

results = cur.fetchall()

# ------------------------------------------
# 5. PRINT RESULTS
# ------------------------------------------
print("\nTop-2 similar books:")
for r in results:
    print(r)
