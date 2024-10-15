# Case_Lab_ML
Тестовое задание на предстажировку в Гринатом

**Выполнила**: Клинова Мария

Ссылка на веб сервис: https://case-lab-ml-klinova.onrender.com/

# Инструкция по установке локально

Скопируйте проект в свой репозиторий
```bash
git clone https://github.com/TyupTupa/Case_Lab_ML
```
Если модель не загружается, то скачайте text_classification_model.pkl вручную и расположите ее в папке проекта mysite.

Создайте окружение python
```bash
python -m venv venv
```
Активируйте окружение
```bash
venv\Scripts\activate
```
Установите зависимые библиотеки
```bash
pip install -r requirements.txt
```
Перейдите в директорию с django проектом
```bash
cd Case_Lab_ML/mysite
```
Запустите
```bash
python manage.py runserver
```
Послt этого по адресу http://127.0.0.1:8000/ будет запущено веб-приложение. Наслаждайтесь его работой!