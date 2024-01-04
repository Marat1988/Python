import specialization


def insert_doctor(cursor):
    try:
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name:")
        salary = int(input("Enter your salary: "))
        holiday = bool(input("Enter your holiday: "))
        print("------------------------------------------")
        specialization.show_specialization(cursor)
        print("------------------------------------------")
        specializationId = int(input("Enter your specializationId: "))
        query = ("INSERT INTO doctor (firstname, lastname, salary, holiday, specializationId) VALUES (%s, %s, %s, %s, "
                 "%s)")
        values = (firstname, lastname, salary, holiday, specializationId)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def show_doctors(cursor):
    print("Список докторов")
    try:
        query = "SELECT * FROM doctor"
        cursor.execute(query)
        print(*cursor)
    except Exception as e:
        print(e)


def update_doctor(cursor):
    print("----------------------------------")
    show_doctors(cursor)
    print("----------------------------------")
    doctor_id = int(input("Enter your doctorId: "))
    new_firstname = input("Enter your first name: ")
    new_lastname = input("Enter your last name:")
    new_salary = int(input("Enter your salary: "))
    new_holiday = bool(input("Enter your holiday: "))
    print("----------------------------------")
    specialization.show_specialization(cursor)
    print("----------------------------------")
    new_specializationId = int(input("Enter your specializationId: "))
    try:
        query = ("UPDATE doctor SET firstname = %s, lastname = %s, salary = %s, holiday = %s, specializationId = %s "
                 "WHERE id = %s")
        values = (new_firstname, new_lastname, new_salary, new_holiday, new_specializationId, doctor_id)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def update_all_information_doctors(cursor):
    print("----------------------------------")
    show_doctors(cursor)
    print("----------------------------------")
    new_salary = int(input("Enter your salary for all doctors: "))
    choose = int(input("Enter 1 for update all record"))
    if choose == 1:
        try:
            query = "UPDATE doctor SET salary = %s"
            values = new_salary
            cursor.execute(query, values)
            cursor.connection.commit()
        except Exception as e:
            print(e)
