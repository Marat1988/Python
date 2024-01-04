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
            print("Введите 5 для обновление информации о докторе")
            print("Введите 6 для обновление зарплаты всех у всех докторов")
            print("Введите 7 для обновление информации о специализации")
            print("Введите 8 для обновление информации о палатах")
            print("Введите 9 для обновления количества мест во всех палатах")
            print("Введите 10 для обновления информации о пациенте")
            print("Введите 11 для обновления инофрмации о докторе у всех пациентов")
            print("Введите 12 для удаления доктора")
            print("Введите 13 для удаления всех докторов")
            print("Введите 14 для удаления специализации")
            print("Введите 15 для удаления всех специализаций")
            print("Введите 16 для удаления палаты")
            print("Введите 17 для удаления всех палат")
            print("Введите 18 для удаления пациента")
            print("Введите 19 для удаления всех пациентов")
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
                case "5":
                    doctor.update_doctor(cursor)
                case "6":
                    doctor.update_all_information_doctors(cursor)
                case "7":
                    specialization.update_specialization(cursor)
                case "8":
                    ward.update_ward(cursor)
                case "9":
                    ward.update_all_information_wards(cursor)
                case "10":
                    patient.update_patient(cursor)
                case "11":
                    patient.update_all_information_patients(cursor)
                case "12":
                    doctor.delete_doctor(cursor)
                case "13":
                    doctor.delete_all_doctors(cursor)
                case "14":
                    specialization.delete_specialization(cursor)
                case "15":
                    specialization.delete_all_specializations(cursor)
                case "16":
                    ward.delete_ward(cursor)
                case "17":
                    ward.delete_all_wards(cursor)
                case "18":
                    patient.delete_patient(cursor)
                case "19":
                    patient.delete_all_patients(cursor)
                case "0":
                    quit()
except Exception as error:
    print(error)
