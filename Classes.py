import os

#For my reference, os.walk returns a generator, that creates a tuple of values (current_path, directories in current_path, files in current_path).
#Uses the os.walk function that returns:
#r = root directory
#d = a list with the subdirectories in the root directory
#f = a list with all the files in the root directory
#Pulled on 23 Dec 2022 and merged on 23 Dec 2022

class FindArgs:
   """docstring for FindArgs"""
   def __init__(self, searchstring, pth):
      #super(FindArgs, self).__init__()
      self.searchstring = searchstring
      self.pth = pth
   #def __str__(self):
      #return f"{self.searchstring}("drive: "{self.drivename})"
      
inp = input("Enter File Search String eg COB: ")
drivename = input("Filepath or drivename (eg if you want to search drive c, enter c:\\\\ or give full path like c:\\user\\etc) : ")
arguments = FindArgs(inp,drivename)
print("***********************************************")
print("These are the Parameters")
print("Search String: ", arguments.searchstring)
print("Drivename or Path: ", arguments.pth)
print("***********************************************")
thisdir = os.getcwd()
counter = int(0)
def findfiles(inp,drivename,counter):
   for r, d, f in os.walk(arguments.pth): 
      print("Searched Directory: ", r)
      print("Subdirectories Present: ", d)
      print("List of Files present: ", f)
      print("------------------------------------------")
      for file in f:
         filepath = os.path.join(r, file)
         if inp in file:
            counter = counter + 1
            #print(os.path.join(r, file))
            print(filepath)
            #print("Searched Directory: ", r)
            #print("Subdirectories Present: ", d)
            #print("List of Files present: ", f)
            print("File: ", file)
            print("------------------------------------------")
   print(f"{counter} files are present")
findfiles(arguments.searchstring,arguments.pth,counter)
print("Current working dir:", thisdir)
