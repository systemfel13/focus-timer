' VBS (Visual Basic Script): Windows-script for automating tasks, similar to bash-scripts on Linux
' Starts the timer whithout showing the console window

Set objShell = CreateObject("WScript.Shell") ' Creates an object that can run programs and commands
objShell.Run "pythonw main.py", 0, False ' pythonw = runs Python wihout the console window, 0 means hide the window completely, false = the scripts starts the timer and then the scripts exits itself