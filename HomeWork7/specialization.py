def insert_specialization(cursor):
    try:
        name = input("Enter your name: ")
        query = "INSERT INTO specialization (name) VALUES (%s)"
        values = name
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)