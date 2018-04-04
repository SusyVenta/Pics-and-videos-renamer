import exifread
import os
import re
import datetime
import shutil
path="C:\Users\Susy\Desktop\Prova foto"
for i in os.listdir(path):
    fpath=os.path.join(path, i)
    r =re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}.[0-9]{2}.[0-9]{2}')
    if r.match(os.path.basename(i)):
        print "No need to rename: "+os.path.basename(i)
    elif not r.match(os.path.basename(i)):
        try:
            with open (fpath,"rb") as f:
                tags = exifread.process_file(f)
                for tag in tags.keys():
                    if tag == "EXIF DateTimeOriginal":
                        new_name =(str(tags[tag])[:10]).replace(":","-")+(str(tags[tag])[10:]).replace(":",".")
                        file_name, file_ext=os.path.splitext(i)
                        exif_name="%s%s" %(new_name,file_ext)
                        new_path=os.path.join(path, exif_name)
                        a=1
                        for i in os.listdir(path):
                            if os.path.exists(new_path)==False:
                                try:
                                    os.rename(fpath, new_path)
                                    print file_name +" renamed as: "+exif_name
                                except:
                                    shutil.move(fpath, new_path)
                                    print file_name +" renamed as: "+exif_name
                            else:
                                def doubles_exif():
                                    pass
                                doubles_exif()
                                new_name=new_name+"-"+str(a)
                                exif_name="%s%s" %(new_name,file_ext)
                                new_path=os.path.join(path, exif_name)
                                if os.path.exists(new_path)==False:
                                    try:
                                        os.rename(fpath, new_path)
                                        print file_name +" renamed as: "+exif_name
                                    except:
                                        shutil.move(fpath, new_path)
                                        print file_name +" renamed as: "+exif_name
                                else:
                                    a+=1
                                    doubles_exif()
                                                      
        except:
            try:
                os.remove(fpath)
                print file_name +" renamed as: "+exif_name  
            except:
                pass
        else:
            try:
                file_name, file_ext=os.path.splitext(i)
                mtime=os.stat(fpath).st_mtime
                n_noexif=(str(datetime.datetime.fromtimestamp(mtime))[:19]).replace(":",".")
                name_noexif= "%s%s"%(n_noexif,file_ext)
                path_noexif=os.path.join(path, name_noexif)
                a=1
                for i in os.listdir(path):
                    if os.path.exists(path_noexif)==False:
                        try:
                            os.rename(fpath, path_noexif)
                            print file_name+" renamed as: "+name_noexif
                        except:
                            shutil.move(fpath, path_noexif)
                            print file_name+" renamed as: "+name_noexif
                    else:
                        def doubles_noexif():
                            pass
                        doubles_noexif()
                        n_noexif=n_noexif+"-"+str(int(a))
                        name_noexif= "%s%s"%(n_noexif,file_ext)
                        path_noexif=os.path.join(path, name_noexif)
                        if os.path.exists(path_noexif)==False:
                            try:
                                os.rename(fpath, path_noexif)
                                print file_name+" renamed as: "+name_noexif
                            except:
                                shutil.move(fpath, path_noexif)
                                print file_name+" renamed as: "+name_noexif
                        else:
                            a+=1
                            doubles_noexif()
                            
            except:
                try:
                    os.remove(fpath)
                    print file_name+" renamed as: "+name_noexif
                except:
                    pass
