# 社員管理システム Backend

## 更新履歴

Created 2022/03/22 -20222/03/28

## 開発環境構築

pip install -r requirements.txt
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 777

## 動作確認

post
http://127.0.0.1:8000/api/auth/jwt/create/

header(Authorization: JWT xxxxxxxxx)
get, post
http://127.0.0.1:8000/api/employees

put, delete
http://127.0.0.1:8000/api/employees/<id>
