mkdir release
mkdir release\\icon
mkdir release\\help
copy clock.exe release
copy README.md release
copy clock.conf release
xcopy icon release\\icon
xcopy help release\\help

"C:\Program Files\7-Zip\cmd\7za.exe" a Release.zip release

rd release /s /q
