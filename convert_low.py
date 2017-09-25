import sys
import string
import os

if __name__ == '__main__':
	in_filename=sys.argv[1]
	out_file_name=sys.argv[2]

	f_original=open(in_filename,'r')
	f_lowercase=open(out_file_name,'w')

	contexts=""
	lowercase=""
	#first_prob=""
	for eachline in f_original:
		contexts=eachline.strip()
		#s = 'hEllo pYthon'
		#print s.upper() #s.lower(),s.capitalize(),s.title()
		#result HELLO PYTHON,hello python,Hello python,Hello Python
		lowercase=contexts.lower()
		f_lowercase.write(lowercase.strip())
		f_lowercase.write('\n')

f_original.close()
f_lowercase.close()




