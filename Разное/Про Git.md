# GIT
В PyCharm есть удобные инструменты для работы напрямую с GitHub,
можно связать, например, новый проект в PyCharm с репозиторием на GitHub, для этого, копируйте путь к репозиторию,
естественно, создав его предварительно, и переходите во вкладку VCS - Git - Clone... затем,
в поле URL вставляете адрес, который берете из GitHub, а в поле Directory указываете путь до папки,
в которой будет лежать ваш проект.

После этого скорее всего вас попросят залогиниться на GitHub из pyCharm (но это не точно,
возможно, попросят на другой стадии, просто не забывайте логин и пароль от аккаунта),
следующая работа очень проста, по right-click в поле проекта у вас появляется
дополнительная вкладка в меню "Git", в ней:

+ Git - Add -- добавить файл (физически этот файл уже может быть создан у вас локально).При создании нового файла, система сразу предлагает использовать эту команду;
+ Git - Commit -- сделать коммит, команда выдает форму с возможностью ввести комментарий;
+ Git - Repository - Push -- отправить все изменения текущие на сервер.

###### На Github есть отличные уроки по работе с репозиторием.
Надо, чтобы уже был аккаунт на github, потом выбираем курс, и бот от гитхаба создает
в вашем аккаунте учебный репозиторий, а потом дает через него задания, которые надо сделать.
Полное впечатление, что работаешь с кем-то в команде и получаешь задания. 

[Github Learning Lab](https://lab.github.com/)

###### Создаем в пишарме файл **.gitignore**
В нем будет список файлов и папок, которые не надо отслеживать системой контроля версий.
Т.к. их не надо выкладывать и отслеживать, то пишем в него:

    /venv/
    /.idea/

###### Шпаргалка по git
http://rogerdudler.github.io/git-guide/index.ru.html

https://git-scm.com/book/ru/v2/

https://learngitbranching.js.org/
