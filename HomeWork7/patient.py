def insert_patient(cursor):
    try:
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name:")
        receiptdate = input("Enter your receipt date (YYYY-MM-DD): ")
        wardId = int(input("Enter your ward id: "))
        doctorId = int(input("Enter your doctor id: "))
        diagnosis = input("Enter your diagnosis: ")
        query = "INSERT INTO patient (firstname, lastname, receiptdate, wardId, doctorId, diagnosis) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (firstname, lastname, receiptdate, wardId, doctorId, diagnosis)
        cursor.execute(query, values)
        cursor.connection.commit()
    except Exception as e:
        print(e)
