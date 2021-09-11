from genericpath import isdir
from os import getcwd,listdir,system
from sched import Event
from time import sleep

class Usuario:

    def getInputUser(self,message="Ingrese el path de donde estan los archivos:\n"):
        inputUser = input(message)
        return inputUser

    def verifyOption(self,option):
        try:
            valueInt = int(option)
            return valueInt
        except ValueError:
            system("cls")
            
    def messageHelps(self):
        system("cls")
        print("Elija una opción")
        print("1- El programa organizara los archivos en la carpeta donde se esta ejecutando\n2- Se le pedira una ruta para que organizara los archivos qu esten en esa ruta\n0-Salir el programa")


#This class it's manager all relationship with extensions and names files
class Files:
    #This dicctionary that compuesto by a keys = "extensions" and values = "file names" 
    files = {}
    #aqui iria la ruta donde estan los archivos que quiero mover
    pathFilesMove = getcwd()
    #este método agrupa todas las demás métodos para 
    #extraer el script,extraer las extensiones y los listar los nombres de archivos
    def execution(self):
        from os.path import basename
        from os import getpid
        from psutil import Process
        filesDirectory = listdir(path=Files.pathFilesMove)   
        nameExecutable = Process(getpid())
        myScript = (basename(__file__),nameExecutable.name(),"config.json")
        filesDirectory = self.deleteMyScript(filesDirectory,myScript)
        self.changeSlash()
        self.extracExtension(filesDirectory)

    def extracExtension(self,listFiles):
        for file in listFiles:
            extensions = ""
            for point in reversed(range(len(file))):
                if file[point] == ".":
                    extensions = file[point+1:]
                    self.addNameFiles(extensions,file[:point])
                    break

    def changeSlash(self):
        import re
        pattern = r"\\"
        path = Files.pathFilesMove
        newPath = re.sub(pattern,"/",path)
        Files.pathFilesMove = newPath

    def deleteMyScript(self,listFiles,myscript):
        for names in myscript:
            if names  in listFiles:
                listFiles.remove(names)
        return listFiles
        
    def addNameFiles(self,key,value):
        if key in Files.files.keys():
            Files.files[key].append(value)
        else:
            Files.files[key] = [value]

#This class it's manager all relationship with directories and save files into directories
class Directories:    

    def __init__(self, folders):
        #{"extensions:files with itself extensions"}
        self.folder = folders
        #amount files did move
        self.cantFilesMoves = 0
        self.filesRepeat = []

    def verifyFolder(self):
        try:
            from os import mkdir
            from os.path import isdir
            #itero sobre las extenciones con nombres de archivos
            for nameFolder in self.folder.keys():
                #verifico si esta el la carpeta esta en esa ruta
                if isdir(Files.pathFilesMove+"/"+nameFolder):
                    self.moveFiles(nameFolder)
                else:
                   mkdir(Files.pathFilesMove+"/"+nameFolder.upper())
                   self.moveFiles(nameFolder)
        except:
            pass

    #folder es la extensión del archivo que al mismo tiempo es el nombre de la carpeta                
    def moveFiles(self,folder):
        from shutil import move
        from os.path import isdir
        #self.folder es el diccionario con los archivos
        for files in self.folder[folder]:
            fileCopy = Files.pathFilesMove+"/"+folder
            if not files+"."+folder in listdir(fileCopy):
                move(Files.pathFilesMove+"/"+files+"."+folder,Files.pathFilesMove+"/"+folder) 
                self.cantFilesMoves +=1
            else:
                self.filesRepeat.append(files+"."+folder)
        del self.folder[folder]
        sleep(2.5)

    def detailsOperation(self,directorio,d=False):
        print("Se han movido [",self.cantFilesMoves,"] archivos del directorio ",directorio)
        if len(self.filesRepeat) > 0 and d:
            print("Los siguiente/s archivo/s se han eliminados por estar repetido/s")
            for files in self.filesRepeat:
                print("[",files,"]")
        sleep(3.5)
    
    #f = the path input main
    def deleteFiles(self,f):
        self.deleteFilesRepeat(f)

    def deleteFilesRepeat(self,f):
        from os import remove
        for files in self.filesRepeat:
            remove(f+"/"+files)

from json import load

config = None
with open("config.json") as f:
    config = load(f)

def run():
    global config
    if len(config["directorios"]) > 0:
        from os.path import isdir
        for directorio in config["directorios"]:
            if isdir(directorio):
                Files.pathFilesMove = directorio
                f = Files()
                f.execution()
                obj_directorio = Directories(Files.files)
                for i in range(len(obj_directorio.folder)):
                    obj_directorio.verifyFolder()
                if len(obj_directorio.filesRepeat) > 0 and config["delete"] == 1:
                    obj_directorio.deleteFiles(Files.pathFilesMove)
                if config["delete"] == 1:
                    obj_directorio.detailsOperation(directorio,d=True)
                else:
                    obj_directorio.detailsOperation(directorio)

if config["event"]["repeat"] == 1:
    from sched import scheduler
    from time import time,sleep
    obj = scheduler(time,sleep)
    while True:
        obj.enter(config["event"]["delay"],1,run())
else:
    run()