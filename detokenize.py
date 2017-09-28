#!/usr/bin/python
#-*-coding:utf-8 -*-
# author: mld
# email: miradel51@126.com
# date : 2017/9/28


import sys
import string
import re


def de_tokenizestr(original_str):

	after_de_tok = ""

	original_str = original_str.replace(" [","[")
	original_str = original_str.replace(" !",'!')
	original_str = original_str.replace(" %","%")
	original_str = original_str.replace(" #","#")
	original_str = original_str.replace(" @","@")
	original_str = original_str.replace("~ ","~")
	original_str = original_str.replace(" &","&")
	original_str = original_str.replace(" *","*")
	original_str = original_str.replace(" .",".")
	original_str = original_str.replace(" ;",";")
	original_str = original_str.replace(" ,",",")
	original_str = original_str.replace(" ^","^")
	original_str = original_str.replace(" (","(")
	original_str = original_str.replace(" )",")")
	original_str = original_str.replace(" {","{")
	original_str = original_str.replace(" >",">")
	original_str = original_str.replace(" ?","?")
	original_str = original_str.replace(" }","}")
	original_str = original_str.replace(" -","-")
	original_str = original_str.replace(" :",":")
	original_str = original_str.replace(" =","=")
	original_str = original_str.replace(" +","+")

	after_de_tok = original_str
	
	return after_de_tok

if __name__ == '__main__':

	ori_ = sys.argv[1]
	de_tok_ = sys.argv[2]

	ori_file = open(ori_,"r")
	de_tok_file = open(de_tok_,"w")

	context = ""

	for eachline in ori_file:

		context = eachline.strip()

		#need to tokenization (just separate symboles from words in current line)
		context = de_tokenizestr(context)

		de_tok_file.write(context)
		de_tok_file.write("\n")

ori_file.close()
de_tok_file.close()