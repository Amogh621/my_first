#import os
import subprocess

file = open("s3testlog.txt","w+")
cmd = "aws s3 ls amogh-s-baalti"
cmd_var = subprocess.check_output(cmd)
#file.write(os.system(cmd)) #os.system(cmd) gives 0 as output
cmd_res_str = str(cmd_var)
file.write(cmd_res_str)
file.close()
