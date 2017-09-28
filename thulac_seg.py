#!/usr/bin/python
#-*-coding:utf-8 -*-
# author: mld
# email: miradel51@126.com
# date : 2017/9/28

import thulac
import sys
import string

def ch_seg_line(eachline):

	seg_line = ""

	thu1 = thulac.thulac(seg_only=True)  #only split but not tag
	seg_line = thu1.cut(eachline,text=True) #splitted input_ch
	seg_line = seg_line.strip()

	return seg_line

def ch_seg_file(original,seged):

	thu1 = thulac.thulac(seg_only=True)
	thu1.cut_f(original,seged)

	return thu1

if __name__ == '__main__':

	ori_ = sys.argv[1]
	seg_ = sys.argv[2]

	ori_file = open(ori_,"r")
	seg_file = open(seg_,"w")

	context = ""

	'''
	for eachline in ori_file:

		context = ch_seg_line(context)
		seg_file.write(context)
		seg_file.write("\n")
	'''

	ch_seg_file(ori_,seg_)


ori_file.close()
seg_file.close()




