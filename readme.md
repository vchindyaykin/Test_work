Всю работу выполняем на отдельных ветках, после завершения, выкатываем pull request на ревью

Сева:  
- [UI] Покрыть тестами форму: https://demoqa.com/automation-practice-form  
- [UI] Покрыть тестами модальные окна: https://demoqa.com/modal-dialogs  
- [UI] Покрыть тестами динамические элементы: https://demoqa.com/dynamic-properties
- [UI] Покрыть тестами сайт: https://www.saucedemo.com/
- [API] Покрыть тестами api: https://restful-booker.herokuapp.com/apidoc/index.html#api-Auth  
  
Влад:  
- [UI] Покрыть тестами чекбоксы: https://demoqa.com/checkbox  
- [UI] Покрыть тестами таблицу: https://demoqa.com/webtables  
- [UI] Покрыть тестами скачивание и загрузку файла: https://demoqa.com/upload-download  
- [UI] Покрыть тестами сайт: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/  
- [API] Покрыть api тестами ручки BookStore: https://demoqa.com/swagger/#/  

Соответственно для demoqa нужно описать свою страницу, разделите между собой обязанности для её создания.    
Для API тестов тоже необходимо описать базовый модуль с запросами (GET, POST, PUT, DELETE) и добавить в них логирование,
обработку ошибок и т.д. и уже на его основе, создавать модуль в директории lib под свой сервис и покрывать всё тестами

Распределите между собой обязанности, кто-то делает страницу для сайта demoqa, кто-то описывает базовый модуль для 
работы с API
