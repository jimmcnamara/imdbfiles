from lxml import html
import requests
import time
import psycopg2


# psqlconnection=psycopg2.connect(database="imdb1")

def getList():
	"""opens DX file and converts into dictionary with DXs in [0] and IMDB UI [1]"""
	f=open('DX.csv','r')
	dxlist={}
	for line in f:
		dxId=line.split(',') #splits the csv into list of two items
		newDxId=dxId[1].rstrip() #takes /n out
		dxlist[dxId[0]]=newDxId
	return dxlist

def pulllist():
	start=time.time()
	uniqueIds=getList()
	final_list={}
	for i in uniqueIds:
		ident=uniqueIds[i] #sets ident=tt###
		#print(ident)
		try:	
			name=str(ident)
			page = requests.get('http://www.imdb.com/title/'+name+'/?ref_=nv_sr_1')
			tree=html.fromstring(page.content)
	#this is th base IMDB numer which returns 8.2
	#tt3783958
			rating = tree.xpath('//span[@itemprop="ratingValue"]/text()')
			numrates= tree.xpath('//span[@itemprop="ratingCount"]/text()')
			#print(rating[0])
			# put(i,ident,rating[0])
			final_list[i]=[numrates[0],rating[0]]
		except IndexError as e:
			final_list[i]=''
	end=time.time()
	print(end-start)
	return final_list

def main():
	output=pulllist()
	with open('numratingsfile.csv','w') as outstream:
		for i in output:
			outstream.write(i)
			outstream.write('\t')
			outstream.write(output[i])
			outstream.write('\n')
	outstream.close()


# def put(dx,uid,rating):
# 	with connection, connection.cursor() as cursor:
# 		try:
# 			cursor.execute("insert into imdb1 (%s, %s, %s)",(dx,uid,rating))
# 		except:
# 			connection.rollback()
# 			cursor.execute("update imdb1 set rating=%s where dx=%s",(rating,dx))
# 	connection.commit()



if __name__ == "__main__":
	main()

