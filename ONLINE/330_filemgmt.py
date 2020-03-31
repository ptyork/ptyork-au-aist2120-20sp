import os                 # core filesystem commands are mostly here
import shutil             # additional commands that do useful stuff
from pathlib import Path  # use to easily construct cross-platform path strings

if not os.path.exists('DELETEME'):    # does "DELETEME" exist in PWD?
    os.mkdir('DELETEME')              # if not, create the directory

shutil.copy('330_contacts_v2.py','DELETEME')   # copy a file to a directory
shutil.copy('330_contacts_v2.py','DELETEME\\test.py') # copy/rename a file
#shutil.move()   # not demonstrated, but it's the same idea
os.chdir('DELETEME')   # change the PWD for the script to the DELETEME directory
os.remove('test.py')   # remove a file in teh PWD
os.chdir('..')         # change the PWD back to where we started...not needed

#os.remove('db.db.dat')
#os.removedirs('DELETEME')  # doesn't work if the directory isn't empty
shutil.rmtree('DELETEME')   # delete a directory even if it isnt' empty


# again, a Path object just allows us to work with file paths in a cross-platform
# manner without hassle
p = Path('.')        # get a "path" object for the PWD
print(str(p))        # just prints "." (i.e., PWD)
#dm = '.\\DELETEME'
dm = p / 'DELETEME'  # the / character is "path concatenation"
print(str(dm))       # prints "DELETEME" ... loses the './' because the dot
                     # is the PWD and is "assumed"

h = Path.home()      # every OS has a home directory for a user that is generally
                     # always able to be written to
print(str(h))        # prints "C:\Users\Paul" in my case

temp_dir = h / "temp"
#temp_file = h / "temp" / "temp.txt"
temp_file = temp_dir / "temp.txt"

print(str(temp_dir))       # C:\Users\Paul\temp" in my case
print(str(temp_file))      # C:\Users\Paul\temp\temp.txt" in my case

if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

with open(temp_file, 'w') as fi:
    fi.write('hello world\n')

# Now, (for me) c:\Users\Paul\temp\temp.txt will contain a single line of text...
