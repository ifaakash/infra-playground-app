# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Create table if not exists
conn = sqlite3.connect('notes.db')
conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')
conn.close()

class Note(BaseModel):
    content: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/notes")
def get_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.execute("SELECT id, content FROM notes")
    notes = [{"id": row[0], "content": row[1]} for row in cursor]
    conn.close()
    return notes

@app.post("/notes")
def create_note(note: Note):
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (note.content,))
    conn.commit()
    conn.close()
    return {"message": "Note created"}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM notes WHERE id=?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "content": row[1]}
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    return {"message": "Note deleted"}
