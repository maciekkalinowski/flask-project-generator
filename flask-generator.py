from os import mkdir, rename
from shutil import copytree, ignore_patterns, Error
from unicodedata import name


appName = ''
appName = input('Podaj nazwe aplikacji: ')


try:
    copytree('resources', appName, ignore=ignore_patterns('env', '__pycache__', '*.sqlite'), dirs_exist_ok= False)
except FileExistsError as err: 
    print(err)



filesToChange = [
    #'run.py',
    #'app.ini',
    #'Dockerfile',
    #'boot.sh',

    '/app/templates/test.html',
    #'/app/__init__.py',
    '/app/views.py'
]
print('Pliki do zmiany zawartosci w folderze ' + appName + ': ' + '\n\t' + str(filesToChange))

for elem in filesToChange:
    elemPath = appName + '/' + elem
    #print('Modyfikuje tresc pliku: /'+ elemPath)
    file = open(elemPath, 'r')
    fileContent = file.read()   
    file.close()

    file = open(elemPath, 'w')
    fileContent = fileContent.replace('APP_NAME', appName)
    #print('################')
    #print(fileContent)
    file.write(fileContent)
    file.close()


'''
namesToChange = [
    #appName + '/app',
    #appName + '/app.ini'
]
print('Elementy do zmiany nazwy: ' + '\n\t' + str(namesToChange))

for elem in namesToChange:
    dest = str(elem).replace('APP_NAME', appName)
    #print(elem)
    #print(dest)
    rename(elem, dest)
'''
