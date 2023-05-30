# ; Протокол HTTP(HyperText Transfer Protocol) - протокол передачи гипертекста

# ; Клиент <-> Сервер

# ; HTTP - 1. GET(метод запроса для получения данных и возврат этих данных клиенту)
# ;     2. POST(метод для создания чего то)
# ;     3. PUT(метод для полного изменения чего либо)
# ;     4. PATCH(метод для частичного изменения)
# ;     5. DELETE(удаляет что то)


# ; Привет, мир! -> PUT() -> Обновленный!
# ; Привет, мир! -> PATCH() -> Привет. Мир!

# ; Запрсо/статус ответа:
# ;     Запрос(Request):
# ;     GET http://35.127.18.190/all_books/ HTTP 1.1
# ;     POST http://mysite.com/all_books/1/buy/ < URL
    
# ;     Заголовки(Headers):
# ;     Host: http://mysite.com/all_books
# ;     Content-Type: text/html; charset=UTF-8


# ;     http://mysite.com/all_books/1/buy


# ; Список статусов:

# ; 1xx - Информационные
# ; 2xx - Успешно(200(ОК), 201(Создано))
# ; 3xx - Перенаправление
# ; 4xx - Ошибка клиента(404(Страница не найдена))
# ; 5xx - Ошибка сервера(500(Внутренняя ошибка сервера))