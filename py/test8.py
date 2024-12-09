import sqlite3

def main():
    conn = sqlite3.connect('BookInfo.db')
    cursor = conn.cursor()

    author_name = input("Enter Author Name: ").strip()

    query="""
    SELECT Books.ID, Books.Title, Authors.Name,Books.DataPublished
    FROM Books
    JOIN Authors ON Books.AuthorID=Authors.AuthorID
    WHERE Authors.name = ?;
    """

    cursor.execute(query, (author_name,))
    results = cursor.fetchall()

    if results:
        with open("Booklist.txt","w",encoding="utf-8") as f:
            for bookid,booktitle,authorname,date in results:
                f.write(f"{bookid}-{booktitle}-{authorname}-{date}\n")
        conn.close()
    else:
        print("No books found.")
        conn.close()

    with open("Booklist.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    main()