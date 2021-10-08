from os import listdir
from os import makedirs
from shutil import copyfile

dayFolders=[int(x.replace('Day ', '')) for x in listdir('./') if 'Day ' in x]
lastDay=max(dayFolders) if dayFolders else 0
newDay='Day ' + str(lastDay+1)
makedirs(newDay)
copyfile('./template.py', './'+newDay+'/d'+str(lastDay+1)+'.py')
open(newDay+'/input.txt', 'a').close()
print('Added ' + newDay)
