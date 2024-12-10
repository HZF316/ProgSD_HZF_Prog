import sqlite3

def main():
    conn = sqlite3.connect("BookInfo.db")
    cursor = conn.cursor()

    print("Authors and their place of birth:")
    cursor.execute("SELECT Name, PlaceOfBirth FROM Authors;")
    authors = cursor.fetchall()
    for name, place in authors:
        print(f"Author: {name}, Place of Birth: {place}")
    
    user_input = input("\nEnter a place of birth to search for authors: ").strip()

    query = """
    SELECT Books.Title, Books.DataPublished, Authors.Name
    FROM Books
    JOIN Authors ON Books.AuthorID = Authors.AuthorID
    WHERE Authors.PlaceOfBirth = ?;
    """
    # 注意这里参数传入要加逗号构成元组
    cursor.execute(query, (user_input,))
    results = cursor.fetchall()

    if results:
        print(f"\nBooks by authors born in {user_input}:")
        for title, year, author_name in results:
            print(f"Title: {title}, Year: {year}, Author: {author_name}")
    else:
        print(f"\nNo books found by authors born in {user_input}.")
    
    conn.close()

if __name__ == "__main__":
    main()