

def buildPythonTable(newfile,oldfile,name):
	with open(newfile, 'w') as outfile, open(oldfile, 'r') as infile:
		lineCounter = 0
		atomCounter = 1
		newLine = ""
		outfile.write('icos'+name+' = [')
		lines = infile.readlines()
		for line in lines:

			newLine += line.strip()
			lineCounter += 1
			s = ',' if lineCounter < 3 else ''
			newLine += s
			if lineCounter == 3:
				outLine = "("+newLine+")"
				atomCounter+=1
				ss = ',' if atomCounter <= len(lines)/3 else ''
				outLine += ss
				outfile.write(outLine)
				lineCounter = 0
				newLine = ""
		outfile.write(']')

def main():
	covs=['72','92','122','132']
	for c in covs:
		buildPythonTable('out'+c,'rawxyz'+c+'.txt',c)

if __name__== "__main__":
  main()