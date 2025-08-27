import os
import shutil

def delete_from_directory(working_dir, dir):
    joined_path = os.path.join(working_dir, dir)
    abs_path = os.path.abspath(joined_path)
    print("deleted abs path:", abs_path)
    
    if(os.path.exists(joined_path)):
        shutil.rmtree(joined_path)
        os.mkdir(joined_path)
    else:
        raise Exception(f"Delete Error: File path {abs_path} does not exist.")

def copy_to_directory(working_dir, target_dir, copied_dir):
    target_path = os.path.join(working_dir, target_dir)
    copied_path = os.path.join(working_dir, copied_dir)
    if(not os.path.exists(target_path)):
        raise Exception(f"Copy Error: Target path {os.path.abspath(target_path)} does not exist.")
    if(not os.path.exists(copied_path)):
        raise Exception(f"Copy Error: Copied path {os.path.abspath(copied_path)} does not exist.")
    
    traverse_files(copied_path, target_path)
       
    

def traverse_files(copied_path, target_path):
    files = os.listdir(copied_path)
    new_copied_path = ""
    new_target_path = target_path
    for file_name in files:
        # value in listdir only returns file/directory name so needs to be joined to path previously joined
        new_copied_path = os.path.join(copied_path, file_name)
        if(not os.path.exists(new_copied_path)):
             raise Exception(f"Copy Error: no file found at {os.path.abspath(copied_path)}")
        if(not os.path.exists(new_target_path)):
            os.mkdir(new_target_path)
            print("creating directory at", new_target_path)
        # I want to check the previous directory so I update new_target_path after
        new_target_path = os.path.join(target_path, file_name)
        
        if(os.path.isdir(new_copied_path)):
            traverse_files(new_copied_path, new_target_path)
        else:
            print("copied path:", new_copied_path)
            print("target path:", new_target_path)
            shutil.copy(new_copied_path, new_target_path)
            
        


            
