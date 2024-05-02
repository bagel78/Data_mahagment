* База данных

** Сущность пользователь

Поле - тип данных

id - INT(11) * AUTO_INCREMENT
Фамилия - VARCHAR(60) *
Имя - VARCHAR(30) *
Отчество - VARCHAR(30)
Дата рождения - DATE * 
Email - VARCHAR(50) *
Телефон - CHAR(20) 
Форма обучения - ENUM("очная", "заочная", "очно-заочная") *
Статус - TINYINT(1) * DEFAULT = 1
Пароль - VARCHAR(32) *
ID_группы - INT(11) *

** Сущность факультет

id - INT(11) * AUTO_INCREMENT
Название - VARCHAR(100) *

** Сущность группа

id - INT(11) * AUTO_INCREMENT
Название - VARCHAR(100) *
ID_факультета - INT(11) *