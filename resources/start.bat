echo off

echo '### Tworze srodowisko flask:'
call createEnv.bat

echo '### instaluje pakiety'
pip install flask
pip install -r requirements.txt

echo '### Ustawiam zmienne srodowiskowe'
set FLASK_APP=run.py
set FLASK_ENV=development

echo '### Wpisz:  flask run     aby uruchomic aplikacje'


