import os, filecmp, shutil
from datetime import datetime

startTime = datetime.now()
#b = "/home/pi/stack/Music/REM-Automatic for the people"
#a = "/mnt/storage/Music/REM-Automatic for the people"

b = "/home/pi/stack/Music"
a = "/mnt/storage/Music"

##copy new files and folder
def copy_new_files(dcmp):
    #print('Searching for new files')
    for name in dcmp.left_only:
#        print('new file %s found in %s' % (name, dcmp.left))
        dst = os.path.join(dcmp.right, name)
        src = os.path.join(dcmp.left, name)
        if os.path.isfile(src) == True:
            print('%s is new file' %(src))
            shutil.copy(src,dst)
            print('%s is copied to %s' %(src, dst))
        else:
            print('%s is folder' %(src))
            shutil.copytree(src,dst)
            print('%s is copied to %s' %(src, dst))
#        print('copy new file %s to %s'  % (name, os.path.join(dcmp.right, name)))
    for subdir in dcmp.subdirs.values():
        copy_new_files(subdir)

##Compare existing files by file size
def check_existing_files(dirs_cmp):
    #dirs_cmp = filecmp.dircmp(a,b)
    for file in dirs_cmp.common_files:
        for right_file in sorted(dirs_cmp.right_list):
            if file == right_file:
                rightFileSize = os.path.getsize(os.path.join(dirs_cmp.right, file))                
                dst = os.path.join(dirs_cmp.right, file)
        for left_file in sorted(dirs_cmp.left_list):
            if file == left_file:
                leftFileSize = os.path.getsize(os.path.join(dirs_cmp.left,file))
                src = os.path.join(dirs_cmp.left, file)
        if leftFileSize != rightFileSize:
            shutil.copy(src,dst)
            print('%s copied to %s' %(src, dst))
    for subdir in dirs_cmp.subdirs.values():
        check_existing_files(subdir)
        
dirs_cmp = filecmp.dircmp(a,b)
copy_new_files(dirs_cmp)
check_existing_files(dirs_cmp)



