import doctor
import ward


def insert_patient(cursor):
    try:
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name:")
        receiptdate = input("Enter your receipt date (YYYY-MM-DD): ")
        print("------------------------------------------")
        ward.show_wards(cursor)
        print("------------------------------------------")
        wardId = int(input("Enter your ward id: "))
        print("------------------------------------------")
        doctor.show_doctors(cursor)
        print("------------------------------------------")
        doctorId = int(input("Enter your doctor id: "))
        print("------------------------------------------")
        diagnosis = input("Enter your diagnosis: ")
        query = ("INSERT INTO patient (firstname, lastname, receiptdate, wardId, doctorId, diagnosis) VALUES (%s, %s, "
                 "%s, %s, %s, %s)")
        values = (firstname, lastname, receiptdate, wardId, doctorId, diagnosis)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def show_patients(cursor):
    print("Список пациентов")
    try:
        query = "SELECT * FROM patient"
        cursor.execute(query)
        print(*cursor)
    except Exception as e:
        print(e)


def update_patient(cursor):
    print("------------------------------------------")
    show_patients(cursor)
    print("------------------------------------------")
    patientId = input("Enter your patient id: ")
    new_firstname = input("Enter your first name: ")
    new_lastname = input("Enter your last name: ")
    new_receiptdate = input("Enter your receipt date (YYYY-MM-DD): ")
    print("------------------------------------------")
    ward.show_wards(cursor)
    print("------------------------------------------")
    new_wardId = input("Enter your ward id: ")
    print("---------------------------------------")
    doctor.show_doctors(cursor)
    print("---------------------------------------")
    new_doctorId = input("Enter your doctor id: ")
    new_diagnosis = input("Enter your diagnosis: ")
    try:
        query = ("UPDATE patient SET firstname = %s, lastname = %s, receiptdate = %s, wardId = %s, doctorId = %s, "
                 "diagnosis = %s WHERE id = %s")
        values = (new_firstname, new_lastname, new_receiptdate, new_wardId, new_doctorId, new_diagnosis, patientId)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def update_all_information_patients(cursor):
    print("---------------------------------------")
    doctor.show_doctors(cursor)
    print("---------------------------------------")
    new_doctorId = input("Enter your doctor id for update information: ")
    choose = int(input("Enter 1 for update all record"))
    if choose == 1:
        try:
            query = ("UPDATE patient SET doctorId = %s")
            values = new_doctorId
            cursor.execute(query, values)
            cursor.connection.commit()
        except Exception as e:
            print(e)


def delete_patient(cursor):
    print("----------------------------------")
    show_patients(cursor)
    print("----------------------------------")
    patientId = input("Enter your patient id: ")
    try:
        query = "DELETE FROM patient WHERE id = %s"
        values = patientId
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)


def delete_all_patients(cursor):
    choose = int(input("Enter 1 for delete all record"))
    if choose == 1:
        try:
            query = "DELETE FROM patient"
            cursor.execute(query)
            cursor.connection.commit()
        except Exception as e:
            print(e)
