class login:
    def __init__(self,id,pas):
        self.id="admin"
        self.pas="admin"

    def check(id,pas):
        print self.id
        print lod.id
        if(self.id==log.id and self.pas==log.pas):
            print "Login success!"


log=login("","")
log.check(raw_input("Enter Login ID:"),
        input("Enter password: "))

print "Login Page"
Error: Enter Login ID:admin Enter password: admin

Traceback (most recent call last):
  File "C:/Python27/login.py", line 15, in <module>
    input("Enter password: "))
  File "<string>", line 1, in <module>
NameError: name 'admin' is not defined