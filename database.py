import sqlite3

with sqlite3.connect('db.sqlite3') as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS goods(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            title VARCHAR (150) NOT NULL,
            price INTEGER,
            warranty_period_days INTEGER NULL
        )
    """
    cursor.execute(query)

    values = (
        ('Sumosung TV', '13499', '180'),
        ('Polystation 6', '7999', '120'),
        ('Chitos Cheese без цукру', '139', None),
        ('Intil Core I8', '24499', '270'),
        ('Toilet paper', '39', '20'),
        ('Toy', '45', None),
        ('Milk без цукру', '23', None),
        ('Cucumber без цукру', '15', None),
        ('Laptop', '1000', '660'),
        ('Shoes', '50', None),
        ('Coffee maker', '80', '200'),
    )

    query = """
        INSERT INTO goods(title, price, warranty_period_days)
        VALUES (?, ?, ?)
    """
    cursor.executemany(query, values)


    query = """
            SELECT title
            FROM goods
            WHERE price >= 50
        """
    result = cursor.execute(query)
    print(result.fetchall())

    without_sugar = cursor.execute('SELECT * FROM goods WHERE title LIKE "%без цукру%"')
    print(f"\n{without_sugar.fetchall()}")

    print(f"\n{cursor.execute('SELECT * FROM goods LIMIT 3').fetchall()}")
    print(f"\n{cursor.execute('SELECT * FROM goods LIMIT 3 OFFSET 3').fetchall()}")
