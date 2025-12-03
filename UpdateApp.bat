@echo off
REM --- Fetch in pull najnovejše spremembe ---
git fetch
git pull

echo.
echo SKRIPTA JE POSODOBLJENA NA NAJNOVEJSO VERZIJO.
echo.
echo IZVEDLO SE BO NADGRADNJE PAKETOV....
echo.

cmd /k "cd /d %~dp0\.venv\Scripts & call activate & cd /d %~dp0 & python -m pip install --upgrade pip & python -m pip install -r requirements.txt

pause
