@echo off
setlocal

echo === Check update ===
git fetch

for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD') do set BRANCH=%%i

for /f "tokens=*" %%i in ('git rev-parse HEAD) do set LOCAL_COMMIT=%%i
for /f "tokens=*" %%i in ('git rev-parse origin/%BRANCH%') do set REMOTE_COMMIT=%%i

if "%LOCAL_COMMIT%"=="%REMOTE_COMMIT%" (
	echo No updates.
) else (
	echo found new updates.
	set /p ANSWER=Install? (y/n):
	set "ANSWER=%ANSWER: =%"
	if /i "%ANSWER%"=="y" (
		echo === Project updates ===
		git pull
		
		echo === Updates finish ===
	) else (
		echo Skip update by user
	)
)

pause