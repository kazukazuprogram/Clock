pyinstaller -w -F clock.pyw
copy dist\clock.exe . /Y
rd build /s /q
rd dist /s /q
del clock.spec /Q
