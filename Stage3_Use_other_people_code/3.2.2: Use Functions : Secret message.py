#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
###My solution
#import osx functions
#
#liste de fichiers
#for every elements in list :
#	if un des deux premiers caractère est un chiffre, retire
#	OU retir les deux premiers
#

import os
import sys

def rename_files():
	# (1) get file names from a folder
	file_list_before = os.listdir("/Users/camille/Google Drive/Udacity/Stage 3_Use other people code/3.2.2_images")
	file_list_after = []
	print (file_list_before)


	# (2) for each file, rename filename
	os.chdir("/Users/camille/Google Drive/Udacity/Stage 3_Use other people code/3.2.2_images")
	for file_name in file_list_before:
		print "name before : " + str(file_name)
		renamed = file_name.translate(None,"0123456789")
		os.rename(file_name,renamed)
		print "name after : " + str(renamed)

	print (file_list_after)




rename_files()