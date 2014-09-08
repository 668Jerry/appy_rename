import os 

def batch_rename(array,path):  

	count = 0

	for fname in os.listdir(path):

		new_fname = str(array[count])+'.png'

		print os.path.join(path, fname)

		os.rename(os.path.join(path, fname), os.path.join(path, new_fname))

		count = count + 1

ins = open( "../random.csv", "r" )

array = []

for line in ins:

	array.append( line[:16] )

ins.close()

batch_rename(array,os.getcwd())


