import os
import platform


with open("output.txt", "a") as f:
    for value in platform.uname():
        f.write(value + '\n')


        
        