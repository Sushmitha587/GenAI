'''import sqlite3

# ------------------------------
# 1. CONNECT TO SQLITE DATABASE
# ------------------------------
conn = sqlite3.connect("mydata.db")
cur = conn.cursor()

# ------------------------------
# 2. CREATE TABLE
# ------------------------------
cur.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    document TEXT NOT NULL,
    metadata TEXT
);
""")

# Your data (same as ChromaDB)
student_info = "Student name is John, studying AI."
club_info = "The Robotics Club meets every Friday."
university_info = "The university is ranked top 10 in research."

documents = [student_info, club_info, university_info]
metadatas = ["student info", "club info", "university info"]
ids = ["id1", "id2", "id3"]

# ------------------------------
# 3. INSERT INTO SQLITE
# ------------------------------
for doc_id, doc, meta in zip(ids, documents, metadatas):
    cur.execute("""
        INSERT OR REPLACE INTO documents (id, document, metadata)
        VALUES (?, ?, ?)
    """, (doc_id, doc, meta))

conn.commit()
print("Data saved successfully in SQLite!")



search_text = "student"

cur.execute("""
    SELECT id, document, metadata
    FROM documents
    WHERE document LIKE ?
    LIMIT 2
""", ("%" + search_text + "%",))

results = cur.fetchall()

print("Search results:")
for r in results:
    print(r)'''
    
    
    
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    content TEXT NOT NULL,
    metadata TEXT,
    embedding BLOB
);

