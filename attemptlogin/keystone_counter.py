#!/usr/bin/env python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0
loginpass = 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines=keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
        tline = keystone_file_lines[i]
        temp, ipaddress = tline.split("from")
        print('The failure came from IP address ' + ipaddress)
    elif "-] Authorization failed" in keystone_file_lines[i]:
        loginpass +=1
print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful login attempts is ' + str(loginpass))
