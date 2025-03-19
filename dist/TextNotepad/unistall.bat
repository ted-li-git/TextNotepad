@echo off
title TextNotepad卸载向导
echo 即将为你卸载TextNotepad
pause
del "%USERPROFILE%\Desktop\TextNotepad.lnk"
rd /s /q %cd%
echo 卸载完毕！
pause