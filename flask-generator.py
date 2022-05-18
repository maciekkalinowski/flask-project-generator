from os import mkdir, rename
from shutil import copytree, ignore_patterns, Error
from unicodedata import name


appName = ''
appName = input('Podaj nazwe aplikacji: ')


try:
    copytree('resources', appName, ignore=ignore_patterns('env', '__pycache__', '*.sqlite'), dirs_exist_ok= False)
except FileExistsError as err: 
    print(err)


'''
namesToChange = []
namesToChange.append(appName +'/' + 'appName')
namesToChange.append(appName +'/appName.ini')
#print(namesToChange)
for elem in namesToChange:
    src = elem
    dest = str(elem).replace('appName', appName)
    rename(src, dest)

filesToChange = []
filesToChange.append(appName +'/run.py')
filesToChange.append(appName +'/' + appName + '.ini')
filesToChange.append(appName +'/Dockerfile')
filesToChange.append(appName +'/boot.sh')

filesToChange.append(appName + '/' + appName + '/templates/base.html')
filesToChange.append(appName + '/' + appName + '/__init__.py')
filesToChange.append(appName + '/' + appName + '/views.py')

for elem in filesToChange:
    print('Modyfikuje tresc pliku: '+ elem)
    file = open(elem, 'r')
    fileContent = file.read()   
    file.close()

    file = open(elem, 'w')
    fileContent = fileContent.replace('appName', appName)
    print('################')
    print(fileContent)
    file.write(fileContent)
    file.close


#print(filesToChange)
'''

'''
# zmiana nazwy folderu z aplikacja
src = appName +'/' + 'appName'
dest = appName +'/' + appName
rename(src, dest)

# zmiana nazwy pliku .ini
src = appName +'/' + 'appName.ini'
dest = appName +'/' + appName + '.ini'

rename(src, dest)
'''