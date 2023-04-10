import time
import subprocess
import sys
def fucking_repeat_cord():
    cycle = 0 
    while cycle < 10 :
        print("jk die")
        time.sleep(2)
        print("jk die")
        time.sleep(2)
        cycle = cycle + 1   
user_input_mod = int(input("enter your mod:\n"))
if user_input_mod == 1 :
    with open("cfg.ini", "r") as f:
        for line_GenshinPath in f:
            if line_GenshinPath.startswith("GenshinPath"):
                genshin_path = line_GenshinPath.split("=")[1].strip() 
                genshin_path = genshin_path.split(".exe")[0] + ".exe"
                break
    print(genshin_path)
elif user_input_mod == 2 :
    genshin_path = "0"
    user_input_path = input("enter your genshin path:\n").strip()
    genshin_path = user_input_path
    with open("cfg.ini", "r+") as f:
        file_content = f.read()
        new_content = file_content.replace("GenshinPath = ", "GenshinPath = " + user_input_path)
        f.seek(0)
        f.write(new_content)
        f.truncate()
    print(genshin_path)
else:
    print("plese enter your mod correctly")
    sys.exit()
subprocess.run (genshin_path, shell=True)
repeat_cord = fucking_repeat_cord()

