#!/usr/bin/env python3
import subprocess
import os

DEVNULL = open(os.devnull, 'wb', 0)

solversDir = '/home/ubuntu/solvers/'
benchmarkPath = '/home/ubuntu/A/1/'

# paths to solvers
pyglaf = solversDir + 'pyglaf/pyglaf.py'
ArgSemSat = solversDir + 'ArgSemSATS/ArgSemSAT'

solvers = [pyglaf, ArgSemSat]

# mapping of benchmark frameworks to tasks
tasks = {
    'A': ['DS-PR', 'EE-PR', 'EE-CO'],
    'B': ['DS-ST', 'DC-ST', 'SE-ST', 'EE-ST', 'DC-PR', 'SE-PR', 'DC-CO']
}


for solver in solvers:
    for benchmark in tasks:
        for task in tasks[benchmark]:
            for argumentFramework in os.listdir(benchmarkPath):
                if os.path.splitext(argumentFramework)[1] == '.tgf':
                    if 'DS' not in task and 'DC' not in task:
                        subprocess.Popen(
                            [solver,
                             '-f', benchmarkPath + argumentFramework,
                             '-p', task,
                             '-fo', 'tgf'], stdout=DEVNULL, stderr=subprocess.STDOUT)
                        print(solver)



"""
A (download, 614MB): DS-PR, EE-PR, EE-CO
B (download, 713MB): DS-ST, DC-ST, SE-ST, EE-ST, DC-PR, SE-PR, DC-CO
C (download, 856MB): DS-CO, SE-CO, DC-GR, SE-GR
D (download, 614MB): DC-ID, SE-ID
E: DS-SST, DC-SST, SE-SST, EE-SST, DS-STG, DC-STG, SE-STG, EE-STG.
"""