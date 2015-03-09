import urllib2
from re import *
"""
#url = "http://jandan.net/ooxx/page-1341#comments"
url = "http://www.archdaily.com/603088/brillhart-house-brillhart-architecture/"

html_content = urllib2.urlopen(url).read()

#print html_content

txt=open("archdaily.txt",'w')

img_link = findall("http://ad009cdnb.archdaily.net/wp-content/uploads/20.*.jpg",html_content)
#http://ad009cdnb.archdaily.net/wp-content/uploads/2015/02/54eebdf9e58ecea943000089_brillhart-house-brillhart-architecture_rear-exterior_credit-stefani-fachini-530x304.jpg
#http://ad009cdnb.archdaily.net/wp-content/uploads/2015/02/54eebd48e58ecea943000083_brillhart-house-brillhart-architecture_exterior_credit-stefani-fachini-530x263.jpg
#http://ad009cdnb.archdaily.net.s3.amazonaws.com/wp-content/uploads/2015/02/54eebd15e58ece892500007a_brillhart-house-brillhart-architecture_bookscases_credit-stefani-fachini-1000x337.jpg
#    http://www.archdaily.com/603088/brillhart-house-brillhart-architecture/54eebd15e58ece892500007a_brillhart-house-brillhart-architecture_bookscases_credit-stefani-fachini-jpg
for i in img_link:
	print i
	txt.write(i+"\n")

txt.close
"""
url = str(raw_input("type in the url\n>"))

html_content = urllib2.urlopen(url).read()

img_url = findall("http://ad009cdnb.archdaily.net/wp-content/uploads/20.*?.jpg", html_content)
img_url2 = findall("http://ad009cdnb.archdaily.net.s3.amazonaws.com/wp-content/uploads/20.*?urban-house-in-tua-do-lindo-vale-ana-cl-udia-monteiro-v-tor-oliveira.*?.jpg", html_content)

for i in img_url2:
	print i
#print len(img_url)
"""
a = img_url.pop()
if len(a) == 217:
	b = url + a[69:206] + "jpg/" # high
else:
	b = url + a[69:208] + "jpg/" # painel
print b
"""
