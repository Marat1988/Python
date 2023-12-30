
def insert_ward(cursor):
    try:
        number = int(input("Enter your number: "))
        places = int(input("Enter your places you: "))
        query = "INSERT INTO ward (number, places) VALUES (%s, %s)"
        values = (number, places)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)