#!/usr/bin/python
#-*-coding:utf-8 -*-
# author: mld
# email: miradel51@126.com
# date : 2017/9/30
# time : 23:42(pm)

import sys
import re

# Remove the whitespace at the begining or ending of the sentence
# Helps to convert full-width and half-width from chinese sentence
# If there is any english characters among the chinise sentence, it can lowercase the non-chinse symbols

def chinese_norm(original_sen):

	conver_sen = ""

	for char in original_sen:

		_code = ord(char)

		if _code == 0x3000:
			_code = 0x0020
		else:
			_code -= 0xfee0

		# restore the original sentence after converted if it is still not half-width character
		if _code < 0x0020 or _code > 0x7e:
			conver_sen += char
		else:
			conver_sen += chr(_code)

	conver_sen = re.sub(r'\s+', ' ', conver_sen)

	#conver lower
	conver_sen = conver_sen.lower()

	return conver_sen

if __name__ == '__main__':
	
	ori_ = sys.argv[1]
	convert_ = sys.argv[2]

	ori_file = open(ori_,"r")
	converted_file = open(convert_,"w")

	context = ""

	for eachline in ori_file:

		context = chinese_norm(eachline.strip())
		converted_file.write(context)
		converted_file.write("\n")

ori_file.close()
converted_file.close()
