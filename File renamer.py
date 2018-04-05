import exifread
import os
import re
import datetime
import shutil
path="C:\Users\Susy\Desktop\Prova foto"
def rename_curr_file():
    try:
        os.rename(fpath, new_path)
        print file_name +" renamed as:\t"+new_name
    except:
        shutil.move(fpath, new_path)
        print file_name +" renamed as:\t"+new_name
#check if filename is in correct format
for i in os.listdir(path):
    fpath=os.path.join(path, i)
    r =re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}.[0-9]{2}.[0-9]{2}')
    if r.match(os.path.basename(i)):
        print "No need to rename:\t"+os.path.basename(i)
#if file name is not in correct format, try to rename with exif date
    else:
        try:
            with open (fpath,"rb") as f:
                tags = exifread.process_file(f)
                for tag in tags.keys():
                    if tag == "EXIF DateTimeOriginal":
                        exif_name =(str(tags[tag])[:10]).replace(":","-")+(str(tags[tag])[10:]).replace(":",".")
                        file_name, file_ext=os.path.splitext(i)
                        new_name="%s%s" %(exif_name,file_ext)
                        new_path=os.path.join(path, new_name)
                        a=1
                        #check if file with this new name already exists
                        for i in os.listdir(path):
                            if os.path.exists(new_path):
                                exif_name=exif_name+"-"+str(a)
                                new_name="%s%s" %(exif_name,file_ext)
                                new_path=os.path.join(path, new_name)
                                if os.path.exists(new_path):
                                    a+=1
                                else:
                                    rename_curr_file()
                            else:
                                rename_curr_file()                                                          
        except:
            try:
                os.remove(fpath)
                print file_name +" renamed as:\t"+new_name  
            except:
                pass
#if file has no exif date, rename with last mod date
        else:
            try:
                file_name, file_ext=os.path.splitext(i)
                mtime=os.stat(fpath).st_mtime
                n_noexif=(str(datetime.datetime.fromtimestamp(mtime))[:19]).replace(":",".")
                new_name= "%s%s"%(n_noexif,file_ext)
                new_path=os.path.join(path, new_name)
                a=1
                #check if file with this new name already exists
                for i in os.listdir(path):
                    if os.path.exists(new_path):
                        n_noexif=n_noexif+"-"+str(a)
                        new_name= "%s%s"%(n_noexif,file_ext)
                        new_path=os.path.join(path, new_name)
                        if os.path.exists(new_path):
                            a+=1
                        else:
                            rename_curr_file()    
                    else:
                        rename_curr_file()
            except:
                try:
                    os.remove(fpath)
                    print file_name +" renamed as:\t"+new_name  
                except:
                    pass
