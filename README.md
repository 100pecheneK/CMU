# CMU
 
Установка
====
# Установить:
1) В settings.py
2) В urls.py
     ```python
    path('CMU/', include('CMU.urls')),
    ```
3) ./manage.py makemigrations; ./manage.py migrate
---
# Настроить
1) Изменить в services/cutUrl.py в 11 строчке ссылку
2) Вставить куда надо форму изменив в ней input[value] на ссылку объекта (можно убрать тег ```<p>```)
    ```html
    <form method="POST" action="{% url 'cmu:register_url' %}" class="cmu_form" hidden>
        {% csrf_token %}
        <input type="text" class="cmu_obj_url" value="https://ссылка" hidden>
        <button type="submit" class="cmu_button btn btn-primary" data-toggle="tooltip" data-placement="bottom"
                title="Получить ссылку"><i class="far fa-copy"></i></button>
        <p class="cmu_new_url"></p>
    </form>
    ```
3) Подключить зависимости (Убедись, что твои скрипты не младше моих) + иконки проверь
    ```
    <script
        src="https://code.jquery.com/jquery-3.4.1.js"
        integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU="
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
            integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
            crossorigin="anonymous"></script>
    
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
            integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
            crossorigin="anonymous"></script>
    ```
4) Подключить cmu_script.js 
---
# Готово
