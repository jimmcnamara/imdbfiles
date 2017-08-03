from lxml import html
import requests

def main():
	page = requests.get('http://www.imdb.com/title/tt1959563/?ref_=nv_sr_1')
	tree=html.fromstring(page.content)


	rating = tree.xpath('//span[@class="subText"]/text()')
	#print(rating[0])
	num=filter(str.isdigit,rating[0])
	nums=''
	for i in num:
		nums+=i
	print(nums)	
	# for i in str(rating):
	# 	if i in range(10):
	# 		nums.append(i)
	# print(nums)	

if __name__ == "__main__":
	main()

