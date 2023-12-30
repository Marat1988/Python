import pymysql
import doctor
import ward
import patient
import specialization

try:
    with pymysql.connect(host='localhost', user='root', password='', port=3306, database='hospital') as connection:
        cursor = connection.cursor()
        while True:
            print("Введите 1 для вставки строки в таблицу doctor: ")
            print("Введите 2 для вставки строки в таблицу patient: ")
            print("Введите 3 для вставки строки в таблицу specialization: ")
            print("Введите 4 для вставки строки в таблицу ward: ")
            print("Введите 0 для выхода из программы: ")
            user_choice = input("Ваш выбор: ")
            match user_choice:
                case "1":
                    doctor.insert_doctor(cursor)
                case "2":
                    patient.insert_patient(cursor)
                case "3":
                    specialization.insert_specialization(cursor)
                case "4":
                    ward.insert_ward(cursor)
                case "0":
                    quit()
except Exception as error:
    print(error)
