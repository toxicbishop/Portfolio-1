@echo off
SETLOCAL

echo 🚀 Starting Portfolio Automation...

:menu
echo.
echo 1. Build and Start Portfolio (Background)
echo 2. View Logs
echo 3. Stop Portfolio
echo 4. Full Cleanup (Delete Volumes/Images)
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo Building and starting containers...
    docker-compose up -d --build
    echo Done! App is running at http://localhost:5000
    goto menu
)
if "%choice%"=="2" (
    docker-compose logs -f
    goto menu
)
if "%choice%"=="3" (
    echo Stopping containers...
    docker-compose down
    goto menu
)
if "%choice%"=="4" (
    echo cleaning up everything...
    docker-compose down -v --rmi all
    goto menu
)
if "%choice%"=="5" (
    exit
)

echo Invalid choice, try again.
goto menu
