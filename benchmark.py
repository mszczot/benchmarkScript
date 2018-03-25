#!/usr/bin/env python3
import subprocess
import os

DEVNULL = open(os.devnull, 'wb', 0)

solversDir = '/home/ubuntu/solvers/'
#paths to solvers
pyglaf = solversDir + 'pyglaf/pyglaf.py'
ArgSemSat = solversDir + 'ArgSemSATS/ArgSemSAT'

solvers = [pyglaf, ArgSemSat]

#mapping of benchmark frameworks to tasks
tasks = {
	'A' : ['DS-PR', 'EE-PR', 'EE-CO'],
	'B' : ['DS-ST', 'DC-ST', 'SE-ST', 'EE-ST', 'DC-PR', 'SE-PR', 'DC-CO']
}

benchmarkPath = '/home/ubuntu/A/1/'

for solver in solvers:
	for benchmark in tasks:
		for task in tasks[benchmark]:
			for argumentFramework in os.listdir(benchmarkPath):
				if os.path.splitext(argumentFramework)[1] == '.tgf':
					if 'DS' not in task and 'DC' not in task:
						subprocess.Popen(
							[solver, 
							'-f', benchmarkPath +  argumentFramework, 
							'-p', task, 
							'-fo', 'tgf'], stdout=DEVNULL, stderr=subprocess.STDOUT)
						print(solver)

