print('Enter name of the file:')
xl = input("name:")
        # read all content from a file using read()
f = open(xl, "a")
file = open(xl, 'r')
content = file.read()
        # check if string present or not
if '1=1' in content:
    print('SQL INJECTION ATTACK DETECTED\n 1=1 found in log')
elif 'OR' in content:
    print('SQL INJECTION ATTACK DETECTED\n OR found in log')
elif 'INSERT' in content:
    print('SQL INJECTION ATTACK DETECTED\n INSERT found in log')
elif 'SELECT' in content:
    print('SQL INJECTION ATTACK DETECTED\n SELECT found in log')
elif 'WHERE' in content:
    print('SQL INJECTION ATTACK DETECTED\n WHERE found in log')
elif 'union' in content:
    print('SQL INJECTION ATTACK DETECTED\n union found in log')
elif 'alert' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n alert found in log')
elif 'script' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n script found in log')
elif 'ALERT' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n ALERT found in log')
elif 'SCRIPT' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n SCRIPT found in log')
elif 'ECHO' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n ECHO found in log')
elif 'DIR' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n DIR found in log')
elif 'LS' in content:
    print('COMMAND INJECTION ATTACK ATTACK DETECTED\n LS found in log')
elif 'CP' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n CP found in log')
elif 'CAT' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n CAT found in log')
elif 'TYPE' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n TYPE found in log')
elif 'type' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n type found in log')
elif 'cat' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n cat found in log')
elif 'cp' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n cp found in log')
elif 'ls' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n ls found in log')
elif 'dir' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n dir found in log')
elif 'echo' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\n echo found in log')
elif '../' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n ../ found in log')
elif '/etc/passwd' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n ALERT found in log')
elif '/' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n ALERT found in log')
elif 'ID' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n ID found in log')
elif 'id' in content:
    print('COMMAND INJECTION ATTACK DETECTED\n id found in log')
elif 'nikto' in content:
    print('NIKTO DETECTED\n nikto found in log')
else:
    print('string does not exist')