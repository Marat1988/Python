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


def show_info_doctors_specialization(cursor):
    try:
        query = "SELECT fullname, specialization FROM vw_show_info_doctors"
        cursor.execute(query)
        print(*cursor)
    except Exception as e:
        print(e)


def show_doctors_not_holiday(cursor):
    try:
        query = "SELECT lastname, salary FROM vw_show_info_doctors WHERE holiday = 0"
        cursor.execute(query)
        print(*cursor)
    except Exception as e:
        print(e)


def delete_doctor(cursor):
    print("----------------------------------")
    show_doctors(cursor)
    print("----------------------------------")
    doctor_id = int(input("Enter your doctorId: "))
    try:
        query = "DELETE FROM doctor WHERE id = %s"
        values = doctor_id
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def delete_all_doctors(cursor):
    choose = int(input("Enter 1 for delete all record"))
    if choose == 1:
        try:
            query = "DELETE FROM doctor"
            cursor.execute(query)
            cursor.connection.commit()
        except Exception as e:
            print(e)
