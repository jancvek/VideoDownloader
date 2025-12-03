@echo off
REM --- Fetch in pull najnovejše spremembe ---
git fetch
git pull

cmd /k "cd /d %~dp0\.venv\Scripts & call activate & cd /d %~dp0 & python -m pip install --upgrade pip & python -m pip install -r requirements.txt

echo.
echo Skripta je posodobljena
pause
