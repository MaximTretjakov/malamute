@echo on
REM переходим в папку проекта
cd C:\Users\KARMA\Desktop\Projects\build\questionnaire\questionnaire-master

REM создаём инвармент
python -m venv env

REM активируем созданный ранее инвайрмент
call env\Scripts\activate.bat

REM устанавливаем зависимости
env\Scripts\pip install -r requirements.txt

REM деактивируем созданный ранее инвайрмент
env\Scripts\deactivate.bat