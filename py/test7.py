import sqlite3

def main():
    conn = sqlite3.connect('BookInfo.db')
    cursor = conn.cursor()

    years_input = input("Enter the year: ").strip()
    year = int(years_input)

    query="""
    SELECT Title, DataPublished
    FROM Books
    WHERE DataPublished > ?
    ORDER BY DataPublished ASC;
    """

    cursor.execute(query, (year,))
    results = cursor.fetchall()
    if results:
        print(f"\nBooks after {year}:")
        for title, date in results:
            print(f"\tTitle: {title}, DatePublished: {date}")
    else:
        print(f"\nNo books found after {year}.")

    conn.close()

if __name__ == "__main__":
    main()