#!/usr/bin/python

import requests
from time import sleep
from subprocess import call
import string
import os
import sys

alarmfile="/var/timer"
tmpfile="/var/timertmp"
data=[]
now=[]

def setvolume(value):
	return 0
def addsong(name):
	return 0
def loadtimes():
	tmp=[]
	f=open(alarmfile, "r")
	for line in f:
		if (line.find(":")>0) :
			tmp.append(line.split(":"))
	
	return tmp

def gettime():
	f=open(tmpfile, "r")
	for line in f:
		if ( line.find(":")>0) :
			return line.split(":")
			break

def check():
	data= loadtimes()
	for item in data:
		if now==[item[0],item[1],item[2],"\n"]:
			return "aufwachen"
			break
	return "weiterschlafen"

def wecken():
	print "aufwachen"
	


while 1==1:
	os.system("date +'%a:%H:%M:'>"+tmpfile)
	now= gettime()
	#print now
	if check()=="aufwachen":
		wecken()
	sleep(1)
	

