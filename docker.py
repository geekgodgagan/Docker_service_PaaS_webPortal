import os
import subprocess as sp
print("content-type: text/html")
print()
f=cgi.FieldStorage()
cmd = f.getvalue("x")
o = sp.getoutput("sudo {}".format(cmd))
res = ""
if "run" in cmd:
        res = "Container successfully Launched"
        print(res)
if "systemctl start" in cmd:
        o = "Service started successfully"
if "enable" in cmd:
        o = "Service enabled successfully"
if "rm" in cmd:
        print("Deleted Successfully")
if "docker start" in cmd:
        o = "Container started successfully"
if "docker stop" in cmd:
        o = "Container stopped successfully"

print(o)
