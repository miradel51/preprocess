#!usr/bin/python
#-*-coding:utf-8-*-
#auhor : mld
#email : miradel51@126.com
#date : 2017/09/21
#time : 20:43

import sys
import string
import re
import pdb
import time

class Timer(object):

	def __init__(self):
		self.total = 0

	def start(self):
		self.start_time = time.time()
		return self.start_time

	def finish(self):
		self.total += time.time() - self.start_time
		return self.total

if __name__ == '__main__':
	
	t = Timer()
	t.start()

	origin_line = ""
	begin_pos = 0
	end_pos = 0

	senline = 0 # in order to validate whether discard any line or not

	ori_corpus = sys.argv[1]
	rmv_sgm = sys.argv[2]

	f_ori_corpus = open(ori_corpus,"r")
	f_no_sgm = open(rmv_sgm,"w")

	for eachline in f_ori_corpus:

		senline += 1
		eachline = eachline.strip()
		end_pos = eachline.find("</seg>")
		begin_pos = eachline.find("\">")

		if eachline.count("</seg>") != 0 and eachline.count("id=\"") != 0:

			eachline = eachline[begin_pos+2:end_pos-1]

			f_no_sgm.write(eachline.strip())
			f_no_sgm.write("\n")

	f_ori_corpus.close()
	f_no_sgm.close()

print "Processed total line is : %d"%(senline)
print "Process total time is : %0.8f s"%(t.finish())

