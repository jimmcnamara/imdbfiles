def main():
	f=open('DX.csv','r')
	dxlist={}
	for line in f:
		dxId=line.split(',')
		newDxId=dxId[1].rstrip()
		dxlist[dxId[0]]=newDxId
	with open('DX1.csv','w') as outstream:
		for i in dxlist:
			outstream.write(i)
			outstream.write('\t')
			outstream.write(dxlist[i])
			outstream.write('\n')
		outstream.close()


if __name__ == '__main__':
	main()




