@echo off
title TextNotepadж����
echo ����Ϊ��ж��TextNotepad
pause
del "%USERPROFILE%\Desktop\TextNotepad.lnk"
rd /s /q %cd%
echo ж����ϣ�
pause