print('Enter name of the file:')
xl = input("name:")
        # read all content from a file using read()
f = open(xl, "a")
file = open(xl, 'r')
content = file.read()
        # check if string present or not
if '1=1' in content:
    print('SQL INJECTION ATTACK DETECTED\n1=1 found ')
elif 'OR' in content:
    print('SQL INJECTION ATTACK DETECTED\nOR found ')
elif 'INSERT' in content:
    print('SQL INJECTION ATTACK DETECTED\nINSERT found ')
elif 'SELECT' in content:
    print('SQL INJECTION ATTACK DETECTED\nSELECT found ')
elif 'WHERE' in content:
    print('SQL INJECTION ATTACK DETECTED\nWHERE found ')
elif 'union' in content:
    print('SQL INJECTION ATTACK DETECTED\nunion found ')
elif 'alert' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\nalert found ')
elif 'script' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\nscript found ')
elif 'ALERT' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\nALERT found ')
elif 'SCRIPT' in content:
    print('CROSS SITE SCRIPTING ATTACK DETECTED\nSCRIPT found ')
elif 'ECHO' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nECHO found ')
elif 'DIR' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nDIR found ')
elif 'LS' in content:
    print('COMMAND INJECTION ATTACK ATTACK DETECTED\nLS found ')
elif 'CP' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nCP found ')
elif 'CAT' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nCAT found ')
elif 'TYPE' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nTYPE found ')
elif 'type' in content:
    print('COMMAND INJECTION ATTACK DETECTED\ntype found ')
elif 'cat' in content:
    print('COMMAND INJECTION ATTACK DETECTED\ncat found ')
elif 'cp' in content:
    print('COMMAND INJECTION ATTACK DETECTED\ncp found ')
elif 'ls' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nls found ')
elif 'dir' in content:
    print('COMMAND INJECTION ATTACK DETECTED\ndir found ')
elif 'echo' in content:
    print('COMMAND INJECTION ATTACK DETECTED\necho found ')
elif '../' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n../ found ')
elif '/etc/passwd' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n/etc/passwd found ')
elif '/' in content:
    print('local file inclusion and remote file inclusion ATTACK DETECTED\n/ found ')
elif 'ID' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nID found ')
elif 'id' in content:
    print('COMMAND INJECTION ATTACK DETECTED\nid found ')
elif 'nikto' in content:
    print('NIKTO DETECTED\nnikto found ')
else:
    print('No threat Detected')