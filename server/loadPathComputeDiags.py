import routes
import csv
import os

# load image file paths
with open("int_patients_033116.csv", 'rb') as csvfile:
	pathlist = csv.reader(csvfile, delimiter=',')
	f = open("diagouttest_full.csv",'w')
	# compute diags
	computedDiag = {}
	for i,line in enumerate(pathlist):
		if i != 0:
			path = line[0]
			print path
			newpath = "/home/edb/test_html_server/app/tmp/"+path.split('/')[-1].split('.')[0] + ".jpg"
			print newpath
			os.system(
			"scp tswedish@matlaber3.media.mit.edu:"+path+" "+newpath)
			computedDiag = routes.getDiagRequest(newpath)
			os.system("rm tmp/*.jpg")
			f.write("".join(path +","+str(float(computedDiag[3:-2]))+"\n"))
	f.close()

