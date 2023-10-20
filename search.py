print('Enter name of the file:')
xl = input("name:")
        # read all content from a file using read()
f = open(xl, "a")
file = open(xl, 'r')
content = file.read()
        # check if string present or not
if '1=1' in content:
    print('SQL INJECTION ATTACK DETECTED\n 1=1 found ')
elif 'OR' in content:
    print('SQL INJECTION ATTACK DETECTED\n OR found ')
elif 'INSERT' in content:
    print('SQL INJECTION ATTACK DETECTED\n INSERT found ')
elif 'SELECT' in content:
    print('SQL INJECTION ATTACK DETECTED\n SELECT found ')
elif 'WHERE' in content:
    print('SQL INJECTION ATTACK DETECTED\n WHERE found ')
elif 'union' in content:
    print('SQL INJECTION ATTACK DETECTED\n union found ')
elif 'alert' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n alert found ')
elif 'script' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n script found ')
elif 'ALERT' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n ALERT found ')
elif 'SCRIPT' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n SCRIPT found ')
elif 'ECHO' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n ECHO found ')
elif 'DIR' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n DIR found ')
elif 'LS' in content:
    print('COMMAND INJECTION ATTACK ATTACK DETECTED\n LS found ')
elif 'CP' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n CP found ')
elif 'CAT' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n CAT found ')
elif 'TYPE' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n TYPE found ')
elif 'type' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n type found ')
elif 'cat' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n cat found ')
elif 'cp' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n cp found ')
elif 'ls' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n ls found ')
elif 'dir' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n dir found ')
elif 'echo' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n echo found ')
elif '../' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n ../ found ')
elif '/etc/passwd' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n /etc/passwd found ')
elif '/' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n / found ')
elif 'ID' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n ID found ')
elif 'id' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n id found ')
elif 'nikto' in content:
    print('NIKTO DETECTED\n nikto found ')
else:
    print('No threat Detected')