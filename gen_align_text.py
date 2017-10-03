#!/usr/bin/python
#-*-coding:utf-8 -*-
# author: mld
# email: miradel51@126.com
# date : 2017/9/28
# time : 11:40(am)


import sys
import string
import time
import re

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
	
	t=Timer()
	#print "The process started at : \t"
	#print t.start()
	t.start()

	_src = sys.argv[1]
	_trg = sys.argv[2]
	_com_txt = sys.argv[3]

	src_file = open(_src,'r')
	trg_file = open(_trg,'r')
	combined_file = open(_com_txt,"w")

	src_con = ""
	trg_con = ""
	combination = ""

	separator = " ||| "

	for eachline in src_file:

		scr_con = eachline.strip()
		trg_con = trg_file.readline().strip()
		combination = scr_con + separator + trg_con # it is the format that fast-align needed

		combined_file.write(combination.strip())
		combined_file.write("\n")

src_file.close()
trg_file.close()
combined_file.close()

print "The process was done in : %0.4f s"%(t.finish())

