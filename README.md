<br />
<div align="center">
  <a href="https://github.com/Rev-1b/MirGovoritTest">
  </a>

  <h3 align="center">Тех-задание для 'МирГоворит'</h3>

  <p align="center">
    На всякий случай добавляю простенький README, вдруг кто-то реально прочитает.
    <br />
</div>

##Формулировка задания

Нужно разработать небольшое приложение поварской книги на Django, со следующим функционалом:

База данных
В базе данных приложения должен храниться список продуктов. Продукт имеет название, а также целочисленное поле,
хранящее информацию о том, сколько раз было приготовлено блюдо с использованием этого продукта. Также в базе данных
хранятся рецепты блюд. Рецепт имеет название, а также набор входящих в рецепт продуктов, с указанием веса в граммах.

Например - рецепт Сырник, в который входят продукты Творог 200г, Яйцо 50г, Сахар 10г.

Один и тот же продукт, может использоваться в разных рецептах. Один и тот же продукт не может быть использован в
одном рецепте дважды.


Функционал
Приложение должно предоставлять следующие HTTP функции, получающие параметры методом GET

1. add_product_to_recipe с параметрами recipe_id, product_id, weight. Функция добавляет к указанному рецепту указанный продукт с указанным весом. Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.

2. cook_recipe c параметром recipe_id. Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.

3. show_recipes_without_product с параметром product_id. Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм. Страница должна генерироваться с использованием Django templates. Качество HTML верстки не оценивается.

Важно: указанные функции должны быть реализованы в разумной степени эффективно с точки зрения производительности, а
также корректно работать в случае одновременного доступа нескольких пользователей.


Админка
Также средствами Джанго должна быть настроена админка, где пользователь сможет управлять входящими в базу данных
продуктами и рецептами. Для рецептов должна быть возможность редактировать входящие в их состав продукты и их вес
в граммах.

##Как клонировать проект

1. Клонируйте репозиторий
   ```sh
   git clone https://github.com/Rev-1b/MirGovoritTest.git
   ```
2. Активируйте виртуальное окружение
   ```sh
   source venv/bin/activate
   ```
3. Установите зависимости
   ```sh
   pip install -r requirements.txt
   ```
4. Находясь в папке 'MirGovoritTest' поднимите локальный сервер
   ```sh
   python manage.py runserver
   ```

В админку можно зайти по <a href="http://127.0.0.1:8000/admin/"> логин 'admin' и пароль 'admin'.

##О реализации

Создано 2 страницы - главная страница со списком всех доступных команд и страница с таблицей для третьей команды.
При действии 1 или 2 вы будете перенаправлены на главную страницу. В нижней части страницы будет выведена информация о
последнем совершенном действии.

Так как объекты рецептов и продуктов достаются из БД с помощью *get_object_or_404()*, то при неуказании необходимых
аргументов будет возвращена 404 ошибка.

В остальном, все сделано по техзаданию выше.

