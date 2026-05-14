@echo off
cd /d "%~dp0PowerChordAPI"
dotnet restore
dotnet run --urls "http://localhost:5163"
pause
