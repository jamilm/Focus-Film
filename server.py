import win32com.client as comclt
wsh= comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Notepad") # select another application
while(1):
    wsh.SendKeys("a") # send the keys you want
