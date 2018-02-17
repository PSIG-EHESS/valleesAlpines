# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:29:54 2018

@author: Pierre
"""

import csv
import glob
import shutil

liste1 = []
liste2 = []
liste3 = []
liste4 = []

with open('group1.csv','r',encoding="utf8") as csvfile1:
    spamreader = csv.reader(csvfile1,delimiter=';')
    for row in spamreader:
        liste1 += [row[0]+'.jpg']
liste1.pop(0)
csvfile1.close()
with open('group2.csv','r',encoding="utf8") as csvfile2:
    spamreader = csv.reader(csvfile2,delimiter=';')
    for row in spamreader:
        liste2 += [row[0]+'.jpg']
liste2.pop(0)
csvfile2.close()
with open('group3.csv','r',encoding="utf8") as csvfile3:
    spamreader = csv.reader(csvfile3,delimiter=';')
    for row in spamreader:
        liste3 += [row[0]+'.jpg']
liste3.pop(0)
csvfile3.close()
with open('group4.csv','r',encoding="utf8") as csvfile4:
    spamreader = csv.reader(csvfile4,delimiter=';')
    for row in spamreader:
        liste4 += [row[0]+'.jpg']
liste4.pop(0)
csvfile4.close()
liste = [liste1 + liste2 + liste3 + liste4]
myPath = glob.glob('D:\\projetRecherche\\photos-maisons-vallees-alpines\\*')
listNames = []
for name in liste[0]:
    realName = name.split(' ')
    rName = ''
    for i in range(0, len(realName)-2):
        rName += realName[i]
    if rName not in listNames:
        listNames += [rName]
        try:
            for path in myPath:
                try:
                    myFile = glob.glob(path + '\\' + name)
                    shutil.copyfile(myFile[0], 'running2\\Test_bois_hv\\'+name)
                except:
                    pass
        except:
            pass