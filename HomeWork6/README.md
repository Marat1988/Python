# <b>Home work6</b>

Задание 1.<br>

Необходимо пропарсить данные про страны Европы по данной ссылке:<br>
https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D1%8B_%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D1%8B_%D0%BF%D0%BE_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E<br>
(Страны Европы по населению)<br>



Данные надо сохранить в следующем виде:<br>
JSON-файл.<br>
{@название страны@: <br>
	{flag: @ссылка на флаг в общей папке img@,<br>
	is_growth: @true or false@,<br>
	population: @население@}<br>
}<br>
Папка для флагов должна лежать рядом с JSON файлом в папке img