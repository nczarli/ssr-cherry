import os
import sys
import subprocess


theta_s = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for i in range(len(theta_s)):
    subprocess.call(['python', 'main_cifar_own.py', 
                     '--dataset', 'runtime_cifar_theta_s',
                     '--theta_s', str(theta_s[i])])

