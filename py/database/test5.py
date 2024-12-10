import sqlite3
import os

def main():
    if os.path.exists("BookInfo.db"):
        os.remove("BookInfo.db")

    conn = sqlite3.connect("BookInfo.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE Authors (
        AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        PlaceOfBirth TEXT
    );
    """)

    authors_data = [
        ('Agatha Christie', 'Troquay'),
        ('J.K. Rowling', 'Bristol'),
        ('Oscar Wilde','Dublin')
    ]
    
    cursor.executemany("INSERT INTO Authors (Name, PlaceOfBirth) VALUES (?,?);",authors_data)

    cursor.execute("""
    CREATE Table Books(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        AuthorID INTEGER NOT NULL,
        DataPublished INTEGER,
        FOREIGN KEY (AuthorID) REFERENCES Authors (AuthorID)
    );
    """)

    cursor.execute("SELECT AuthorID, Name From Authors;")
    author_map = {name:aid for (aid, name) in cursor.fetchall()}
    
    books_data = [
        ('De Profundis', author_map['Oscar Wilde'], 1905),
        ('Harry Potter and the chamber of secrets', author_map['J.K. Rowling'], 1998),
        ('The seven dials mystery', author_map['Agatha Christie'], 1929),
        ('The picture of Dorian Gray', author_map['Oscar Wilde'], 1890),
        ('Murder on the Orient Express', author_map['Agatha Christie'], 1934),
        ('Harry Potter and the prisoner of Azkaban', author_map['J.K. Rowling'], 1999)
    ]

    cursor.executemany("INSERT INTO Books (Title,AuthorID,DataPublished) VALUES (?,?,?);",books_data)

    conn.commit()

    conn.close()

if __name__=="__main__":
    main()