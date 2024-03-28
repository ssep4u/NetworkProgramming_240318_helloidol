# helloidol

---

1. startproject helloidol
   1. python -m pip install django~=4.2
   2. django-admin startproject _helloidol_ .
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. helloidol/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달: urls -> views -> (models -> )templates
   - 코드 작성: (models -> )views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4. -> templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
---
5. startapp 아이브
   1. Terminal
      1. python manage.py startapp 아이브
   2. helloidol/settings.py
      1. '아이브',   in INSTALLED_APPS
6. 아이브/
   1. views
      1. show_유진()
      2. show_원영()
   2. templates/아이브/
      1. 유진.html
         1. title: 아이브 - 유진
         2. h1: 아이브
         3. h2: 유진
         4. img: 유진 프로필 사진
            1. border-radius: 50%;
      2. 원영.html
   3. urls
      1. 아이브/ -> 유진/ -> show_유진()
      2. 아이브/ -> 원영/ -> show_원영()








