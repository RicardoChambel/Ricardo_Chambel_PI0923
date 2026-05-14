@echo off
cd /d "%~dp0"
npx mb --configfile imposter\mountebank.json --allowInjection
pause
