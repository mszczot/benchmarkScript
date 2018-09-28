#!/usr/bin/env python3

from os import listdir
import alias
import subprocess
import json

path = '/home/szczocik/Workspaces/Benchmark/B/1/'
# test = {}
# for f in listdir(path):
#     af = alias.read_tgf(path+f)
#     test[f] = {'args': af.get_args_count(), 'attacks': af.get_attacks_count()}
# sorted_dict = sorted(test.items(),key=lambda x: x[1]['args'],reverse=False)

sorted_dict = []

with open('/home/szczocik/Workspaces/bFiles.json', 'r') as file:
    sorted_dict = json.load(file)
    # json.dump(sorted_dict, file)

for k, v in sorted_dict:
   cmd = '/home/szczocik/Workspaces/benchmarkScript/alias/benchmark.py ' + path + k
   print(cmd)
   process = subprocess.Popen('ulimit -t 60; ' + cmd, shell=True)
   out, err = process.communicate()
   print(out)
