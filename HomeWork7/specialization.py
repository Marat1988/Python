def insert_specialization(cursor):
    try:
        name = input("Enter your name: ")
        query = "INSERT INTO specialization (name) VALUES (%s)"
        values = name
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def show_specialization(cursor):
    print("Все специализации")
    try:
        query = "SELECT * FROM specialization"
        cursor.execute(query)
        print(*cursor)
    except Exception as e:
        print(e)


def update_specialization(cursor):
    print("-------------------------------------")
    show_specialization(cursor)
    print("-------------------------------------")
    specialization_id = int(input("Enter the specialization id: "))
    new_name = input("Enter the new name: ")
    try:
        query = "UPDATE specialization SET name = %s WHERE id = %s"
        values = (new_name, specialization_id)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def delete_specialization(cursor):
    print("-------------------------------------")
    show_specialization(cursor)
    print("-------------------------------------")
    specialization_id = int(input("Enter the specialization id: "))
    try:
        query = "DELETE FROM specialization WHERE id = %s"
        values = specialization_id
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def delete_all_specializations(cursor):
    choose = int(input("Enter 1 for delete all record"))
    if choose == 1:
        try:
            query = "DELETE FROM specialization"
            cursor.execute(query)
            cursor.connection.commit()
        except Exception as e:
            print(e)
