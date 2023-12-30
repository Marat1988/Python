

def insert_doctor(cursor):
    try:
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name:")
        salary = int(input("Enter your salary: "))
        holiday = bool(input("Enter your holiday: "))
        specializationId = int(input("Enter your specializationId: "))
        query = "INSERT INTO doctor (firstname, lastname, salary, holiday, specializationId) VALUES (%s, %s, %s, %s, %s)"
        values = (firstname, lastname, salary, holiday, specializationId)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)

