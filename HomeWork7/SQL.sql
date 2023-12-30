DROP DATABASE IF EXISTS hospital;

CREATE DATABASE hospital;

USE hospital;

/*Специализация*/
CREATE TABLE specialization
(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL CHECK (name <> ''),
    CONSTRAINT PK_specialization_Id PRIMARY KEY (id),
    CONSTRAINT QU_specialization_name UNIQUE (name)
);
/*Палата*/
CREATE TABLE ward
(
	id INT NOT NULL AUTO_INCREMENT,
    number INT NOT NULL CHECK (number > 0),
    places INT NOT NULL CHECK (places > 0),
    CONSTRAINT PK_ward_Id PRIMARY KEY (id)
);
/*Врачи*/
CREATE TABLE doctor
(
	id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(50) NOT NULL CHECK (firstname<>''),
    lastname VARCHAR(50) NOT NULL CHECK (lastname <> ''),
    salary INT NOT NULL CHECK (salary > 0),
    holiday BIT DEFAULT 0,
    specializationId INT NOT NULL,
    CONSTRAINT PK_doctor_id PRIMARY KEY (id)
);
/*Пациенты*/
CREATE TABLE patient
(
    id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(50) NOT NULL CHECK (firstname<>''),
    lastname VARCHAR(50) NOT NULL CHECK (lastname <> ''),
    receiptdate DATE NOT NULL,
    wardId INT NOT NULL,
    doctorId INT NOT NULL,
    diagnosis VARCHAR(200) NOT NULL,
    CONSTRAINT PK_patient_id PRIMARY KEY (id)
);

/*Связи между таблицами*/
ALTER TABLE doctor
ADD CONSTRAINT FK_doctor_specializationId FOREIGN KEY (specializationId) REFERENCES specialization(id) ON DELETE CASCADE;

ALTER TABLE patient ADD CONSTRAINT FK_patient_wardId FOREIGN KEY (wardId) REFERENCES ward(id) ON DELETE CASCADE;
ALTER TABLE patient ADD	CONSTRAINT FK_patient_doctorId FOREIGN KEY (doctorId) REFERENCES doctor(id) ON DELETE CASCADE;

/*Тестовые данные*/
INSERT INTO specialization (name)
VALUES ('Хирург');

INSERT INTO ward (number, places)
VALUES (13, 7);

INSERT INTO doctor (firstname, lastname, salary, holiday, specializationId)
VALUES ('Марат', 'Тухтаров', 1000000, 0, 1);

INSERT INTO patient (firstname, lastname, receiptdate, wardId, doctorId, diagnosis)
VALUES ('Максим', 'Пономаренко', DATE_ADD(NOW(), INTERVAL 1 DAY), 1, 1, 'Перелом руки');

INSERT INTO patient (firstname, lastname, receiptdate, wardId, doctorId, diagnosis)
VALUES ('Виталий', 'Белоусов', DATE_ADD(NOW(), INTERVAL 2 DAY), 1, 1, 'Перелом ноги');

INSERT INTO patient (firstname, lastname, receiptdate, wardId, doctorId, diagnosis)
VALUES ('Иван', 'Зорин', DATE_ADD(NOW(), INTERVAL 3 DAY), 1, 1, 'Перелом ребер');

INSERT INTO patient (firstname, lastname, receiptdate, wardId, doctorId, diagnosis)
VALUES ('Сергей', 'Калашников', DATE_ADD(NOW(), INTERVAL 4 DAY), 1, 1, 'Воспаление хитрости');

INSERT INTO patient (firstname, lastname, receiptdate, wardId, doctorId, diagnosis)
VALUES ('Никита', 'Рудяченко', DATE_ADD(NOW(), INTERVAL 5 DAY), 1, 1, 'Перелом шей');

DELIMITER $$

/*Триггер на таблицу*/
-- Создаем триггер 'check_available_places'
DELIMITER $$
CREATE TRIGGER check_available_places BEFORE INSERT ON patient
FOR EACH ROW
BEGIN
    DECLARE total_places INT;
    DECLARE occupied_places INT;
    
    -- Получаем общее количество мест в палате
    SELECT places INTO total_places FROM ward WHERE id = NEW.wardId;
    
    -- Получаем количество занятых мест в палате
    SELECT COUNT(*) INTO occupied_places FROM patient WHERE wardId = NEW.wardId;
    
    -- Проверяем, есть ли свободные места
    IF occupied_places >= total_places THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'All places in the ward are occupied.';
    END IF;
END$$
DELIMITER ;