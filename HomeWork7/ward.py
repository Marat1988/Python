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


def show_wards(cursor):
    print("Список палат")
    try:
        query = "SELECT * FROM ward"
        cursor.execute(query)
        print(*cursor)
    except Exception as e:
        print(e)


def update_ward(cursor):
    print("------------------------------")
    show_wards(cursor)
    print("------------------------------")
    ward_id = int(input("Enter your ward id: "))
    new_number = int(input("Enter your new number: "))
    new_places = int(input("Enter your new places you: "))
    try:
        query = "UPDATE ward SET number = %s, places = %s WHERE id = %s"
        values = (new_number, new_places, ward_id)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def update_all_information_wards(cursor):
    new_places = int(input("Enter your new places you: "))
    choose = int(input("Enter 1 for update all record"))
    if choose == 1:
        try:
            query = "UPDATE ward SET places = %s"
            values = new_places
            cursor.execute(query, values)
            cursor.connection.commit()
        except Exception as e:
            print(e)


def delete_ward(cursor):
    print("----------------------------------")
    show_wards(cursor)
    print("----------------------------------")
    ward_id = int(input("Enter your ward id: "))
    try:
        query = "DELETE FROM ward WHERE id = %s"
        values = ward_id
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def delete_all_wards(cursor):
    choose = int(input("Enter 1 for delete all record"))
    if choose == 1:
        try:
            query = "DELETE FROM ward"
            cursor.execute(query)
            cursor.connection.commit()
        except Exception as e:
            print(e)
