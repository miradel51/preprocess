#!/usr/bin/python
#-*-coding:utf-8 -*-
# author: mld
# email: miradel51@126.com
# date : 2017/9/28


import sys
import string
import re


def tokenizestr(original_str):
	after_tok = ""

	original_str = original_str.replace("[", " [")
	original_str = original_str.replace('!', " !")
	original_str = original_str.replace("%", " %")
	original_str = original_str.replace("#", " #")
	original_str = original_str.replace("@", " @")
	original_str = original_str.replace("~", "~ ")
	original_str = original_str.replace("&", " &")
	original_str = original_str.replace("*", " *")
	original_str = original_str.replace(".", " .")
	original_str = original_str.replace(";", " ;")
	original_str = original_str.replace(",", " ,")
	original_str = original_str.replace("^", " ^")
	original_str = original_str.replace("(", " (")
	original_str = original_str.replace(")", " )")
	original_str = original_str.replace("{", " {")
	original_str = original_str.replace(">", " >")
	original_str = original_str.replace("?", " ?")
	original_str = original_str.replace("}", " }")
	original_str = original_str.replace("-", " -")
	original_str = original_str.replace(":", " :")
	original_str = original_str.replace("=", " =")
	original_str = original_str.replace("+", " +")

	after_tok = original_str
	return after_tok

if __name__ == '__main__':

	ori_ = sys.argv[1]
	tok_ = sys.argv[2]

	ori_file = open(ori_,"r")
	tok_file = open(tok_,"w")

	context = ""

	for eachline in ori_file:

		context = eachline.strip()

		#need to tokenization (just separate symboles from words in current line)
		context = tokenizestr(context)

		tok_file.write(context)
		tok_file.write("\n")

ori_file.close()
tok_file.close()
